# clean img ext
Python program that uses the OpenCV library to clean bulk images, and then uses the Tesseract OCR library to extract text from the cleaned images

### Special Note:

Make sure you have installed Tesseract OCR engine before installing pytesseract. You can download and install the Tesseract OCR engine from this link: https://github.com/tesseract-ocr/tesseract/wiki

### Here's a brief explanation of how it works:

The clean_image function takes an image as input and applies a series of OpenCV image processing techniques to clean the image and remove noise.

The extract_text function takes the path to an image file and the path to an output text file as input. It loads the image, cleans it using the clean_image function, and then uses Tesseract OCR to extract text from the cleaned image. The extracted text is saved to the output text file.

The main function gets a list of image files in a directory, and then processes each image file using the extract_text function. The output text files are saved in a separate directory with names like text1.txt, text2.txt, etc.
