from pymongo import MongoClient

client = MongoClient("mongodb+srv://ingredoai2:BXM6Hc1R57Hkiofy@cluster0.zimunh9.mongodb.net/")

db = client["ingredoai2"]
collection = db["products"]


def get_product(name):
    if not name:
        return None

    product = collection.find_one(
        {"product_name": {"$regex": name, "$options": "i"}},
        {
            "product_name": 1,
            "brands": 1,
            "ingredients_text": 1,
            "categories": 1
        }
    )

    if product:
        return {
            "product_name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "ingredients": product.get("ingredients_text", "Not available"),
            "categories": product.get("categories", "Not available")
        }

    return None