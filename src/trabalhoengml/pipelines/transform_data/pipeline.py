"""
This is a boilerplate pipeline 'transform_data'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import transform_data, metric_data, split_train

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=transform_data,
            inputs= 'intermediate_data',
            outputs=['primary_data','primary_data_3PT'],
            name='NoTransformaDados'
        ),
        node(
            func=metric_data,
            inputs= 'primary_data',
            outputs='primary_data_metrics',
            name='NoMetricasDados'
        ),
        node(
            func=split_train,
            inputs= [
                'primary_data',
                'params:test_size',
                'params:test_split_randon_state'],
            outputs=['data_train', 'data_test'],
            name='NoSplitaDados'
        )
    ])
