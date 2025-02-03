import pandas as pd
from orient_express import ModelExpress


def execute(temp_root):
    model_wrapper = ModelExpress(
        model_name="dwarf",
        model_version=4,
        project_name="my-project",
        region="us-central1",
        bucket_name="model_bucket",
    )

    input_df = pd.read_parquet(
        f"{temp_root}/input.parquet"
    )

    df = model_wrapper.local_predict(input_df)
    
    df.to_parquet(
        f"{temp_root}/predicted.parquet"
    )
