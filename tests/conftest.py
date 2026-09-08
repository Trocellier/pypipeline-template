# tests/conftest.py -------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Pytest configuration and shared fixtures.

import pytest
from pathlib import Path
import sys

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def temp_data_dir(tmp_path):
    """Create a temporary data directory for tests."""
    return tmp_path / "data"


@pytest.fixture
def sample_settings():
    """Provide sample settings for fetch_data tests."""
    return {
        "data_source": "raw_sample",
        "max_records": 1000
    }
