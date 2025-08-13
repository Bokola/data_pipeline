from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import data_pipeline_project


@dbt_assets(manifest=data_pipeline_project.manifest_path)
def data_pipeline_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    

