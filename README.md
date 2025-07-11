# Dataset Catalog API

A lightweight backend API built using **Flask**, **MongoDB**, and **Flasgger**, to manage datasets and track quality logs.

---

## 🚀 Features

* RESTful API for managing datasets
* Soft deletion support
* Quality log tracking (PASS/FAIL)
* MongoDB with PyMongo
* Modular MVC structure (routes, services, models)
* CSV-based data seeding
* Auto-generated API docs with Swagger (Flasgger)

---

## 🧰 Tech Stack

* Python 3.10+
* Flask 2.x
* MongoDB
* PyMongo
* Marshmallow (for validation)
* Flasgger (Swagger docs)

---

## 📁 Folder Structure

```
.
├── app.py
├── routes/
├── services/
├── models/
├── utils/
├── seed.py
├── .env
│── dummy_test_data.csv   
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone <https://github.com/rajneeshkr96/datawise-backend>
cd dataset-backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # On mac use: 
source venv/bin/activate
```
### 3. Configure environment variables

Create a `.env` file in the root with:

```
MONGO_URI=mongodb://localhost:27017/
DB_NAME=user_database_name
```

Or edit `models/dataset_model.py` to set your URI directly.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```


### 5. Run the Flask app

```bash
python app.py
```

Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### 6. View API Docs

```http
GET http://127.0.0.1:5000/apidocs/
```

### 7.(optional) Seed the database with CSV data for testing

```bash
python seed.py
```

---

## 🧪 Example API Calls (using curl)

### Create a dataset

```bash
curl -X POST http://localhost:5000/datasets \
     -H "Content-Type: application/json" \
     -d '{"name": "Demo Dataset", "owner": "admin", "description": "Just testing", "tags": ["test"]}'
```

### List all datasets

```bash
curl http://localhost:5000/datasets
```
 and many endpoints check on /apidocs route.
---


