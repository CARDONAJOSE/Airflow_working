from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

from airflow.contrib.sensors.file_sensor import FileSensor
from datetime import datetime, timedelta 
# from airflow.sensors.filesystem import FileSensor


with DAG(dag_id='filesensor',
        description='FileSensor',
        schedule_interval= "@daily",
        start_date=datetime(2022, 8, 20),
        end_date=datetime(2022, 8, 25),
        max_active_runs=1,
        tags=['']
):

    start = BashOperator(task_id='start',
                        bash_command= "echo 'comencemos'"
                        )

    t3= bash_task = BashOperator(
        task_id = "t3",
        bash_command = "sleep 10 && touch /tmp/file.txt",
        # env: Optional[Dict[str, str]] = None,
        # output_encoding: str = 'utf-8',
        # skip_exit_code: int = 99,
    )
    
    t4= FileSensor( task_id= "t4",
                    filepath="/tmp/file.txt"
                    )

    end = BashOperator(task_id='end',
                        bash_command= "echo 'el fichero esta aqui'"
                        )

    start >> t3 >> end