import os
import subprocess
import argparse
import sys
print("Using Python interpreter:", sys.executable)

import torch_geometric
print("PyTorch Geometric is available")


# Define file paths
RAW_DATA_PATH = "data/raw_transactions.csv"
PROCESSED_DATA_PATH = "data/processed_data.csv"
GRAPH_DATA_PATH = "data/graph_data.pt"
MODEL_PATH = "models/gnn_model.pth"
EDA_REPORT_PATH = "data/EDA_report.pdf"

# Function to execute a script and handle errors
def run_script(script_name):
    try:
        print(f"\n🚀 Running {script_name}...")
        subprocess.run([sys.executable, script_name], check=True)
        print(f"✅ {script_name} completed successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error occurred while running {script_name}: {e}")
        exit(1)

# Data preprocessing step
def preprocess_data():
    if not os.path.exists(PROCESSED_DATA_PATH):
        run_script("src/data_preprocessing.py")
    else:
        print("ℹ️ Processed data already exists. Skipping preprocessing...")

# Graph construction step
def construct_graph():
    if not os.path.exists(GRAPH_DATA_PATH):
        run_script("src/graph_construction.py")
    else:
        print("ℹ️ Graph data already exists. Skipping graph construction...")

# Model training step
def train_model():
    if not os.path.exists(MODEL_PATH):
        run_script("src/model_training.py")
    else:
        print("ℹ️ Model already trained. Skipping training...")

# Exploratory Data Analysis (EDA)
def generate_eda_report():
    if not os.path.exists(EDA_REPORT_PATH):
        run_script("notebooks/EDA.ipynb")
    else:
        print("ℹ️ EDA report already exists. Skipping EDA...")

# API Deployment using FastAPI
def deploy_api():
    print("\n🚀 Starting API Server at http://127.0.0.1:8000/docs")
    subprocess.run(["uvicorn", "deployment.app:app", "--reload"])

# Command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fraud Detection Pipeline")
    parser.add_argument("--preprocess", action="store_true", help="Run data preprocessing")
    parser.add_argument("--graph", action="store_true", help="Construct transaction graph")
    parser.add_argument("--train", action="store_true", help="Train the fraud detection model")
    parser.add_argument("--eda", action="store_true", help="Generate EDA report")
    parser.add_argument("--deploy", action="store_true", help="Deploy the API")
    parser.add_argument("--all", action="store_true", help="Run the full pipeline")

    args = parser.parse_args()

    if args.preprocess:
        preprocess_data()

    if args.graph:
        construct_graph()

    if args.train:
        train_model()

    if args.eda:
        generate_eda_report()

    if args.deploy:
        deploy_api()

    if args.all:
        preprocess_data()
        construct_graph()
        train_model()
        generate_eda_report()
        deploy_api()

    print("🎉 Pipeline execution completed successfully!")