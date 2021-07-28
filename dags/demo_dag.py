"""For demo."""
import datetime
import time
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)

default_args = {
    'owner': 'mark',
    'depends_on_past': False,
    'email': [''],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
    'start_date': YESTERDAY,
}

def my_sleeping_function(sec: int):
    print(f'sleep for {sec} seconds...')
    time.sleep(sec)

with DAG(
        'composer_demo_dag',
        default_args=default_args,
        schedule_interval=datetime.timedelta(days=1)) as dag:
    
    start = DummyOperator(
        task_id='start'
    )

    # Print the dag_run id from the Airflow logs
    print_dag_run_conf = BashOperator(
        task_id='print_dag_run_conf', bash_command='echo {{ dag_run.id }}')
    
    t1 = PythonOperator(
        task_id='task_1', python_callable=my_sleeping_function,
        op_kwargs={'sec': 10}
    )

    t2 = BashOperator(
        task_id='task_2', bash_command='echo "execute task 2!"'
    )

    t3 = BashOperator(
        task_id='task_3', bash_command='echo "execute task 3!"'
    )

    t4 = BashOperator(
        task_id='task_4', bash_command='echo "execute task 4!"'
    )

    end = DummyOperator(
        task_id='end'
    )

    start >> print_dag_run_conf >>[t1, t2, t3, t4] >> end
