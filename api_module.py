import requests

def get_product_from_api(product_name):

    url = "https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": product_name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }

    response = requests.get(url, params=params)

    data = response.json()

    if data["products"]:

        product = data["products"][0]

        return {
            "product_name": product.get("product_name"),
            "brands": product.get("brands"),
            "ingredients_text": product.get("ingredients_text"),
            "categories": product.get("categories")
        }

    return None