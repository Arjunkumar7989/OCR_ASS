import streamlit as st
from PIL import Image
import tempfile

from ocr_module import extract_text
from database import get_product

st.title("OCR Product Scanner")

uploaded_file = st.file_uploader(
    "Upload Product Image", type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Save temp image
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    image.save(temp_file.name)
    temp_file.close()

    # OCR
    text = extract_text(temp_file.name)

    st.subheader("Extracted Text")
    st.write(text)

    # ---- SEARCH WORD LOGIC ----
    search_word = None

    if text and len(text.strip()) > 0:
        words = text.lower().split()
        search_word = words[0]

    # OCR fail ayina MongoDB search try cheyyadaniki fallback
    if not search_word:
        search_word = "coca"

    # ---- MongoDB FETCH ----
    product = get_product(search_word)

    if product:

        st.subheader("Product Details")

        st.write("Product Name:", product.get("product_name"))
        st.write("Brand:", product.get("brands"))
        st.write("Ingredients:", product.get("ingredients_text"))
        st.write("Categories:", product.get("categories"))

    else:
        st.warning("Product not found in MongoDB")