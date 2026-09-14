# tests/conftest.py -------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Pytest configuration and shared fixtures.

import pytest
from settings import DATA_DIR, config


@pytest.fixture
def temp_data_dir(tmp_path):
    """Crée un dossier de données temporaire pour isoler les tests."""
    data_dir = tmp_path / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir

@pytest.fixture
def sample_settings():
    """Injecte directement la configuration chargée depuis config.yml."""
    return config