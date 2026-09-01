from pathlib import Path
import os
from dotenv import load_dotenv




BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# Enviroment 
APP_ENV = os.getenv("APP_ENV", "development")

# INPUT FILE
INPUT_FILENAME = os.getenv("INPUT_FILENAME", "orders.csv")

# directories
DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Files
INPUT_FILE = RAW_DATA_DIR / INPUT_FILENAME

CLEAN_OUTPUT = PROCESSED_DATA_DIR / "clean_orders.csv"

SUMMARY_OUTPUT = PROCESSED_DATA_DIR / "summary_report.json"

LOG_DIR = BASE_DIR / "logs"

LOG_FILE = LOG_DIR / "application.log"