from models.dataset_model import datasets
from bson.objectid import ObjectId
from datetime import datetime

def create_dataset(data):
    data.update({
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "is_deleted": False
    })
    return str(datasets.insert_one(data).inserted_id)

def list_datasets(owner=None, tag=None):
    query = {"is_deleted": False}
    if owner:
        query["owner"] = owner
    if tag:
        query["tags"] = tag
    return list(datasets.find(query))

def get_dataset(dataset_id):
    return datasets.find_one({"_id": ObjectId(dataset_id), "is_deleted": False})

def update_dataset(dataset_id, data):
    data["updated_at"] = datetime.utcnow()
    return datasets.update_one({"_id": ObjectId(dataset_id)}, {"$set": data}).modified_count > 0

def soft_delete_dataset(dataset_id):
    return datasets.update_one({"_id": ObjectId(dataset_id)}, {"$set": {"is_deleted": True}}).modified_count > 0
