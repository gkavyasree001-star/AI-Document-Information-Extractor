import pytesseract
from PIL import Image
import re

# TELL PYTHON WHERE TESSERACT IS INSTALLED:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_document_info(image_name):
    try:
        # 1. Open the document image
        img = Image.open(image_name)
        
        # 2. Read the text from the image (OCR)
        extracted_text = pytesseract.image_to_string(img)
        
        print("--- 📄 Raw Extracted Text From Document ---")
        print(extracted_text)
        print("------------------------------------------")
        
        # 3. Look for email structures inside the text
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', extracted_text)
        
        print("\n--- 🔍 Extracted Structured Data ---")
        if emails:
            print(f"Emails Found: {emails}")
        else:
            print("Emails Found: None detected in this image.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Tell the code to run using our document image
extract_document_info("doc.png")
