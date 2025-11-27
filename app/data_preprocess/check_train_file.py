from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

out_dir = Path(__file__).parent / "out"
out_dir.mkdir(parents=True, exist_ok=True)


def read_img_parquet_to_dataframe(
    file_path="/data/corpus/ocr/findableai/phenology/df_labels_and_images.parquet",
):
    # Read the Parquet file into a PyArrow Table
    table = pq.read_table(file_path)
    img_name = "barley_maturing_time"
    for row in table.to_pylist():
        print(f'{type(row) = }')
        img = row.get(f"{img_name}_image", None)
        labels = row.get(f"{img_name}_labels", None)
        if img:
            out_img_path = out_dir / f"{img_name}_image.png"
            with open(out_img_path, "wb") as img_file:
                img_file.write(img)
            print(f"Sample image written to: {out_img_path}")
            out_label_path = out_dir / f"{img_name}_labels.txt"
            with open(out_label_path, "w", encoding="utf-8") as f:
                if labels is not None:
                    f.write(labels)
            break  # Print only the first row for brevity

    log_file = out_dir / (Path(file_path).stem + "_columns.log")
    columns = table.schema.names
    img_columns = [col for col in columns if col.endswith("_image")]
    unique_img_columns = set(img_columns)
    label_columns = [col for col in columns if col.endswith("_labels")]
    unique_label_columns = set(label_columns)
    columns_from_img = [col.removesuffix("_image") for col in img_columns]
    columns_from_labels = [col.removesuffix("_labels") for col in label_columns]
    common_columns = set(columns_from_img).intersection(set(columns_from_labels))
    print(f'{len(common_columns) = }')
    print(f'{len(img_columns) = }, {len(label_columns) = }')
    print(f'{len(unique_img_columns) = }, {len(unique_label_columns) = }')
    with open(log_file, "w", encoding="utf-8") as f:
        for column in table.schema.names:
            f.write(f"{column}\n")


read_img_parquet_to_dataframe()
