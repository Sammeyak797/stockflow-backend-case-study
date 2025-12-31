# StockFlow – Backend Inventory Management System

This project is a backend inventory management system built as part of the **Backend Engineering Intern case study for Bynry Inc.**

It simulates a real-world SaaS-style inventory platform used to manage products, warehouses, and stock movements while ensuring data consistency, auditability, and scalability.

---

## 🚀 Tech Stack

- **Python**
- **Flask**
- **SQLAlchemy**
- **SQLite (for simplicity, easily replaceable with PostgreSQL/MySQL)**
- **Pydantic (for request validation)**

---

## 📦 Core Features

### 1️⃣ Product Management
- Create products with SKU, price, and configurable low-stock threshold.
- Ensures SKU uniqueness.

### 2️⃣ Inventory Management
- Add stock (IN movement)
- Remove stock (OUT movement with validation)
- Prevents negative inventory

### 3️⃣ Inventory Movement Audit Trail
- Every stock change is recorded as a movement
- Supports traceability and historical analysis

### 4️⃣ Low Stock Alerts
- API to fetch products below their defined stock threshold
- Useful for proactive restocking and monitoring

---

## 🧠 Design Decisions

- **Separation of concerns**: Routes, models, schemas, and database logic are cleanly separated.
- **Auditability**: Inventory movements are tracked instead of directly mutating stock blindly.
- **Scalability-first thinking**: Designed in a way that can be extended to multi-tenant SaaS systems.
- **Validation-first APIs**: Pydantic schemas ensure clean and predictable request handling.

---

## 🔗 API Endpoints

### ➕ Create Product
`POST /products`

```json
{
  "name": "Laptop",
  "sku": "LAP-001",
  "price": 75000,
  "low_stock_threshold": 5
}
