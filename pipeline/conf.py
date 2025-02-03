import os

BASE_PATH = "gs://pipelines/dwarf"

PIPELINE_NAME = "my-pipeline"
PIPELINE_ROOT = f"{BASE_PATH}/{PIPELINE_NAME}"
PIPELINE_TEMP_ROOT = f"{BASE_PATH}/{PIPELINE_NAME}-temp"

PIPELINE_DISPLAY_NAME = "My Pipeline"
PIPELINE_DESCRIPTION = "My pipeline description"

NETWORK_NAME = "my-network"

DOCKER_IMAGE = os.getenv("DOCKER_IMAGE")
BASE_IMAGE = "python:3.11"
PROJECT_ID = "my-project"
PROJECT_REGION = "us-central1"

SERVICE_ACCOUNT = "my-service-account@my-project.iam.gserviceaccount.com"
SCHEDULE_NAME = "My Pipeline"
