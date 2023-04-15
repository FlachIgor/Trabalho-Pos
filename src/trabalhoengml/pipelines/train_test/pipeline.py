"""
This is a boilerplate pipeline 'train_test'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_model_lr, train_model_ada, report_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_model_lr,
            inputs= ['data_train','params:n_folds'],
            outputs='final_model_lr',
            name='NoTreinaModeloLr'
        ),
        node(
            func=train_model_ada,
            inputs= ['data_train','params:n_folds'],
            outputs='final_model_ada',
            name='NoTreinaModeloAda'
        ),
        node(
            func=report_model,
            inputs= ['final_model_lr','data_test'],
            outputs='classification_metrics_lr',
            name='NoMetricasLr'
        ),
        node(
            func=report_model,
            inputs= ['final_model_ada','data_test'],
            outputs='classification_metrics_ada',
            name='NoMetricasAda'
        ),
        node(
            func=report_model,
            inputs= ['final_model_lr','primary_data_3PT'],
            outputs='classification_metrics_lr_3PT',
            name='NoMetricasLR3PT'
        ),
        node(
            func=report_model,
            inputs= ['final_model_ada','primary_data_3PT'],
            outputs='classification_metrics_ada_3PT',
            name='NoMetricasAda3PT'
        )
    ])
