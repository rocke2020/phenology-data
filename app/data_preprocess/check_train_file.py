from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

out_dir = Path(__file__).parent / "out"
out_dir.mkdir(parents=True, exist_ok=True)


def read_parquet_to_dataframe(file_path):
    """
    Reads a Parquet file and converts it to a Pandas DataFrame.

    Parameters:
    file_path (str): The path to the Parquet file.

    Returns:
    pd.DataFrame: The resulting Pandas DataFrame.
    """
    # Read the Parquet file into a PyArrow Table
    table = pq.read_table(file_path)

    # Convert the PyArrow Table to a Pandas DataFrame
    dataframe = table.to_pandas()
    print(
        f"DataFrame loaded with {len(dataframe)} rows and {len(dataframe.columns)} columns.\ndataframe.head():\n{dataframe.head()}"
    )
    print(f"{type(dataframe) = }")
    for row_i, row in dataframe.iterrows():
        print(row)
        print(f"\n{type(row) = }")
        blueberry_flowering = row.get("blueberry_flowering", None)
        blueberry_flowering_labels = row.get("blueberry_flowering_labels", None)
        print(f"{blueberry_flowering = }")
        print(f"{type(blueberry_flowering) = }")
        print(f"{blueberry_flowering_labels = }")
        break  # Print only the first row for br

    # for row in dataframe.itertuples():
    #     print(row[:10])
    #     break  # Print only the first row for brevity

    # with open("dataframe_columns.log", "w") as f:
    #     for column in dataframe.columns:
    #         f.write(f"{column}\n")

    return dataframe


def read_img_parquet_to_dataframe(
    file_path="/data/corpus/findableai/phenology/df_labels_and_images.parquet",
):

    # Read the Parquet file into a PyArrow Table
    table = pq.read_table(file_path)

    # Convert the PyArrow Table to a Pandas DataFrame
    dataframe = table.to_pandas()
    print(
        f"DataFrame loaded with {len(dataframe)} rows and {len(dataframe.columns)} columns.\ndataframe.head():\n{dataframe.head()}"
    )
    for row_i, row in dataframe.iterrows():
        print(f"{type(row) = }")
        barley_maturing_time_image = row.get("barley_maturing_time_image", None)
        barley_maturing_time_labels = row.get("barley_maturing_time_labels", None)
        print(f"{type(barley_maturing_time_image) = }")
        print(f"{type(barley_maturing_time_labels) = }, {barley_maturing_time_labels = }")

        out_img_path = out_dir / "barley_maturing_time_image.png"
        if barley_maturing_time_image is not None:
            with open(out_img_path, "wb") as img_file:
                img_file.write(barley_maturing_time_image)
            print(f"Sample image written to: {out_img_path}")
            break  # Print only the first row for br

    # for row in dataframe.itertuples():
    #     print(row[:10])
    #     break  # Print only the first row for brevity
    log_file = out_dir / (Path(file_path).stem + ".log")
    with open(log_file, "w", encoding="utf-8") as f:
        for column in dataframe.columns:
            f.write(f"{column}\n")

    return dataframe


# read_parquet_to_dataframe("vlm_finetuning/data/df_complete.parquet")
read_img_parquet_to_dataframe()
