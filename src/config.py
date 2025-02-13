from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

log_dir=BASE_DIR.joinpath('logs')
log_dir.mkdir(exist_ok=True)