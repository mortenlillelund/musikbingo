from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "output"

SONG_DATABASE = DATA_DIR / "songs.csv"

ROWS = 5
COLS = 5

CARD_SIZE = ROWS * COLS

DEFAULT_NUMBER_OF_CARDS = 100

DEFAULT_RANDOM_SEED = 2026

YEAR_MIN = 1960
YEAR_MAX = 1995
