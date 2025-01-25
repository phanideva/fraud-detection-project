import torch
import networkx as nx
import pandas as pd
from torch_geometric.data import Data

def create_graph_from_csv(file_path):
    # Load the processed CSV file
    df = pd.read_csv(file_path)

    # Create a unique mapping of entities (senders and receivers) to numeric IDs
    unique_entities = list(set(df["Sender"].tolist() + df["Receiver"].tolist()))
    entity_to_id = {entity: idx for idx, entity in enumerate(unique_entities)}

    # Map sender and receiver to numeric IDs
    df["Sender_ID"] = df["Sender"].map(entity_to_id)
    df["Receiver_ID"] = df["Receiver"].map(entity_to_id)

    # Create the graph using NetworkX
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['Sender_ID'], row['Receiver_ID'], amount=row['Amount'])

    # Create edge_index and edge_attr for PyTorch Geometric
    edge_index = torch.tensor(list(G.edges)).t().contiguous()
    edge_attr = torch.tensor([d['amount'] for _, _, d in G.edges(data=True)], dtype=torch.float)

    # Create node features (randomized here, replace with meaningful features if available)
    num_nodes = len(unique_entities)  # Total number of nodes
    node_features = torch.randn((num_nodes, 16))  # 16-dimensional node features

    # Create the PyTorch Geometric Data object
    graph_data = Data(x=node_features, edge_index=edge_index, edge_attr=edge_attr)
    return graph_data

if __name__ == "__main__":
    graph_data = create_graph_from_csv("data/processed_data.csv")
    torch.save(graph_data, "data/graph_data.pt")
    print("Graph data saved to data/graph_data.pt")