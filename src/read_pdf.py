import sys
import os
import pytesseract
from pdf2image import convert_from_path

def extract_text(pdf_path, output_path):
    try:
        # Try to find tesseract
        tesseract_paths = [
            r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        ]
        for p in tesseract_paths:
            if os.path.exists(p):
                pytesseract.pytesseract.tesseract_cmd = p
                break
                
        # convert pdf to images
        print("Converting PDF to images...")
        
        # In a new process, the PATH might not have poppler yet due to winget just installing it.
        # Let's search for poppler in localappdata winget packages
        local_app_data = os.environ.get('LOCALAPPDATA', '')
        poppler_path = None
        if local_app_data:
            winget_pkgs = os.path.join(local_app_data, 'Microsoft', 'WinGet', 'Packages')
            if os.path.exists(winget_pkgs):
                for d in os.listdir(winget_pkgs):
                    if 'Poppler' in d:
                        # find Library/bin or bin inside it
                        for root, dirs, files in os.walk(os.path.join(winget_pkgs, d)):
                            if 'pdftocairo.exe' in files or 'pdftoppm.exe' in files:
                                poppler_path = root
                                break
        
        images = convert_from_path(pdf_path, poppler_path=poppler_path)
        
        print("Running OCR on images...")
        text = ""
        for i, img in enumerate(images):
            text += f"--- Page {i+1} ---\n"
            text += pytesseract.image_to_string(img) + "\n"
            
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print("Success")
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        extract_text(sys.argv[1], sys.argv[2])
    else:
        print("Please provide a PDF path and output path.")
