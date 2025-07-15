# train.py
# This script trains a model to detect SQL injection, reading data from the 'data' directory
# and saving the trained model artifacts to the 'model' directory.

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

print("Script started: Training model...")

# --- Define Paths ---
DATA_PATH = 'data/sqli_dataset.csv' 
MODEL_DIR = 'model'

# --- Create model directory if it doesn't exist ---
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)
    print(f"Created directory: {MODEL_DIR}")

# --- Download NLTK stopwords ---
try:
    stopwords.words('english')
except LookupError:
    print("Downloading NLTK stopwords...")
    nltk.download('stopwords')

# --- Data Loading ---
print(f"Loading dataset from {DATA_PATH}...")
try:
    # Let pandas automatically detect the header (header=0 is default)
    # Using engine='python' and on_bad_lines='skip' to handle potential CSV formatting errors.
    df = pd.read_csv(DATA_PATH, engine='python', on_bad_lines='skip')
    
    # Check if there are at least two columns
    if len(df.columns) < 2:
        print(f"Error: The CSV file must contain at least two columns. Found {len(df.columns)}.")
        exit()

    # Rename the first column to 'Sentence' and the second to 'Label'
    # This makes the script robust to different column names like 'Query' or 'sentence'.
    df.rename(columns={df.columns[0]: 'Sentence', df.columns[1]: 'Label'}, inplace=True)
    
    print(f"Dataset loaded successfully. Columns renamed to 'Sentence' and 'Label'.")
    
except FileNotFoundError:
    print(f"Error: Dataset file not found at {DATA_PATH}. Please ensure the file exists.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the CSV file: {e}")
    exit()

# --- Data Preprocessing ---
print("Preprocessing data...")

# 1. Drop rows with missing values in 'Sentence' or 'Label'
df.dropna(subset=['Sentence', 'Label'], inplace=True)

# 2. Convert 'Label' column to numeric, coercing errors to NaN (Not a Number)
df['Label'] = pd.to_numeric(df['Label'], errors='coerce')

# 3. Drop rows where 'Label' could not be converted to a number
df.dropna(subset=['Label'], inplace=True)

# 4. Define the text cleaning function
def clean_text(text):
    if not isinstance(text, str):
        text = str(text)
    # The 'count' parameter is deprecated and will be removed in a future version.
    # The re.sub function does not use a 'count' parameter in this way.
    # The flags re.I|re.A are also not standard for the 4th argument.
    # Correct usage is re.sub(pattern, repl, string, count=0, flags=0)
    text = re.sub(r'[^a-zA-Z\s]', '', text, flags=re.IGNORECASE)
    text = text.lower()
    text = text.strip()
    stop_words = set(stopwords.words('english'))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# 5. Apply the cleaning function to the 'Sentence' column
df['Sentence'] = df['Sentence'].apply(clean_text)
print("Data preprocessing complete.")

# --- Feature Extraction (TF-IDF) ---
# The DataFrame is now fully cleaned. We can create X and y.
print("Performing feature extraction with TF-IDF...")
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['Sentence'])
y = df['Label'].astype(int) # This is now safe to do
print("Feature extraction complete.")

# --- Data Splitting ---
print("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data splitting complete.")

# --- Model Training ---
print("Training Logistic Regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
print("Model training complete.")

# --- Model Evaluation ---
print("Evaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy on Test Set: {accuracy * 100:.2f}%")

# --- Saving the Model and Vectorizer ---
model_path = os.path.join(MODEL_DIR, 'model.pkl')
vectorizer_path = os.path.join(MODEL_DIR, 'vectorizer.pkl')

print(f"Saving model to {model_path}...")
joblib.dump(model, model_path)

print(f"Saving vectorizer to {vectorizer_path}...")
joblib.dump(vectorizer, vectorizer_path)

print("Model and vectorizer saved successfully.")
print("Script finished.")