import os
import cv2
import pytesseract

def clean_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply thresholding to remove noise
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Apply morphology to remove small black spots
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    clean = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    return clean

def extract_text(image_path, output_file):
    # Load image
    image = cv2.imread(image_path)
    # Clean image
    cleaned = clean_image(image)
    # Extract text using Tesseract
    text = pytesseract.image_to_string(cleaned, lang='chi_sim')
    # Save text to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

def main():
    # Path to directory containing images
    images_dir = '/path/to/images'
    # Path to directory where output files will be saved
    output_dir = '/path/to/output'
    # Get list of image files in directory
    image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg') or f.endswith('.png')]
    # Process each image file
    for i, image_file in enumerate(image_files):
        # Construct paths for image and output file
        image_path = os.path.join(images_dir, image_file)
        output_file = os.path.join(output_dir, f'text{i+1}.txt')
        # Extract text from image and save to file
        extract_text(image_path, output_file)
        print(f'Extracted text from {image_file} and saved to {output_file}')

if __name__ == '__main__':
    main()
