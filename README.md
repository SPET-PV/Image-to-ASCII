# Image_to_ASCII

Converts images into ASCII art representations.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [License](#license)

## Overview

This Python project is designed to convert images into ASCII art. It takes an image file as input, processes it to create a matrix of pixel brightness values, and then converts these values into ASCII characters, creating an ASCII representation of the image. The resulting ASCII art can be saved as a text file.

## Features

- Image to ASCII Conversion: Convert multiple image formats (JPEG,PNG,BMP,TIFF,WebP) into ASCII symbols representations.
- Resizing Options: Choose to keep the original image size or resize based on aspect ratio or percentage reduction.
- Text File Output: Save the ASCII art as a text file for easy viewing and sharing.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SPET-PV/image-to-ascii.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Dependencies & Versions

- [Python (3.11.2)](https://www.python.org/downloads/release/python-3112/)
- [Pillow "PIL" (10.2.0) (Python Imaging Library)](https://pypi.org/project/pillow/)

> **Note:** This script has been tested on Python version 3.11.2 and uses Pillow (10.2.0). It has not been tested on older versions of Python or the Pillow package.

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. Follow the provided instructions:
    - **Input the image path:** It should be in one of the supported formats (JPEG, PNG, BMP, TIFF, WebP) and must not exceed the pixels limit (10,000 x 8,947) (Height * Width < 89,478,485 pixels).
    - **Specify the output file path:** If it doesn't exist, the script will create the file with the specified name. The output file extension must be in the `.txt` file format (e.g., `~/Desktop/output.txt`) and have correct accessibility permissions.

3. Optional: Choose whether to resize the image:
    - Choose '1' to retain the original image size.
    - Choose '2' to resize based on aspect ratio or percentage reduction.
    - For aspect ratio: Input the desired width and height.
    - For percentage reduction: Input the reduction percentage (0-100).

4. Upon completion, the script will convert the image into ASCII art, saving it to your specified text file path.

> **Note:** Using poor-quality images may result in lower-quality ASCII output. Heavy resizing can lead to loss of details and reduced output quality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.