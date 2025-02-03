import pandas as pd
from google.cloud import bigquery


def execute(temp_root):
    predicted_df = pd.read_parquet(
        f"{temp_root}/predicted.parquet"
    )

    bq_client = bigquery.Client(project='my-project')
    job_config = bigquery.LoadJobConfig()
    table_id = "my-project.ml.creatures"

    job = bq_client.load_table_from_dataframe(
        dataframe=predicted_df,
        table_id=table_id,
        job_config=job_config,
    )
    job.result()
