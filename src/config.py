import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

EXP_FILENAME = os.getenv("EXP_FILENAME") or "exp.csv"
EXP_FILE_PATH = os.path.join(dirname, "..", "data", EXP_FILENAME)

MAIN_FILE_PATH = os.path.join(dirname, "..", "data")
