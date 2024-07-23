# File Converter CLI

File Converter CLI is a Python command-line interface for converting various file types including images, documents, ebooks, audio, and video files using different tools like FFmpeg and Pandoc.

## Features

- **Audio Converter**: Convert between M4A, MP2, MP3, MP4, WAV, and WMA formats.
- **Video Converter**: Convert between M4V, MKV, MOV, MP4, WEBM, and XVID formats.
- **Image Converter**: Convert between AVIF, HEIF, JIF, JPEG, JPG, PDF, PNG, and TIFF formats.
- **Document Converter**: Convert between CSV, DOC, DOCM, DOCX, HTML, PDF, PPT, PPTX, TXT, XLS, and XLSX formats.
- **E-book Converter**: Convert between EPUB, MOBI, PDF, and AZW formats.

## Dependencies

- Python 3.x
- FFmpeg (for audio and video conversions)
- Pandoc (for document conversions)
- Unoconv (for specific document conversions, optional)

## Installation

1. **Python Installation**:
   - Ensure Python 3.x is installed. If not, download and install it from [python.org](https://www.python.org/downloads/).

2. **FFmpeg Installation**:
   - Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and follow the installation instructions for your operating system.

3. **Pandoc Installation** (Optional, for document conversions):
   - Download Pandoc from [pandoc.org](https://pandoc.org/installing.html) and install it according to the instructions for your operating system.

4. **Unoconv Installation** (Optional, for specific document conversions):
   - Install LibreOffice from [libreoffice.org](https://www.libreoffice.org/download/download/) and set up Unoconv as described in the project setup.

5. **Clone the Repository**:
   ```bash
   git clone https://github.com/Tahshon-Holmes/FileConverterCLI.git
   cd FileConverterCLI
