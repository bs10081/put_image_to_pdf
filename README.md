# Put Image to PDF

This project converts images from subfolders into PDF files, where each subfolder represents one PDF. Each image from the subfolder is placed on a separate page of the PDF while maintaining its original aspect ratio. The PDF files are generated in the `output` folder located in the root directory, and the PDFs are named after their respective subfolder names.

## Features
- Supports multiple image formats including JPEG, PNG, and HEIC.
- Maintains the original aspect ratio of the images on each page.
- Automatically generates a PDF file for each subfolder of images.
- Saves the resulting PDFs in the `output` folder within the root directory.

## Requirements

- Python 3.x
- ReportLab: A Python library for generating PDFs.
- Pillow: A Python Imaging Library (PIL) fork to process images.
- pyheif: To handle HEIC format image conversion.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bs10081/put_image_to_pdf.git
   cd put_image_to_pdf
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, create it with the following contents:

   ```bash
   reportlab
   pillow
   pyheif
   ```

   Alternatively, you can manually install the libraries using pip:

   ```bash
   pip install reportlab pillow pyheif
   ```

3. Make sure you have `wkhtmltopdf` installed for handling HEIC files:

   - For macOS:
     ```bash
     brew install pyheif
     ```
   - For Linux (Debian-based):
     ```bash
     sudo apt-get install python3-pyheif
     ```

## Usage

1. Prepare your folder structure:

   - The `root_folder` contains multiple subfolders.
   - Each subfolder contains the images you want to convert into a PDF.

   Example structure:

   ```
   root_folder/
   ├── subfolder1/
   │   ├── image1.jpg
   │   ├── image2.png
   ├── subfolder2/
   │   ├── image1.heic
   │   ├── image2.jpeg
   ```

2. Update the `root_folder` path in the Python script:

   ```python
   if __name__ == "__main__":
       # Root folder that contains multiple subfolders with images
       root_folder = "/path/to/your/root_folder"  # Replace this with your actual path
       generate_pdfs_from_folders(root_folder)
   ```

3. Run the script:

   ```bash
   python3 main.py
   ```

4. The generated PDFs will be located in the `output` folder under the root directory, and each PDF will be named after the subfolder it was created from.

## Example

Suppose you have the following directory structure:

```
root_folder/
├── vacation_photos/
│   ├── beach.jpg
│   ├── sunset.heic
├── work_documents/
│   ├── graph.png
│   ├── chart.jpg
```

Running the script will generate:

```
root_folder/output/
├── vacation_photos.pdf
├── work_documents.pdf
```

Each image from the `vacation_photos` and `work_documents` folders will appear on its own page in the corresponding PDF, with the images maintaining their original aspect ratio.

## Notes

- Only image files (JPEG, PNG, HEIC, etc.) will be included in the PDFs. Other file types in the subfolders will be ignored.
- Ensure that the `pyheif` library is installed if you are processing HEIC files.
- The generated PDFs are placed in the `output` folder inside the root directory.

## Contributing

Feel free to submit issues or pull requests to improve this project!

## License

This project is licensed under the MIT License.
