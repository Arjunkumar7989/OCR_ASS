# OCR-Based Product Information Scanner

## Project Overview

The **OCR-Based Product Information Scanner** is an AI-powered application that extracts text from product label images and retrieves corresponding product information automatically.

The system uses **Tesseract OCR** to detect text from product packaging and then searches a **MongoDB database** to identify the product. If the product is not found in the database, the system can optionally query the **Open Food Facts API** to fetch product details.

The results are displayed through a **Streamlit web interface**, providing a simple and interactive way to scan product labels and view product information.

---

# System Architecture / Workflow

```
Product Image Upload
        ↓
OCR Text Extraction (Tesseract)
        ↓
Image Preprocessing (OpenCV)
        ↓
Keyword Detection from Extracted Text
        ↓
MongoDB Database Search
        ↓
API Fallback (OpenFoodFacts) if product not found
        ↓
Display Product Information (Streamlit UI)
```

---

# Features

• OCR-based product label scanning
• Image preprocessing for improved OCR accuracy
• Automatic product keyword detection
• Product information retrieval from MongoDB
• Optional Open Food Facts API integration
• Interactive Streamlit web interface
• Error handling for invalid images and missing products

---

# Tech Stack

**Programming Language**

• Python

**Libraries & Tools**

• Tesseract OCR
• OpenCV
• PyTesseract
• Streamlit
• PyMongo
• Requests
• Pillow

**Database**

• MongoDB Atlas

---

# Project Structure

```
OCR_ASS/
│
├── main.py            # Streamlit application (UI and pipeline)
├── database.py        # MongoDB connection and product retrieval
├── ocr_module.py      # OCR preprocessing and text extraction
├── api_module.py      # Open Food Facts API integration
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

# Installation & Setup

## 1. Clone the Repository

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

Download and install **Tesseract OCR** from:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the Tesseract path in **ocr_module.py** if required:

```
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

# MongoDB Configuration

Create a MongoDB Atlas cluster and update the connection string in **database.py**.

Example:

```
mongodb+srv://<username>:<password>@cluster.mongodb.net/
```

Database Used:

```
ingredoai2
```

Collection Used:

```
products
```

The system searches for products using the keyword extracted from OCR text.

---

# Running the Application

Start the Streamlit application:

```
streamlit run main.py
```

Open the application in your browser:

```
http://localhost:8501
```

---

# How the System Works

1. The user uploads a product label image using the Streamlit interface.
2. The OCR module processes the image and extracts text from the label.
3. The system identifies a keyword from the extracted text.
4. The keyword is used to search the MongoDB database.
5. If a matching product is found, the system displays product details including:

• Product Name
• Brand
• Ingredients
• Categories
• Nutrition Information (if available)

6. If the product is not found in MongoDB, the system optionally queries the **Open Food Facts API**.

---

# Example Output

```
Product Name: Coca-Cola Classic
Brand: Coca-Cola
Ingredients: Carbonated water, high fructose corn syrup, caramel color, phosphoric acid.
Categories: Beverages, Carbonated drinks, Sodas
Energy: 42 kcal
Sugars: 10.6 g
```

---

# Error Handling

The application handles the following cases:

• No text detected in the image
• Invalid or unsupported image uploads
• Product not found in the database
• API request failures

---

# Future Improvements

• Barcode detection for faster product recognition
• Fuzzy matching for improved product identification
• Multi-language OCR support
• Ingredient risk detection (e.g., high sugar, palm oil)
• Mobile camera integration

---

# Conclusion

This project demonstrates how **Optical Character Recognition (OCR)** can be combined with **database systems and web interfaces** to build an automated product recognition system.

The architecture is modular and scalable, making it suitable for further extensions such as **barcode scanning, ingredient analysis, and real-time product recognition systems**.
