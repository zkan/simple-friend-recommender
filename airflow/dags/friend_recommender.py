from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow.utils import timezone


DAGS_FOLDER = '/opt/airflow/dags'
NOTEBOOKS_FOLDER = f'{DAGS_FOLDER}/notebooks'

distance_columns = [
    'data-engineer',
    'data-scientist',
    'cat',
    'dog',
    'data-engineer',
    'data-scientist',
    'cat',
    'dog',
    'mountain',
    'sea',
    'java',
    'python',
    'blackpink',
    'gong-yoo',
]

default_args = {
    'owner': 'zkan'
}
with DAG('friend_recommender',
         default_args=default_args,
         schedule_interval='*/30 * * * *',
         start_date=timezone.datetime(2021, 4, 1),
         catchup=False,
         tags=['dataength', 'ODDS']) as dag:

    start = DummyOperator(task_id='start')

    friend_recommender = PapermillOperator(
        task_id='friend_recommender',
        input_nb=f'{NOTEBOOKS_FOLDER}/friend_recommender.ipynb',
        output_nb=f'{NOTEBOOKS_FOLDER}/friend_recommender_results.ipynb',
        parameters=dict(DAGS_FOLDER=DAGS_FOLDER, distance_columns=distance_columns),
    )

    end = DummyOperator(task_id='end')

    start >> friend_recommender >> end
