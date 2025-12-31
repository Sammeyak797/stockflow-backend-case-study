from flask import Blueprint, request, jsonify
from database import db
from models import Inventory, InventoryMovement, Product
from schemas import InventoryUpdate

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/inventory/add", methods=["POST"])
def add_stock():
    data = InventoryUpdate(**request.json)

    inventory = Inventory.query.filter_by(
        product_id=data.product_id,
        warehouse_id=data.warehouse_id
    ).first()

    if inventory:
        inventory.quantity += data.quantity
    else:
        inventory = Inventory(
            product_id=data.product_id,
            warehouse_id=data.warehouse_id,
            quantity=data.quantity
        )
        db.session.add(inventory)

    movement = InventoryMovement(
        product_id=data.product_id,
        warehouse_id=data.warehouse_id,
        quantity=data.quantity,
        movement_type="IN"
    )

    db.session.add(movement)
    db.session.commit()

    return jsonify({"message": "Stock added successfully"})

@inventory_bp.route("/inventory/remove", methods=["POST"])
def remove_stock():
    data = InventoryUpdate(**request.json)

    inventory = Inventory.query.filter_by(
        product_id=data.product_id,
        warehouse_id=data.warehouse_id
    ).first()

    if not inventory or inventory.quantity < data.quantity:
        return jsonify({"error": "Insufficient stock"}), 400

    inventory.quantity -= data.quantity

    movement = InventoryMovement(
        product_id=data.product_id,
        warehouse_id=data.warehouse_id,
        quantity=data.quantity,
        movement_type="OUT"
    )

    db.session.add(movement)
    db.session.commit()

    return jsonify({"message": "Stock removed successfully"})

@inventory_bp.route("/inventory/low-stock", methods=["GET"])
def low_stock():
    results = (
        db.session.query(Product.name, Inventory.quantity, Product.low_stock_threshold)
        .join(Inventory, Inventory.product_id == Product.id)
        .filter(Inventory.quantity < Product.low_stock_threshold)
        .all()
    )

    response = [
        {
            "product": r[0],
            "quantity": r[1],
            "threshold": r[2]
        }
        for r in results
    ]

    return jsonify(response)
