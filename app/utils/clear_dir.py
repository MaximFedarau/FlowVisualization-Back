from pathlib import Path


def clear_dir(dirpath: Path) -> None:
    for child in dirpath.iterdir():
        if child.is_file():
            child.unlink()
        else:
            clear_dir(child)
    dirpath.rmdir()
