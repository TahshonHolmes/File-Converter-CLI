# imageconverter.py
import os
import imageio
import av

file_types = {
    '1': 'AVIF',
    '2': 'HEIF',
    '3': 'JIF',
    '4': 'JPEG',
    '5': 'JPG',
    '6': 'PDF',
    '7': 'PNG',
    '8': 'TIFF',
    '9': 'WEBP'
}

def image_converter_menu():
    print("What file type would you like to convert from?")
    for key, value in file_types.items():
        print(f"{key}. {value}")

def image_convert_to_menu(from_type):
    to_types = {key: value for key, value in file_types.items() if value != from_type}
    
    print("What file type would you like to convert to?")
    for key, value in to_types.items():
        print(f"{key}. {value}")

    to_choice = input("Enter your choice: ")

    # Map choice to file type
    to_type = to_types[to_choice]

    # Ask for filename
    filename = input(f"Enter the name of the file you want to convert from {from_type} to {to_type}: ")
    input_path = os.path.join(os.getcwd(), filename)

    if not os.path.isfile(input_path):
        print(f"File {filename} not found!")
        return

    try:
        if from_type == 'AVIF':
            container = av.open(input_path)
            for frame in container.decode(video=0):
                img = frame.to_image()
                new_filename = os.path.splitext(filename)[0] + '.' + to_type.lower()
                img.save(os.path.join(os.getcwd(), new_filename))
        else:
            image = imageio.imread(input_path)
            new_filename = os.path.splitext(filename)[0] + '.' + to_type.lower()
            imageio.imwrite(os.path.join(os.getcwd(), new_filename), image)
        print(f"Converted {filename} to {new_filename}")
    except Exception as e:
        print(f"Failed to convert {filename}: {str(e)}")

    input("Conversion complete. Press Enter to continue...")
