import torch
from model_training import FraudGNN

def load_model(model_path):
    model = FraudGNN(input_dim=16, hidden_dim=32, output_dim=2)
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def predict(features):
    model = load_model("models/gnn_model.pth")
    input_tensor = torch.tensor(features).float()
    output = model(input_tensor)
    return output.argmax(dim=1).item()

if __name__ == "__main__":
    sample_features = torch.randn(1, 16).tolist()
    prediction = predict(sample_features)
    print(f"Predicted Fraud Status: {prediction}")