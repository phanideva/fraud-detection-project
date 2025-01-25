import os
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data

class FraudGNN(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(FraudGNN, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, output_dim)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = F.dropout(x, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

def train_model(graph_data):
    model = FraudGNN(input_dim=16, hidden_dim=32, output_dim=2)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    criterion = torch.nn.CrossEntropyLoss()

    # Dummy target labels for training
    graph_data.y = torch.randint(0, 2, (graph_data.x.shape[0],))

    for epoch in range(50):
        model.train()
        optimizer.zero_grad()
        out = model(graph_data)
        loss = criterion(out, graph_data.y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

    # Ensure the 'models' directory exists
    model_dir = "models"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    torch.save(model.state_dict(), os.path.join(model_dir, "gnn_model.pth"))
    print("Model saved to models/gnn_model.pth")

if __name__ == "__main__":
    # Load the graph data normally
    graph_data = torch.load("data/graph_data.pt")
    train_model(graph_data)