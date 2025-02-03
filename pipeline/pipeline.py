from kfp import dsl

import conf
DOCKER_IMAGE = conf.DOCKER_IMAGE


@dsl.component(base_image=DOCKER_IMAGE)
def temp_root_component() -> str:
    """
    Generate temporary root for a given run
    """
    from datetime import datetime

    pattern = "%Y-%m-%d %H:%M:%S"
    run_datetime = datetime.now().strftime(pattern)
    temp_root = f"gs://pipelines/runs/dwarf/{run_datetime}"
    return temp_root


@dsl.component(base_image=DOCKER_IMAGE)
def read_component(temp_root: str) -> None:
    # read step
    from components import read

    read.execute(temp_root)


@dsl.component(base_image=DOCKER_IMAGE)
def predict_component(temp_root: str):
    from components import predict

    predict.execute(temp_root)


@dsl.component(base_image=DOCKER_IMAGE)
def write_component(temp_root: str):
    """
    Write output to BigQuery
    """
    from components import write

    write.execute(temp_root)


@dsl.pipeline(
    name=conf.PIPELINE_NAME,
    description=conf.PIPELINE_DESCRIPTION,
    pipeline_root=conf.PIPELINE_ROOT,
)
def pipeline():
    temp_root_step = temp_root_component()
    temp_root = temp_root_step.output

    read_step = read_component(temp_root=temp_root)
    predict_step = predict_component(temp_root=temp_root).after(read_step)
    write_step = write_component(temp_root=temp_root).after(predict_step)
