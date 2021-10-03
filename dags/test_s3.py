from airflow.decorators import dag, task
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

default_args = {
    'owner': 'airflow',
}


@dag(default_args=default_args, schedule_interval=None, start_date="2021-09-30", tags=['example'])
def test_s3():

    @task
    def write_to_s3():
        S3Hook.load_string("Some test data", key="first", bucket_name="test-airflow")

    write_to_s3()


test_s3_dag = test_s3()

