🏁 Installation & Setup
1. Clone the Repository
```bash
git clone https://github.com/phanideva/fraud-detection-gnn.git
cd fraud-detection-gnn
```
2. Set Up Virtual Environment
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
3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Preprocess Data
```bash
python src/data_preprocessing.py
```

5. Build Graph from Transactions
```bash
python src/graph_construction.py
```

6. Train the Model
```bash
python src/model_training.py
```

7. Run the API Server
```bash
uvicorn deployment.app:app --reload
```

Once running, open:
    http://127.0.0.1:8000/docs - Swagger UI
    http://127.0.0.1:8000/redoc - Redoc UI

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