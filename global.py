# global.py ------------------------------------------------------------ #
# Author: Louis Trocellier
# Description: Load packages, project configuration, logging, and helper functions.

import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv
import yaml

# Path Setup --------------------------------------------------------------- #
PROJECT_ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))

# Environment & Configuration ---------------------------------------------- #
load_dotenv(PROJECT_ROOT / ".env")
APP_ENV = os.getenv("APP_ENV", "default")

with open(PROJECT_ROOT / "config.yml", "r", encoding="utf-8") as f:
    raw_config = yaml.safe_load(f)
    config = raw_config.get(APP_ENV, raw_config.get("default", {}))

# Directories -------------------------------------------------------------- #
paths = config["paths"]
DATA_DIR = PROJECT_ROOT / paths["data"]
OUTPUTS_DIR = PROJECT_ROOT / paths["outputs"]
LOGS_DIR = PROJECT_ROOT / paths["logs"]
SCRIPTS_DIR = PROJECT_ROOT / paths["scripts"]
FUNCTIONS_DIR = PROJECT_ROOT / paths["functions"]

for directory in [DATA_DIR, OUTPUTS_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# Logging Setup ------------------------------------------------------------ #
log_config = config.get("logging", {})
log_level = getattr(logging, log_config.get("level", "INFO").upper(), logging.INFO)

handlers = [logging.StreamHandler(sys.stdout)]
if log_config.get("log_to_file", True):
    handlers.append(logging.FileHandler(LOGS_DIR / "pipeline.log", encoding="utf-8"))

logging.basicConfig(
    level=log_level,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=handlers
)
logger = logging.getLogger("pipeline")

# Script Discovery ---------------------------------------------------------- #
pipeline_scripts = sorted(SCRIPTS_DIR.glob("[0-9]*_*.py"))

logger.info(f"Environment: {APP_ENV} | Found scripts: {[s.name for s in pipeline_scripts]}")