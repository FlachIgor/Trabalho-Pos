"""
This is a boilerplate pipeline 'LeituraDados'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import load_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_data,
            inputs=None,
            outputs='intermediate_data',
            name='NoImportaDados'
        )
    ])
