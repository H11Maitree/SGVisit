print("CAROUSEL RESIZER")
import os
import glob

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the file extensions for images
image_extensions = ['*.jpeg', '*.jpg', '*.png', '*.JPG']

# Create a list to store all image files
image_files = []

# Loop through each image extension and find matching files
for extension in image_extensions:
    # Create a file path pattern to match the image files
    pattern = os.path.join(current_dir, extension)
    
    # Use glob to find all files matching the pattern
    image_files.extend(glob.glob(pattern))

from PIL import Image, ImageFilter

def process_image(input_filepath, output_filepath="output.jpg", output_size=(1960, 840), blur_radius=10):
    # Open the original image
    input_image = Image.open(input_filepath)

    #display(input_image)

    input_ratio = input_image.width / input_image.height
    output_ratio = output_size[0] / output_size[1]

    # Depending on the input image's aspect ratio, adjust width or height while maintaining aspect ratio for foreground
    if input_ratio > output_ratio:
        # Width needs more adjustment
        new_width = output_size[0]
        new_height = round(new_width / input_ratio)
    else:
        # Height needs more adjustment
        new_height = output_size[1]
        new_width = round(new_height * input_ratio)

    # Resize the image maintaining its aspect ratio for foreground
    resized_image = input_image.resize((new_width, new_height), Image.ANTIALIAS)

    #display(resized_image)

    # Depending on the input image's aspect ratio, adjust width or height while maintaining aspect ratio for background
    if input_ratio > output_ratio:
        # Height needs more adjustment
        new_height_bg = output_size[1]
        new_width_bg = round(new_height_bg * input_ratio)
    else:
        # Width needs more adjustment
        new_width_bg = output_size[0]
        new_height_bg = round(new_width_bg / input_ratio)

    # Create the Gaussian blur background by blurring the original image and then resizing
    background = input_image.filter(ImageFilter.GaussianBlur(blur_radius))
    background = background.resize((new_width_bg, new_height_bg))

    # Calculate the position for the background image to be pasted onto the output canvas
    pos_x_bg = (output_size[0] - new_width_bg) // 2
    pos_y_bg = (output_size[1] - new_height_bg) // 2

    # Create a new blank canvas and paste the background image onto it
    canvas = Image.new('RGB', output_size)
    canvas.paste(background, (pos_x_bg, pos_y_bg))

    # Calculate the position for the input image to be pasted onto the background
    pos_x = (output_size[0] - new_width) // 2
    pos_y = (output_size[1] - new_height) // 2

    # Paste the input image onto the canvas
    canvas.paste(resized_image, (pos_x, pos_y))

    #display(canvas)
    
    canvas.save(output_filepath)

    return canvas

if not os.path.exists(current_dir+"/resized/"):
    os.makedirs(current_dir+"/resized/")

# Loop through each image file
for file_path in image_files:
    # Extract the file name
    file_name = os.path.basename(file_path)
    print("START:", file_path )
    
    process_image(file_path, current_dir+"/resized/"+file_name)
    print("DONE:", file_name )