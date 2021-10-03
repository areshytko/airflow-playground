import datetime

from airflow.decorators import dag, task
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

default_args = {
    'owner': 'airflow',
}


@dag(default_args=default_args, schedule_interval=None, start_date=datetime.datetime(2021, 9, 30), tags=['example'])
def test_s3():

    @task()
    def write_to_s3():
        print("starting task")
        hook = S3Hook(aws_conn_id="obs-connection")
        hook.load_string("Some test data", key="first", bucket_name="test-airflow")
        print("task ended")

    write_to_s3()


test_s3_dag = test_s3()

