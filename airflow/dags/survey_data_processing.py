import csv

from airflow import macros
from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils import timezone


def _answer_count():
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

    with open('/opt/airflow/dags/answer_count.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['answer', 'value'])
        writer.writerows(results.items())

    return '/opt/airflow/dags/answer_count.csv'


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

    answer_count = PythonOperator(
        task_id='answer_count',
        python_callable=_answer_count,
    )

    end = DummyOperator(task_id='end')

    start >> answer_count >> end
