import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 800), output_format='JPEG'):
    """
    Resizes and converts all images in a folder.

    Args:
        input_folder (str): Path to the folder containing original images.
        output_folder (str): Path where resized images will be saved.
        size (tuple): Desired image size, e.g., (800, 800).
        output_format (str): Desired output format ('JPEG', 'PNG', etc.)
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip non-image files
        if not os.path.isfile(file_path):
            continue

        try:
            with Image.open(file_path) as img:
                img = img.resize(size)
                base_name, _ = os.path.splitext(filename)
                new_filename = f"{base_name}.{output_format.lower()}"
                save_path = os.path.join(output_folder, new_filename)
                img.save(save_path, output_format)
                print(f"✅ Saved: {save_path}")
        except Exception as e:
            print(f"⚠️ Could not process {filename}: {e}")

if __name__ == "__main__":
    input_folder = input("Enter the path to the input folder: ").strip()
    output_folder = input("Enter the path to the output folder: ").strip()
    width = int(input("Enter the desired width (e.g., 800): "))
    height = int(input("Enter the desired height (e.g., 800): "))
    format_choice = input("Enter output format (JPEG/PNG): ").upper()

    resize_images(input_folder, output_folder, size=(width, height), output_format=format_choice)
    print("\n🎉 All images have been resized and saved successfully!")
