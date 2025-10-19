"""
Day 2: Data Exploration Script for ML

Goal:
- Read a CSV file (sample or dummy)
- Display head, shape, and column info
- Write clean reusable functions
"""

import pandas as pd

# Function to load dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("✅ Data Loaded Successfully!")
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        return None

# Function to explore dataset
def explore_data(df):
    print("\n🔹 First 5 rows of dataset:")
    print(df.head())

    print("\n🔹 Shape of dataset:")
    print(df.shape)

    print("\n🔹 Columns in dataset:")
    print(df.columns.tolist())

    print("\n🔹 Basic summary:")
    print(df.describe())

# Main driver
if __name__ == "__main__":
    # You can later replace this with real dataset e.g. "spam.csv"
    file_path = "sample_data.csv"  # Keep a dummy file or update later
    df = load_data(file_path)
    
    if df is not None:
        explore_data(df)
