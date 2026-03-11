import requests


def get_product_from_api(product_name):

    url = "https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": product_name,
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "page_size": 1
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()

    except requests.exceptions.RequestException:
        return None

    products = data.get("products")

    if not products:
        return None

    product = products[0]

    nutriments = product.get("nutriments", {})

    return {
        "product_name": product.get("product_name", "Unknown"),
        "brand": product.get("brands", "Unknown"),
        "ingredients": product.get("ingredients_text", "Not available"),
        "categories": product.get("categories", "Not available"),
        "nutrition": {
            "energy": nutriments.get("energy", "Not available"),
            "fat": nutriments.get("fat", "Not available"),
            "sugars": nutriments.get("sugars", "Not available")
        }
    }