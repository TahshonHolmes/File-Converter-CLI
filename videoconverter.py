# videoconverter.py
import os
import subprocess

file_types = {
    '1': 'M4V',
    '2': 'MKV',
    '3': 'MOV',
    '4': 'MP4',
    '5': 'WEBM',
    '6': 'XVID'
}

def check_ffmpeg_installation():
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def video_converter_menu():
    print("What file type would you like to convert from?")
    for key, value in file_types.items():
        print(f"{key}. {value}")

def video_convert_to_menu(from_type):
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
        
        if not check_ffmpeg_installation():
            print("FFmpeg is not installed. Please install it to convert video files.")
            return

        subprocess.run(['ffmpeg', '-i', input_path, output_path], check=True)

        print(f"Converted {filename} to {output_filename}")
    except Exception as e:
        print(f"Failed to convert {filename}: {str(e)}")

    input("Conversion complete. Press Enter to continue...")
