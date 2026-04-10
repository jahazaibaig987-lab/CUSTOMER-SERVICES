import os

folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "models"
]

files = [
    "notebooks/EDA.ipynb",
    "src/data_ingestion.py",
    "src/data_preprocessing.py",
    "src/model_training.py",
    "src/evaluation.py",
    "app.py",
    "requirements.txt",
    "README.md"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, "w") as f:
        pass

print("✅ Project structure created successfully!")