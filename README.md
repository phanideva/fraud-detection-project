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
⚙️ Deployment (Dockerized)
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

🚀 CI/CD Pipeline (GitHub Actions)
This project includes a CI/CD pipeline to automate:
    1. Running tests
    2. Building the Docker container
    3. Deploying the API
Pipeline configuration can be found in .github/workflows/ci-cd-pipeline.yml.

📈 Example API Request
Request (POST /predict/)
```json
[[0.5, 0.2, 0.1, 0.9, 0.3, 0.7, 0.4, 0.6, 0.5, 0.8, 0.2, 0.4, 0.1, 0.9, 0.3, 0.7]]
```
Response
```json
{"prediction": 1}
```

📚 Resources
PyTorch Geometric
FastAPI Documentation
Docker Documentation

👨‍💻 Author
Phaneendra Devabhakthuni
GitHub: @phanideva
LinkedIn: Phaneendra Devabhakthuni
Email: phanisaisri@gmail.com
