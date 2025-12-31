# Part 1 – Code Review & Debugging

Below are the identified issues in the provided product creation API, along with their impact and suggested fixes.

---

## Issue 1: No input validation

**Problem:**  
The API directly accesses request fields without validating their presence or type.

**Impact:**  
This can cause runtime errors (KeyError) and return 500 responses to clients.

**Fix:**  
Validate all required fields and return proper 400 responses with clear messages.

---

## Issue 2: SKU uniqueness not enforced

**Problem:**  
SKU uniqueness is not checked before inserting a new product.

**Impact:**  
Duplicate SKUs can break inventory tracking and reporting.

**Fix:**  
Enforce unique constraint at DB level and check before insert.

---
