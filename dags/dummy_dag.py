from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime


with DAG(
    'example_dag', start_date=datetime(2021, 7, 29), schedule_interval="0 */1 * * *"
) as dag:
    op = DummyOperator(task_id='op')
