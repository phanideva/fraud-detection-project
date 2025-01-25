from fastapi import FastAPI
import torch
from src.model_training import FraudGNN

app = FastAPI()
model = FraudGNN(input_dim=16, hidden_dim=32, output_dim=2)
model.load_state_dict(torch.load("models/gnn_model.pth"))
model.eval()

@app.get("/")
def home():
    return {"message": "Fraud Detection API"}

@app.post("/predict/")
def predict(features: list):
    input_tensor = torch.tensor(features).float()
    output = model(input_tensor)
    return {"prediction": output.argmax(dim=1).item()}