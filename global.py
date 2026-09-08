# global.py ------------------------------------------------------------ #
# Author: Louis Trocellier
# Description: Load packages, project configuration, logging, and helper functions.

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from loguru import logger
import yaml

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))

# Environment & Configuration ---------------------------------------------- #
# Load environment variables from .env if present
env_file = PROJECT_ROOT / ".env"
if env_file.exists():
    load_dotenv(env_file)

# Get the environment name (defaults to 'default')
APP_ENV = os.getenv("APP_ENV", "default")

# Load configuration from config.yml
config_file = PROJECT_ROOT / "config.yml"
config = {}
if config_file.exists():
    with open(config_file, "r", encoding="utf-8") as f:
        all_config = yaml.safe_load(f)
        # Get environment-specific config, fallback to default
        config = all_config.get(APP_ENV, all_config.get("default", {}))
else:
    raise FileNotFoundError(f"Configuration file not found: {config_file}")

# Logging Setup ------------------------------------------------------------ #
# Remove default handler
logger.remove()

# Get log configuration
log_config = config.get("logging", {})
log_level = log_config.get("level", "DEBUG")
log_to_file = log_config.get("log_to_file", True)

# Add console logger
logger.add(sys.stderr, level=log_level, format="<level>{time:YYYY-MM-DD HH:mm:ss}</level> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")

# Add file logger if enabled
if log_to_file:
    log_dir = PROJECT_ROOT / config.get("paths", {}).get("logs", "logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "pipeline.log"
    logger.add(log_file, level=log_level, rotation="10 MB", retention="7 days")

# Setup paths ----------------------------------------------------------- #
paths = config.get("paths", {})
FUNCTIONS_DIR = PROJECT_ROOT / paths.get("functions", "src/functions")
SCRIPTS_DIR = PROJECT_ROOT / paths.get("scripts", "scripts")
DATA_DIR = PROJECT_ROOT / paths.get("data", "data")
OUTPUTS_DIR = PROJECT_ROOT / paths.get("outputs", "outputs")
LOGS_DIR = PROJECT_ROOT / paths.get("logs", "logs")

# Ensure directories exist
for directory in [SCRIPTS_DIR, DATA_DIR, OUTPUTS_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Import helper functions
from src.functions.common import source_directory, get_pipeline_scripts

# Source all functions from functions directory
logger.info(f"Loading functions from {FUNCTIONS_DIR}")
source_directory(FUNCTIONS_DIR)

# Script Discovery ---------------------------------------------------------- #
pipeline_scripts = get_pipeline_scripts(SCRIPTS_DIR)

logger.info(f"Found {len(pipeline_scripts)} pipeline scripts: {[s.stem for s in pipeline_scripts]}")
