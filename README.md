# OCR-Based Product Information Scanner

## Project Overview

This project implements an **OCR-Based Product Information Scanner** that reads text from a product label image and retrieves corresponding product information from a **MongoDB database**.

The system uses **Tesseract OCR** to extract text from the image and then searches the MongoDB database to find the matching product details. The results are displayed using a **Streamlit web interface**.

---

# Workflow / System Architecture

Product Image
↓
OCR extracts text from the label
↓
Extract product keyword (e.g., coca, pepsi)
↓
Query MongoDB database
↓
Fetch product details
↓
Display results in Streamlit interface

---

# Tech Stack

* Python
* Tesseract OCR
* Streamlit
* MongoDB
* PyMongo
* OpenCV
* Pillow
* Requests

---

# Project Structure

```
OCR_ASS/
│
├── main.py           # Streamlit web interface
├── database.py       # MongoDB connection and data retrieval
├── ocr_module.py     # OCR text extraction using Tesseract
├── api_module.py     # Optional API integration
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

---

# MongoDB Configuration

The project connects to the MongoDB cluster using the following connection string:

```
mongodb+srv://ingredoai2:BXM6Hc1R57Hkiofy@cluster0.zimunh9.mongodb.net/
```

Database Used:

```
ingredoai2
```

Collection Used:

```
products
```

The application searches for products using the extracted OCR text.

---

# Installation & Setup

## 1. Clone or Download the Project

```
git clone <repository-url>
cd OCR_ASS
```

---

## 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## 3. Install Tesseract OCR

Download and install Tesseract from:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the path in `ocr_module.py` if required:

```
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

# Running the Application

Start the Streamlit application:

```
streamlit run main.py
```

Then open the application in your browser:

```
http://localhost:8501
```

---

# How the System Works

1. The user uploads a product image through the Streamlit interface.
2. The OCR module extracts text from the image.
3. A keyword from the extracted text is used to search the MongoDB database.
4. If a matching product is found, the following details are displayed:

* Product Name
* Brand
* Ingredients
* Product Categories
* Nutrition Information (if available)

---

# Example Output

```
Product Name: Coca-Cola Classic
Brand: Coca-Cola
Ingredients: Carbonated water, high fructose corn syrup, caramel color, phosphoric acid.
Categories: Beverages, Carbonated drinks, Sodas
```

---

# Error Handling

The system handles the following cases:

* No text detected in the image
* Product not found in the database
* Invalid image uploads

---

# Future Improvements

* Barcode detection
* Integration with Open Food Facts API
* Improved OCR preprocessing
* Support for multiple product recognition

---

# Conclusion

This project demonstrates how **Optical Character Recognition (OCR)** can be combined with **MongoDB and a web interface** to build an automated product information retrieval system. The system provides a simple yet scalable approach for recognizing products from images and retrieving structured product data.
