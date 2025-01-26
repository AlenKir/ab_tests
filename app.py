from flask import Flask
from flask_pymongo import PyMongo
from config.config import Config
from routes.routes import ab_routes

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

app.register_blueprint(ab_routes)

if __name__ == '__main__':
    app.run(debug=True)
