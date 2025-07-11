import csv
from datetime import datetime
from models.dataset_model import datasets

def seed_datasets_from_csv():
    print("📥 Seeding datasets from CSV...")

    # Clear datasets collection
    datasets.delete_many({})

    dataset_docs = []

    # Load and prepare documents
    with open('dummy_test_data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dataset_docs.append({
                "name": row["name"],
                "owner": row["owner"],
                "description": row["description"],
                "tags": [tag.strip() for tag in row["tags"].split(",")],
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
                "is_deleted": False
            })

    # Insert all datasets
    result = datasets.insert_many(dataset_docs)
    print(f"✅ Inserted {len(result.inserted_ids)} datasets successfully.")

if __name__ == '__main__':
    seed_datasets_from_csv()
