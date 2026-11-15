from pathlib import Path

def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def existance_check(path: str | Path) -> bool:
    path = Path(path)
    if path.exists(): return True
    return False