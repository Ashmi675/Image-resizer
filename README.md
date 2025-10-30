Image Resizer Tool
📌 Objective

Automate the process of resizing and converting multiple images in a folder using Python and Pillow.

🧰 Tools & Technologies

Python 3.x

Pillow (PIL)

os module

⚙️ Features

✅ Resize all images in a folder
✅ Convert between formats (JPG → PNG, PNG → JPG, etc.)
✅ Automatically create an output folder
✅ Error handling for non-image files
✅ Simple command-line interface

🗂️ Project Structure
📁 Image-Resizer-Tool
│
├── image_resizer.py      # Main Python script
├── README.md             # Project documentation
├── 📂 input_images        # Folder containing original images (optional)
└── 📂 output_images       # Folder where resized images will be saved

🚀 How to Run

Clone the repository

git clone https://github.com/yourusername/Image-Resizer-Tool.git
cd Image-Resizer-Tool


Install dependencies

pip install pillow


Run the script

python image_resizer.py


Provide inputs

Enter path to the input folder

Enter path to the output folder

Specify desired width & height

Choose output format (JPEG or PNG)

🧩 Example
Enter the path to the input folder: C:\Users\You\Pictures\Originals
Enter the path to the output folder: C:\Users\You\Pictures\Resized
Enter the desired width (e.g., 800): 800
Enter the desired height (e.g., 800): 800
Enter output format (JPEG/PNG): JPEG


Output:

✅ Saved: C:\Users\You\Pictures\Resized\photo1.jpeg
✅ Saved: C:\Users\You\Pictures\Resized\photo2.jpeg
🎉 All images have been resized and saved successfully!

💡 Key Concepts

File Handling – Reading and writing files using the os module

Image Processing – Opening, resizing, and saving images using PIL.Image

Error Handling – Using try-except blocks to catch invalid files

Automation – Batch processing all images without manual effort
