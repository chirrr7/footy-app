from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_model_config(path: str | Path) -> dict[str, Any]:
    """Load a versioned FUTX model configuration."""
    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)
