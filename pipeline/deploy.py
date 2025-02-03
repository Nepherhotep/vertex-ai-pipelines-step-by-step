import argparse
import conf

from pipeline import pipeline
from orient_express.deployment import deploy_pipeline


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-type", required=True)

    args = parser.parse_args()
    deploy_pipeline(run_type=args.run_type,
                    pipeline_dsl=pipeline,
                    pipeline_root=conf.PIPELINE_ROOT,
                    pipeline_name=conf.PIPELINE_NAME,
                    pipeline_display_name=conf.PIPELINE_DISPLAY_NAME,
                    pipeline_schedule_name=conf.SCHEDULE_NAME,
                    gcp_project=conf.PROJECT_ID,
                    gcp_location='us-central1',
                    gcp_service_account=conf.SERVICE_ACCOUNT,
                    gcp_network=conf.NETWORK_NAME,
                    gcp_labels={"team": "ml"})
