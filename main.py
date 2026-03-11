import streamlit as st
from PIL import Image
import tempfile

from ocr_module import extract_text
from database import get_product
from api_module import get_product_from_api


st.title("AI OCR Product Scanner")

uploaded_file = st.file_uploader(
    "Upload Product Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")
    st.image(image, width="stretch")

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    image.save(temp_file.name)
    temp_file.close()

    text = extract_text(temp_file.name)

    st.subheader("Extracted Text")

    if not text or len(text.strip()) == 0:
        st.error("No text detected from image")
        st.stop()

    st.write(text)

    words = text.lower().split()
    search_candidates = sorted(words, key=len, reverse=True)[:5]

    st.subheader("Detected Keywords")
    st.write(search_candidates)

    product = None
    search_word = None

    for word in search_candidates:
        product = get_product(word)
        if product:
            search_word = word
            break

    if not product:
        st.info("Product not found in MongoDB. Searching Open Food Facts API...")
        for word in search_candidates:
            product = get_product_from_api(word)
            if product:
                search_word = word
                break

    if product:
        st.success("Product Found")

        st.subheader("Matched Keyword")
        st.write(search_word)

        st.subheader("Product Details")
        st.write("Product Name:", product.get("product_name"))
        st.write("Brand:", product.get("brand"))
        st.write("Ingredients:", product.get("ingredients"))
        st.write("Categories:", product.get("categories"))

        if product.get("nutrition"):
            st.subheader("Nutrition Info")
            nutrition = product["nutrition"]
            st.write("Energy:", nutrition.get("energy"))
            st.write("Fat:", nutrition.get("fat"))
            st.write("Sugars:", nutrition.get("sugars"))

    else:
        st.warning("Product not found in MongoDB or API")