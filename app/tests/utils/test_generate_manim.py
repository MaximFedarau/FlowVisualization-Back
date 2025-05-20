import json
from pathlib import Path

from app.utils.generate_manim import CreateFlow


def test_generate_manim(tmp_path: Path) -> None:
    """Test generate_manim.

    Args:
        tmp_path (Path): pytest fixture path

    """
    flow_creator = CreateFlow()
    data_path = tmp_path / "data.json"
    data = {"data": "sample"}
    data_path.write_text(json.dumps(data))
    flow_creator.read_data(data_path.as_posix())
    assert flow_creator.data == data
