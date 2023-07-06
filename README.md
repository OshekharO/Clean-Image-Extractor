# Clean Image Extractor

A Python-based tool that leverages the power of OpenCV and Tesseract OCR to cleanse images and extract text from them in a bulk manner. 

## Prerequisite

Before proceeding, ensure that the [Tesseract OCR engine](https://github.com/tesseract-ocr/tesseract/wiki) is installed on your system. Tesseract OCR is an open-source Optical Character Recognition engine used to recognize textual data from images.

## How it Works

The program runs in two significant steps:

1. **Image Cleaning**: Through OpenCV, the program processes each image, reducing noise and enhancing the image quality to ensure optimal text extraction.

2. **Text Extraction**: Utilizing the Tesseract OCR engine, the program extracts textual data from the cleaned images, writing the result to individual text files.

## Usage

Here's a breakdown of the core functions and how they interact:

- `clean_image()`: This function accepts an image as input, applying several image processing techniques via OpenCV to clean the image and eliminate noise.

- `extract_text()`: This function takes two parameters: the path to an image file and the path to an output text file. It loads the image, cleans it using the `clean_image()` function, and then uses Tesseract OCR to extract text from the cleaned image. The extracted text is then saved to the specified output text file.

- `main()`: This function serves as the orchestrator. It retrieves a list of image files in a specified directory, processing each image file using the `extract_text()` function. The resulting output text files are saved in a separate directory, with names following the format `text1.txt`, `text2.txt`, and so on.

### Disclaimer

Please note that the quality of the image impacts the accuracy of the text extraction. Better image quality would invariably lead to more accurate text extraction. Post-processing such as spell-checking might also be necessary to handle OCR's occasional recognition errors.
