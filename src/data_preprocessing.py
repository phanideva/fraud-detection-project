import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df.dropna(inplace=True)
    
    # Encode categorical features
    label_encoder = LabelEncoder()
    df['Category'] = label_encoder.fit_transform(df['Category'])
    
    # Normalize transaction amount using log transformation
    df['Amount'] = np.log1p(df['Amount'])
    
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    load_and_preprocess_data('data/raw_transactions.csv', 'data/processed_data.csv')