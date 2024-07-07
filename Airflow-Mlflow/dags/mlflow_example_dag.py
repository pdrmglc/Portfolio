from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import mlflow

# Definindo argumentos default da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}

# Definindo a DAG
dag = DAG(
    'mlflow_example',
    default_args=default_args,
    description='Uma DAG simples para testar integração com MLflow',
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['example'],
)

# Função que inicia um experimento no MLflow
def start_mlflow_experiment():
    mlflow.set_tracking_uri("http://mlflow-server:5000")
    mlflow.set_experiment("airflow_mlflow_experiment")
    with mlflow.start_run():
        mlflow.log_param("param1", 5)
        mlflow.log_metric("metric1", 0.85)
        mlflow.log_artifact("/opt/airflow/dags/mlflow_example_dag.py")

# Definindo a tarefa
run_mlflow_task = PythonOperator(
    task_id='run_mlflow',
    python_callable=start_mlflow_experiment,
    dag=dag,
)

# Definindo a ordem das tarefas
run_mlflow_task
