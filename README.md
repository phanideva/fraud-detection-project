# Project Overview:<br>
This Project is an AI-powered fraud detection system that leverages Graph Neural Networks (GNNs) to detect fraudulent financial transactions based on relationships between users.<br>
Instead of analyzing transactions individually, the project treats them as a graph, where:<br>
  Nodes represents users (senders/receivers).<br>
  Edges represent financial transactions between users.<br>
  Edge weights represent the transaction amount.<br>

Why use Graph Neural Networks (GNNs) for Fraud Detection?<br>
Fraud detection requires analyizing complex relationships between entities (eg., bank accounts).<br>
Traditional machine learning methods struggle to capture these relationships, but GNNs can:<br>
  Identify fraudulent patterns based on connections.<br>
  Detect suspicious transaction flows in a network.<br>
  Handle dynamic transaction patterns.<br>

# 🏁 Installation & Setup
<details>
  <summary><strong>1️⃣ Clone the Repository</strong></summary>
  
```bash
git clone https://github.com/phanideva/fraud-detection-gnn.git
cd fraud-detection-gnn
```

</details> <details> <summary><strong>2️⃣ Set Up Virtual Environment</strong></summary>
  
```bash
python -m venv venv
```

Activate the virtual environment:
    Windows:
    ```bash
    venv\Scripts\activate
    ```
    macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
</details> <details> <summary><strong>3️⃣ Install Dependencies</strong></summary>
  
```bash
pip install -r requirements.txt
```

</details> <details> <summary><strong>4️⃣ Preprocess Data</strong></summary>
  
```bash
python src/data_preprocessing.py
```

</details> <details> <summary><strong>5️⃣ Build Graph from Transactions</strong></summary>
  
```bash
python src/graph_construction.py
```

</details> <details> <summary><strong>6️⃣ Train the Model</strong></summary>
  
```bash
python src/model_training.py
```

</details> <details> <summary><strong>7️⃣ Run the API Server</strong></summary>
  
```bash
uvicorn deployment.app:app --reload
```

Once running, open:
    http://127.0.0.1:8000/docs - Swagger UI
    http://127.0.0.1:8000/redoc - Redoc UI
</details>

# ⚙️ Deployment (Dockerized)
To build and run the project using Docker:
```bash
docker build -t fraud-detection .
docker run -p 8000:8000 fraud-detection
```

🧪 Running Tests
To run unit tests:
```bash
pytest tests/
```

# 🚀 CI/CD Pipeline (GitHub Actions)
This project includes a CI/CD pipeline to automate the following:<br>  
✅ Running tests<br>  
✅ Building the Docker container<br>  
✅ Deploying the API<br>  

## 🛠️ Pipeline configuration:<br>  
The CI/CD setup can be found in the file:<br>  
📂 `.github/workflows/ci-cd-pipeline.yml`

## 📈 Example API Request
Request (POST /predict/)
```json
[[0.5, 0.2, 0.1, 0.9, 0.3, 0.7, 0.4, 0.6, 0.5, 0.8, 0.2, 0.4, 0.1, 0.9, 0.3, 0.7]]
```
Response
```json
{"prediction": 1}
```

# 📚 Resources
PyTorch Geometric<br>
FastAPI Documentation<br>
Docker Documentation<br>

# 👨‍💻 Author
Phaneendra Devabhakthuni<br>
GitHub: @phanideva<br>
LinkedIn: Phaneendra Devabhakthuni<br>
Email: phanisaisri@gmail.com<br>
