from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import data_pipeline_dbt_assets
from .project import data_pipeline_project
from .schedules import schedules

defs = Definitions(
    assets=[data_pipeline_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=data_pipeline_project),
    },
)

