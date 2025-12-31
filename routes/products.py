from flask import Blueprint, request, jsonify
from database import db
from models import Product
from schemas import ProductCreate

products_bp = Blueprint("products", __name__)

@products_bp.route("/products", methods=["POST"])
def create_product():
    data = ProductCreate(**request.json)

    product = Product(
        name=data.name,
        sku=data.sku,
        price=data.price,
        low_stock_threshold=data.low_stock_threshold
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message": "Product created successfully",
        "product_id": product.id
    }), 201
