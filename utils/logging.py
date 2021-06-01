import logging
import sys
from pathlib import Path


def setup_logging() -> None:
    # Prepare directory for store log
    log_dir = Path(".temp")
    log_dir.mkdir(parents=True, exist_ok=True)

    # REF: https://stackoverflow.com/a/61484381
    file_handler = logging.FileHandler(log_dir / "app.log")
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[file_handler, console_handler],
    )
