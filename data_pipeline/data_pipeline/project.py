from pathlib import Path

from dagster_dbt import DbtProject

data_pipeline_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
data_pipeline_project.prepare_if_dev()

