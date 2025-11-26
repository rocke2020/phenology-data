from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from constants import SYSTEM_PROMPT
from helper_funcs import display_image

out_dir = Path(__file__).parent / "out"
out_dir.mkdir(parents=True, exist_ok=True)
cols_to_predict = [
    "wild_strawberry_timespan",
    "wood_sorrel_flowering",
    "wood_sorrel_fruit",
    "wood_sorrel_timespan",
    "arctic_starflower_flowering",
    "arctic_starflower_fruit",
    "arctic_starflower_timespan",
    "linnaea_flowering",
    "linnaea_fruit",
    "linnaea_timespan",
]

FILE_PATH = "/data/corpus/findableai/phenology/df_labels_and_images.parquet"


def read_data():
    table = pq.read_table(file_path)

    # Convert the PyArrow Table to a Pandas DataFrame
    dataframe = table.to_pandas()
    print(
        f"DataFrame loaded with {len(dataframe)} rows and {len(dataframe.columns)} columns.\ndataframe.head():\n{dataframe.head()}"
    )
