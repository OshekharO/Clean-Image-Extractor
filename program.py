import os
import cv2
import pytesseract

def clean_image(image):
    """
    Clean the image by converting to grayscale, applying thresholding, and morphology.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    clean = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    return clean

def extract_text(image_path, output_file):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Unable to read image {image_path}")
            return
        cleaned = clean_image(image)
        text = pytesseract.image_to_string(cleaned, lang='chi_sim')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as e:
        print(f"Error: {e}")

def main():
    images_dir = '/path/to/images'
    output_dir = '/path/to/output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg') or f.endswith('.png')]
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(images_dir, image_file)
        output_file = os.path.join(output_dir, f'text{i+1}.txt')
        extract_text(image_path, output_file)
        print(f'Extracted text from {image_file} and saved to {output_file}')

if __name__ == '__main__':
    main()
