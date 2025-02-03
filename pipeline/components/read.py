

from google.cloud import bigquery


def execute(temp_root):
    """
    Execute reading from BigQuery and
    save results as a parquet file
    """
    client = bigquery.Client(
        project='my-project'
    )

    with open("query-inputs.sql") as f:
        query = f.read()

    df = client.query(query).to_dataframe()

    logging.info(f"DF size: {df.shape}")
    df.to_parquet(
        f"{temp_root}/input.parquet"
    )







    


