# Converter.py
import imageconverter
import ebookconverter
import documentconverter
import audioconverter
import videoconverter

def main_menu():
    print("******MENU*******")
    print("1. Audio Converter")
    print("2. Video Converter")
    print("3. Image Converter")
    print("4. Document Converter")
    print("5. E-book Converter")
    print("6. Exit")
    print("********************")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            audioconverter.audio_converter_menu()
            from_choice = input("Enter your choice (1-6): ")

            from_type = audioconverter.file_types.get(from_choice)

            # Remove chosen type from options
            del audioconverter.file_types[from_choice]

            audioconverter.audio_convert_to_menu(from_type)

        elif choice == '2':
            videoconverter.video_converter_menu()
            from_choice = input("Enter your choice (1-6): ")

            from_type = videoconverter.file_types.get(from_choice)

            # Remove chosen type from options
            del videoconverter.file_types[from_choice]

            videoconverter.video_convert_to_menu(from_type)

        elif choice == '3':
            imageconverter.image_converter_menu()
            from_choice = input("Enter your choice (1-9): ")

            from_type = imageconverter.file_types.get(from_choice)

            # Remove chosen type from options
            del imageconverter.file_types[from_choice]

            imageconverter.image_convert_to_menu(from_type)

        elif choice == '4':
            documentconverter.document_converter_menu()
            from_choice = input("Enter your choice (1-11): ")

            from_type = documentconverter.file_types.get(from_choice)

            # Remove chosen type from options
            del documentconverter.file_types[from_choice]

            documentconverter.document_convert_to_menu(from_type)

        elif choice == '5':
            ebookconverter.ebook_converter_menu()
            from_choice = input("Enter your choice (1-4): ")

            from_type = ebookconverter.file_types.get(from_choice)

            # Remove chosen type from options
            del ebookconverter.file_types[from_choice]

            ebookconverter.ebook_convert_to_menu(from_type)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
