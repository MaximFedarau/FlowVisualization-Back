from pathlib import Path

from app.utils.clear_dir import clear_dir


def test_clear_dir(tmp_path: Path) -> None:
    """Test clear_dir method.

    Args:
        tmp_path (Path): pytest fixture path

    """
    data_dir = tmp_path / "dir"
    data_dir.mkdir()
    inner_dir = data_dir / "inner"
    inner_dir.mkdir()
    first_file = inner_dir / "first.txt"
    first_file.write_text("First")
    second_file = data_dir / "second.txt"
    second_file.write_text("Second")
    clear_dir(data_dir)
    assert not data_dir.exists()
    assert not inner_dir.exists()
    assert not first_file.exists()
    assert not second_file.exists()
