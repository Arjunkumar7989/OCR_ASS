from pymongo import MongoClient

client = MongoClient("mongodb+srv://ingredoai2:BXM6Hc1R57Hkiofy@cluster0.zimunh9.mongodb.net/")

db = client["ingredoai2"]

collection = db["products"]

def get_product(name):

    product = collection.find_one({
        "product_name": {"$regex": name, "$options": "i"}
    })

    if product:
        return {
            "product_name": product.get("product_name"),
            "brands": product.get("brands"),
            "ingredients_text": product.get("ingredients_text"),
            "categories": product.get("categories")
        }

    return None