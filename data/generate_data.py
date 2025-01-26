from faker import Faker
import pandas as pd
import random

fake = Faker()

# Generate unique numeric IDs for senders and receivers
senders = [fake.random_int(min=10000, max=99999) for _ in range(500)]
receivers = [fake.random_int(min=10000, max=99999) for _ in range(500)]

data = {
    "Sender": [random.choice(senders) for _ in range(1000)],
    "Receiver": [random.choice(receivers) for _ in range(1000)],
    "Amount": [fake.random_int(min=10, max=5000) for _ in range(1000)],
    "Category": [fake.random_element(["Groceries", "Electronics", "Entertainment", "Bills", "Travel"]) for _ in range(1000)],
    "Transaction_Date": [fake.date_between(start_date="-2y", end_date="today").strftime("%Y-%m-%d") for _ in range(1000)],
    "Fraudulent": [random.choices([0, 1], weights=[95, 5])[0] for _ in range(1000)]
}

df = pd.DataFrame(data)
df.to_csv("data/raw_transactions.csv", index=False)
print("Synthetic data with numeric sender/receiver IDs generated.")