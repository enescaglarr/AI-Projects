#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv()
import os
from pathlib import Path
import pandas as pd
from src.helper import create_embeddings, create_index

# --- CONFIGURATION ---
ROOT = Path(__file__).parent
DATA_CSV = ROOT / 'Customer_Support_Training_Dataset' / 'Customer_Support_Training_Dataset.csv'
VECTOR_STORE_DIR = ROOT / 'vector_store'
INDEX_FILE = VECTOR_STORE_DIR / 'faiss_index.index'

def main():
    # 1. Get API Key from environment variable
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ Error: GEMINI_API_KEY environment variable is not set.")
        print("Run: export GEMINI_API_KEY='your_api_key_here' (on Mac/Linux)")
        print("Run: set GEMINI_API_KEY='your_api_key_here' (on Windows)")
        return

    # 2. Check for dataset
    if not DATA_CSV.exists():
        print(f"❌ Error: Dataset not found at {DATA_CSV}")
        return

    VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)

    # 3. Load Data
    print(f"📂 Loading dataset: {DATA_CSV}...")
    df = pd.read_csv(DATA_CSV)

    # 4. Create Gemini Embeddings
    # We pass the api_key here to match your updated helper.py
    print("🧠 Generating Gemini embeddings (this may take a minute)...")
    try:
        vectors = create_embeddings(df, column_name='instruction', api_key=api_key)
        
        # 5. Build and Save FAISS Index
        print(f"💾 Saving FAISS index to {INDEX_FILE}...")
        create_index(vectors, str(INDEX_FILE))
        
        print("✅ Success! Your vector database is now ready for Gemini.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == '__main__':
    main()