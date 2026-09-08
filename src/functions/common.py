# src/functions/common.py ------------------------------------------------- #
# Author: Louis Trocellier
# Description: Shared functions used across all scripts.

import sys
from pathlib import Path
from importlib import util
from loguru import logger

# Utilities ---------------------------------------------------------------- #
def source_directory(directory: Path, pattern: str = "*.py") -> None:
    """
    Dynamically import all Python files in a directory.
    
    Args:
        directory: Path to directory containing .py files
        pattern: File pattern to match (default: "*.py")
    """
    directory = Path(directory)
    if not directory.exists():
        logger.warning(f"Directory not found: {directory}")
        return
    
    for file_path in sorted(directory.glob(pattern)):
        if file_path.name.startswith("__"):
            continue
        
        try:
            spec = util.spec_from_file_location(file_path.stem, file_path)
            if spec and spec.loader:
                module = util.module_from_spec(spec)
                sys.modules[file_path.stem] = module
                spec.loader.exec_module(module)
                logger.debug(f"Loaded module: {file_path.stem}")
        except Exception as e:
            logger.error(f"Failed to load {file_path}: {e}")


def get_pipeline_scripts(scripts_dir: Path) -> list[Path]:
    """
    Get ordered list of pipeline scripts from scripts directory.
    
    Args:
        scripts_dir: Path to scripts directory
        
    Returns:
        List of script paths sorted by name
    """
    scripts_dir = Path(scripts_dir)
    if not scripts_dir.exists():
        logger.warning(f"Scripts directory not found: {scripts_dir}")
        return []
    
    # Get all .py files starting with numbers (e.g., 01_*.py, 02_*.py)
    scripts = [
        f for f in scripts_dir.glob("*.py")
        if f.is_file() and not f.name.startswith("__")
    ]
    
    return sorted(scripts)


# Formatting ----------------------------------------------- #
def format_output(data):
    """Format output data for display."""
    # TODO: Add custom formatting functions
    return data


# Display --------------------------------------------------- #
def display_summary(data) -> None:
    """Display summary information."""
    # TODO: Add common display functions
    pass
