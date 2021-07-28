"""Demo for trigger by cloud function."""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id='composer_sample_trigger_response_dag',
    start_date=days_ago(1),
    schedule_interval=None) as dag:

    # Print the received dag_run configuration.
    # The DAG run configuration contains information about the
    # Cloud Storage object change.
    t1 = BashOperator(
        task_id='print_gcs_info',
        bash_command='echo Triggered from GCF: {{ dag_run.conf }}',
        dag=dag)

    t1
