"""
This module provides functions for processing images, converting them to ASCII art, and saving the ASCII representation to a text file.

Functions:
    1. inputs() -> (PIL.Image.Image, str):
        - Prompts the user to input an image path and an output file path.
        - Opens the specified image file and creates an output file.
        - Returns a tuple containing the opened image object and the output file path.
    
    2. matrix_creation(image: PIL.Image.Image) -> list:
        - Converts an image to grayscale and creates a matrix of brightness values.
        - Parameters:
            - image (PIL.Image.Image): Image object to process.
        - Returns a 2D matrix containing brightness values of each pixel in the image.
    
    3. resize_image(input_image_path: str) -> Image:
            - Resize an image based on user preference: aspect ratio or percentage reduction.
            - Prompts the user to choose between resizing based on aspect ratio or by a percentage reduction.
            - Validates the input and performs the resizing operation accordingly.
            - Returns the resized image object.

    4. convert_to_ascii(matrix: list) -> list:
        - Converts pixel brightness values to ASCII symbols representing a gradient of shades.
        - Parameters:
            - matrix (list of lists): 2D matrix containing brightness values of each pixel in the image.
        - Returns an ASCII representation of the image based on brightness levels.
    
    5. save_ascii_to_file(ascii_matrix: list, file_name: str):
        - Saves an ASCII representation of an image to a text file.
        - Parameters:
            - ascii_matrix (list of strings): ASCII matrix representing the image.
            - file_name (str): Name of the output text file.
"""

from PIL import Image, ImageFilter

def inputs() -> (Image.Image, str):
    """
    Prompts the user to input an image path and an output file path.
    Opens the specified image file and creates an output file.
    :return: Tuple containing the opened image object, the output file path.
    :rtype: tuple (PIL.Image.Image, str, tuple)
    """
    # Open an image file
    while True:
        image_path = input("Input the image path: ")
        try:
            if image_path.lower().endswith(('.jpg', '.jpeg', '.tiff', '.bmp', '.png', '.webp')):
                img = Image.open(image_path)
                max_pixels = 89478485  # Maximum number of pixels allowed
                width, height = img.size
                if width * height > max_pixels:
                    raise ValueError(f"The image exceeds the maximum pixel limit of {max_pixels}. Please use a smaller image.")
                break
            else:
                raise ValueError("Invalid file format. Please provide an image in one of the supported formats (JPEG, PNG, BMP, TIFF, WebP).")
        except Exception as e:
            print(f"Cannot open the image. Retry... \nError: {e}")
    #Create a file
    while True:
        file_name = str(input("Input the output file path and name: "))
        try:
            if file_name.lower().endswith('.txt'):
                with open(file_name, 'w') as file:
                    print(f"File '{file_name}' created successfully.")
                    break
            else :
                print(f"The file path '{file_name}' doesn't end with a '.txt' extension.")
        except FileExistsError:
            print(f"File '{file_name}' already exists.")
        except Exception as e:
            print(f"Cannot create the file, Retry... \nError : {e}")
    
    return img, file_name

def resize_image(image: Image) -> Image:
    """
    Resize an image based on user preference: aspect ratio or percentage reduction.
    This function prompts the user to choose between resizing based on aspect ratio or by a percentage reduction.
    It then validates the input and performs the resizing operation accordingly.

    :param image: Original image object.
    :type image_path: str
    :return: Resized image object.
    :rtype: PIL.Image.Image
    """
    while True:
        try:
            # Get the original image size
            original_width, original_height = image.size
            # Ask for user choice
            choice = int(input("Choose resizing method :\n1) Aspect Ratio (Height,Width)\n2) Percentage of Reduction (%)\n:  "))
            # Ensure choice is either '1' or '2'
            if choice not in [1, 2]:
                raise ValueError("Invalid choice. Please enter '1' for aspect ratio or '2' for percentage reduction")
            if choice == 1:  # Aspect ratio
                # Ask for resizing dimensions
                output_width = int(input("Enter the desired width for the resized image: "))
                output_height = int(input("Enter the desired height for the resized image: "))
                # Ensure output_width and output_height are integers
                if not isinstance(output_width, int) or not isinstance(output_height, int):
                    raise ValueError("Resizing dimensions must be integers")
                # Ensure the resizing dimensions are within the original image size
                if output_width > original_width or output_height > original_height:
                    raise ValueError("Resizing dimensions should not exceed the original image size")
                # Ensure the resizing dimensions are non-negative and non-zero
                if output_width <= 0 or output_height <= 0:
                    raise ValueError("Resizing dimensions should be non-negative and non-zero")
                # Resize the image while maintaining the aspect ratio
                resized_image = image.resize((output_width, output_height), Image.LANCZOS)
            elif choice == 2:  # Percentage reduction
                # Ask for reduction percentage
                reduction_percentage = float(input("Enter the percentage reduction (0-100): "))
                # Ensure the percentage reduction is within the allowed range
                if not (0 < reduction_percentage <= 100):
                    raise ValueError("Percentage reduction should be between 0 and 100")
                # Calculate new dimensions based on the percentage reduction
                output_width = int(original_width * (1 - reduction_percentage / 100))
                output_height = int(original_height * (1 - reduction_percentage / 100))
                # Resize the image by the calculated dimensions
                resized_image = image.resize((output_width, output_height), Image.LANCZOS)
            # Return the resized image
            return resized_image
        except ValueError as e:
            print(f"Error: {e}. Please enter valid inputs.")
            # Continue the loop to re-ask for correct input

def matrix_creation(image: Image) -> list:
    """
    Converts an image to grayscale and creates a matrix of brightness values.
    
    :param image: Image object to process.
    :type image: PIL.Image.Image
    :return: 2D matrix containing brightness values of each pixel in the image.
    :rtype: list of lists
    """
    # Convert the image to grayscale for simplicity
    img = image.convert('L')
    # Get the pixel data as a flat list of brightness values
    pixel_data = list(img.getdata())
    # Reshape the pixel data into a 2D matrix
    width, height = img.size
    pixel_matrix = [pixel_data[i * width:(i + 1) * width] for i in range(height)]
    
    return pixel_matrix

def convert_to_ascii(matrix: list) -> list:
    """
    Convert pixel brightness values to ASCII symbols representing a gradient of shades.

    :param pixel_matrix: 2D matrix containing brightness values of each pixel in the image.
    :type pixel_matrix: list of lists
    :return: ASCII representation of the image based on brightness levels.
    :rtype: list of strings
    """
    ascii_symbols = [' ', '`', '.', ',', ':', '-', '*', '░', '▒', '#', '%', '&', '8', '@', '▓', '█']
    ascii_matrix = []
    for row in matrix:
        ascii_row = []
        for pixel_value in row:
            # Normalize pixel value to fit within the range of ASCII symbols
            symbol_index = int((pixel_value / 255) * (len(ascii_symbols) - 1))  # Adjusted index calculation
            ascii_row.append(ascii_symbols[symbol_index])
        ascii_matrix.append(''.join(ascii_row))
    
    return ascii_matrix

def save_ascii_to_file(ascii_matrix: list, file_name: str):
    """
    Save an ASCII representation of an image to a text file.
    
    :param ascii_matrix: ASCII matrix representing the image.
    :type ascii_matrix: list of strings
    :param file_name: Name of the output text file.
    :type file_name: str
    """
    with open(file_name, 'w') as file:
        for row in ascii_matrix:
            file.write(''.join(row) + '\n')
