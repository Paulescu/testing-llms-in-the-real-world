from pathlib import Path

ROOT_DIR = Path(__file__).parent.resolve().parent

ARTIFACTS_DIR = ROOT_DIR / 'artifacts'

MODEL_DIR = ARTIFACTS_DIR / 'model'
if not MODEL_DIR.exists():
    Path(MODEL_DIR).mkdir(parents=True)

DATASET_DIR = ARTIFACTS_DIR / 'dataset'
if not DATASET_DIR.exists():
    Path(DATASET_DIR).mkdir(parents=True)

REPORTS_DIR = ROOT_DIR / 'report'
if not REPORTS_DIR.exists():
    Path(REPORTS_DIR).mkdir(parents=True)