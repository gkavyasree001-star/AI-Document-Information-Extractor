# AI Document Information Extractor (OCR)

An automated Document Intelligence pipeline built with Python, Tesseract OCR, and Pillow. This project demonstrates how to ingest unstructured document images—such as receipts, digital forms, and invoices—convert their visual layouts into raw machine-readable text, and programmatically extract specific metadata using advanced pattern matching.

---

## 🚀 Key Features

* **Optical Character Recognition (OCR):** Translates pixel-based text inside images into dynamic, editable Python strings using the Tesseract engine.
* **Regex-Driven Data Extraction:** Utilizes optimized Regular Expressions (`re`) to scan the raw text blocks and instantly isolate critical contact arrays (emails).
* **Fault-Tolerant Processing:** Implements explicit error handling (`try-except`) to safely manage execution exceptions and missing local dependencies without crashing production pipelines.

---

## 🛠️ Technical Stack & Concepts Demonstrated

* **Language:** Python
* **Libraries:** `pytesseract`, `Pillow` (PIL), `re` (Regular Expressions)
* **Engineering Concepts:** Optical character recognition, regular expression parsing, file I/O operations, structural exception handling, and pattern matching.

---

## 📋 How It Works

1. **Image Ingestion:** Pillow reads the document image file format and handles memory management for the pixel array.
2. **Text Synthesis (OCR):** The image matrix is passed to the Tesseract OCR engine, which detects individual text baselines and converts optical shapes into characters.
3. **Metadata Scrubbing:** The extracted text stream is filtered through a compilation pattern to catch matching structural email patterns.
4. **Output Compilation:** Prints out both the full raw layout representation and a clean, isolated array of extracted target data.

---

## 🖥️ Sample Execution Output

```text
--- 📄 Raw Extracted Text From Document ---
Invoice Number: INV-2026-001
Date: August 12, 2026
Company: AI Solutions Ltd.

Contact Email: gkavya@gmail.com
Support: contact@aisolutions.com

Total Amount Due: $450.00
Status: Paid
------------------------------------------

--- 🔍 Extracted Structured Data ---
Emails Found: ['gkavya@gmail.com', 'contact@aisolutions.com']
