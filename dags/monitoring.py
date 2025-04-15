from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def myfunction():
    pass
with DAG(dag_id="monitoring",
        description="surveiller notre  DAG",
        schedule_interval="@daily",
        start_date=datetime(2022, 1, 1),
        end_date=datetime(2022, 2, 1),
        # catchup=False  # Evita ejecuciones históricas no deseadas
        default_args={
        "retries": 1,  # Reintenta 1 vez antes de marcar como fallida
        "depends_on_past": False}  # No depende de ejecuciones anteriores

) as dag:

    t1 = BashOperator(task_id="work_1",
                    bash_command="sleep 2 && echo 'Primera tache!'")

    t2 = BashOperator(task_id="work_2",
                    bash_command="sleep 2 && echo 'Segunda tache!'")

    t3 = BashOperator(task_id="work_3",
                    bash_command="sleep 2 && echo 'Tercera tache!'")

    t4 = PythonOperator(task_id="work_4",
                    python_callable=myfunction)

    t5 = BashOperator(task_id="work_5",
                    bash_command="sleep 2 && echo 'Quinta tache!'")


    t1 >> t2 >> t3 >> t4 >> t5
