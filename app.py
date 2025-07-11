import os
from flask import Flask
from flasgger import Swagger, LazyJSONEncoder
from routes.dataset_routes import dataset_bp
from routes.home_routes import home_bp
from routes.quality_routes import quality_bp

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

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

# Register routes
app.register_blueprint(dataset_bp)
app.register_blueprint(home_bp)
app.register_blueprint(quality_bp)

# for development used this method-----------

# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

