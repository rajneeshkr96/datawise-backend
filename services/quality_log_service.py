from models.dataset_model import quality_logs
from bson.objectid import ObjectId
from datetime import datetime

def add_quality_log(dataset_id, data):
    data.update({
        "dataset_id": ObjectId(dataset_id),
        "timestamp": datetime.utcnow()
    })
    return str(quality_logs.insert_one(data).inserted_id)

def get_quality_logs(dataset_id):
    return list(quality_logs.find({"dataset_id": ObjectId(dataset_id)}))
