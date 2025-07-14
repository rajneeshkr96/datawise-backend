import os
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger, LazyJSONEncoder
from dotenv import load_dotenv

from routes.dataset_routes import dataset_bp
from routes.home_routes import home_bp
from routes.quality_routes import quality_bp

load_dotenv()

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

cors_origins = os.getenv("CORS_ORIGINS", "*")

if cors_origins.strip() == "*":
    CORS(app)  
else:
    allowed_origins = [origin.strip() for origin in cors_origins.split(",") if origin.strip()]
    CORS(app, resources={r"/*": {"origins": allowed_origins}})


template = {
    "swagger": "2.0",
    "info": {
        "title": "Dataset API",
        "description": "API for managing datasets and quality logs",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http"]
}
Swagger(app, template=template)

app.register_blueprint(dataset_bp)
app.register_blueprint(home_bp)
app.register_blueprint(quality_bp)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',, port=port, debug=True)
