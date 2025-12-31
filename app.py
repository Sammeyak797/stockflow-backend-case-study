from flask import Flask
from database import db
from routes.products import products_bp
from routes.inventory import inventory_bp



def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stockflow.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


app = create_app()
app.register_blueprint(products_bp)
app.register_blueprint(inventory_bp)


if __name__ == "__main__":
    app.run(debug=True)
