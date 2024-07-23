# ebookconverter.py
import os
import subprocess

file_types = {
    '1': 'EPUB',
    '2': 'MOBI',
    '3': 'PDF',
    '4': 'AZW'
}

def ebook_converter_menu():
    print("What file type would you like to convert from?")
    for key, value in file_types.items():
        print(f"{key}. {value}")

def ebook_convert_to_menu(from_type):
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
        output_filename = os.path.splitext(filename)[0] + '.' + to_type.lower()
        output_path = os.path.join(os.getcwd(), output_filename)
        subprocess.run(['ebook-convert', input_path, output_path], check=True)
        print(f"Converted {filename} to {output_filename}")
    except Exception as e:
        print(f"Failed to convert {filename}: {str(e)}")

    input("Conversion complete. Press Enter to continue...")
