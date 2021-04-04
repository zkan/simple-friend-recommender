import csv

from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils import timezone

import pandas as pd


DAGS_FOLDER = '/opt/airflow/dags'


def _dump_survey_data():
    table = 'questions_surveyresponse'
    pg_hook = PostgresHook(postgres_conn_id='survey_db_conn', schema='postgres')
    pg_hook.bulk_dump(table, f'{DAGS_FOLDER}/{table}_export.tsv')

    return f'{DAGS_FOLDER}/{table}_export.tsv'


def _count_survey_answers():
    pg_hook = PostgresHook(postgres_conn_id='survey_db_conn', schema='postgres')
    connection = pg_hook.get_conn()
    cursor = connection.cursor()

    sql = """
        SELECT * FROM questions_surveyresponse
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    results = {}
    for _, _, each in rows:
        for value in each.values():
            if value in results:
                results[value] += 1
            else:
                results[value] = 1

    with open(f'{DAGS_FOLDER}/survey_answer_count.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['answer', 'value'])
        writer.writerows(results.items())

    return f'{DAGS_FOLDER}/survey_answer_count.csv'


def _transform_data_for_recommender(ti):
    filepath = ti.xcom_pull(key='return_value', task_ids=['dump_survey_data'])[0]
    print(filepath)
    df = pd.read_csv(filepath)
    print(df.T)


default_args = {
    'owner': 'zkan',
    'start_date': timezone.datetime(2017, 5, 5),
}
with DAG(dag_id='survey_data_processing',
         default_args=default_args,
         schedule_interval='*/5 * * * *',
         catchup=False,
         tags=['ODDS']) as dag:

    start = DummyOperator(task_id='start')

    count_survey_answers = PythonOperator(
        task_id='count_survey_answers',
        python_callable=_count_survey_answers,
    )

    dump_survey_data = PythonOperator(
        task_id='dump_survey_data',
        python_callable=_dump_survey_data,
    )

    transform_data_for_recommender = PythonOperator(
        task_id='transform_data_for_recommender',
        python_callable=_transform_data_for_recommender,
    )

    end = DummyOperator(task_id='end')

    start >> [count_survey_answers, dump_survey_data] >> end
    dump_survey_data >> transform_data_for_recommender
