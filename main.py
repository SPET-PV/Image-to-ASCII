from core import *

def execution():
	"""
    Executes the process of converting an image to ASCII art and saving it to a text file.

    This function performs the following steps:
    1. Takes user inputs for an image path and an output file path.
    2. Opens the specified image file and creates an output file.
    3. Converts the image to grayscale and creates a matrix of brightness values.
    4. Converts pixel brightness values to ASCII symbols representing a gradient of shades.
    5. Saves the ASCII representation of the image to a text file.
    
    :raises Exception: If an error occurs during the execution, it is raised and printed.
    """
	try:
		#Inputs
		original_image, file_name = inputs()
		#Optionnal Resizing:
		while True:
			choice = int(input("Do you want to keep the original image size or resize the image :\n1) keep original image\n2) Resize the image\n: "))
			if choice not in [1,2]:
				raise ValueError("Invalid choice. Please enter '1' to keep the original image size or '2' to resize the image")
			elif int(choice) == 1:
				matrix = matrix_creation(original_image)
				break
			elif int(choice) == 2:
				resized_image = resize_image(original_image)
				#Pixel Brightness Values Matrix Creation
				matrix = matrix_creation(resized_image)
				break
		#Pixel Brightness Values to 16 shades of ASCII Symbols conversion
		ascii_matrix = convert_to_ascii(matrix)
		#Saving the ASCII matrix to the file
		save_ascii_to_file(ascii_matrix,file_name)
		print(f"Image converted to ASCII successfully!")
	except Exception as e:
		print(f"Error : {e}")
		raise e
	finally:
		print("Exiting the ...")


if __name__ == "__main__":
	execution()
