from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


#Task 1 - Define the DAG arguments
default_args = {
    'owner': 'munna',
    'start_date': days_ago(0),
    'email': ['munnazaishy@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Task 2 - Define the DAG
dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='DAG for processing web server logs',
    schedule_interval=timedelta(days=1),
)

# Task 3: Extract data
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" /path/to/web_server_log.txt > /path/to/extracted_data.txt',
    dag=dag,
)

# Task 4: Transform data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v "198.46.149.143" /path/to/extracted_data.txt > /path/to/transformed_data.txt',
    dag=dag,
)


# Task 5: Load data
load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -cvf /path/to/weblog.tar /path/to/transformed_data.txt',
    dag=dag,
)


# Define the task sequence
extract_data >> transform_data >> load_data
