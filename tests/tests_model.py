import torch
from src.model_training import FraudGNN

def test_model_output_shape():
    model = FraudGNN(input_dim=16, hidden_dim=32, output_dim=2)
    test_input = torch.randn(10, 16)
    output = model.forward(test_input)
    assert output.shape == (10, 2)

def test_prediction_range():
    model = FraudGNN(input_dim=16, hidden_dim=32, output_dim=2)
    test_input = torch.randn(1, 16)
    output = model.forward(test_input)
    assert output.argmax(dim=1).item() in [0, 1]