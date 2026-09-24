"""Resolve the standalone DataAnalyser workspace."""
from pathlib import Path
import os


def project_root() -> Path:
    configured = os.environ.get("DATA_ANALYSER_ROOT")
    if configured:
        root = Path(configured).expanduser().resolve()
        if not (root / "config/finance_read_sources.json").is_file():
            raise ValueError("DATA_ANALYSER_ROOT does not contain the read-only source configuration")
        return root
    source_root = Path(__file__).resolve().parents[2]
    if (source_root / "config/finance_read_sources.json").is_file():
        return source_root
    for candidate in (Path.cwd(), *Path.cwd().parents):
        if (candidate / "config/finance_read_sources.json").is_file():
            return candidate.resolve()
    raise ValueError("DataAnalyser project directory not found")
