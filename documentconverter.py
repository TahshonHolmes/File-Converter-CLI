# documentconverter.py
import os
import subprocess

file_types = {
    '1': 'CSV',
    '2': 'DOC',
    '3': 'DOCM',
    '4': 'DOCX',
    '5': 'HTML',
    '6': 'PDF',
    '7': 'PPT',
    '8': 'PPTX',
    '9': 'TXT',
    '10': 'XLS',
    '11': 'XLSX'
}

def document_converter_menu():
    print("What file type would you like to convert from?")
    for key, value in file_types.items():
        print(f"{key}. {value}")

def document_convert_to_menu(from_type):
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
        
        if from_type in ['DOC', 'DOCM', 'DOCX', 'PPT', 'PPTX', 'XLS', 'XLSX'] or to_type in ['DOC', 'DOCM', 'DOCX', 'PPT', 'PPTX', 'XLS', 'XLSX']:
            subprocess.run(['unoconv', '-f', to_type.lower(), '-o', output_path, input_path], check=True)
        else:
            subprocess.run(['pandoc', input_path, '-o', output_path], check=True)

        print(f"Converted {filename} to {output_filename}")
    except Exception as e:
        print(f"Failed to convert {filename}: {str(e)}")

    input("Conversion complete. Press Enter to continue...")
