"""
This file should NOT BE EDITED.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parents[1] / "Data"
DATA_FILE = "NASDAQ_100_Data_From_2010.csv"


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / DATA_FILE, date_parser = 'Date')

