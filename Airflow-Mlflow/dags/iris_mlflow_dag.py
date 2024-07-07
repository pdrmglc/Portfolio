from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle

# Definindo argumentos default da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}

# Definindo a DAG
dag = DAG(
    'iris_mlflow_dag',
    default_args=default_args,
    description='DAG que treina um modelo com o dataset Iris e registra no MLflow',
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['example'],
)

# Função para carregar os dados
def load_data(**kwargs):
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    with open('/tmp/train_test_data.pkl', 'wb') as f:
        pickle.dump((X_train, X_test, y_train, y_test), f)

# Função para processar os dados
def process_data(**kwargs):
    with open('/tmp/train_test_data.pkl', 'rb') as f:
        X_train, X_test, y_train, y_test = pickle.load(f)
    # Não há necessidade de processamento adicional para este exemplo
    with open('/tmp/processed_data.pkl', 'wb') as f:
        pickle.dump((X_train, X_test, y_train, y_test), f)

# Função para treinar o modelo
def train_model(**kwargs):
    with open('/tmp/processed_data.pkl', 'rb') as f:
        X_train, X_test, y_train, y_test = pickle.load(f)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='macro'),
        'recall': recall_score(y_test, y_pred, average='macro'),
        'f1_score': f1_score(y_test, y_pred, average='macro')
    }
    with open('/tmp/model_and_metrics.pkl', 'wb') as f:
        pickle.dump((model, metrics), f)

# Função para registrar no MLflow
def log_model(**kwargs):
    with open('/tmp/model_and_metrics.pkl', 'rb') as f:
        model, metrics = pickle.load(f)
    mlflow.set_tracking_uri("http://mlflow-server:5000")
    mlflow.set_experiment("iris_mlflow_experiment")
    with mlflow.start_run():
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", metrics['accuracy'])
        mlflow.log_metric("precision", metrics['precision'])
        mlflow.log_metric("recall", metrics['recall'])
        mlflow.log_metric("f1_score", metrics['f1_score'])
        mlflow.sklearn.log_model(model, "model")

# Definindo as tarefas
load_data_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

process_data_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag,
)

train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

log_model_task = PythonOperator(
    task_id='log_model',
    python_callable=log_model,
    dag=dag,
)

# Definindo a ordem das tarefas
load_data_task >> process_data_task >> train_model_task >> log_model_task
