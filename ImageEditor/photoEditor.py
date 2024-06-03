# python -m pip install --upgrade pip
# python -m pip install --upgrade Pillow

from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"  # folder for unedited images
pathOut = "./editedImgs"  # folder for edited images

for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    if os.path.isfile(filepath):  # Check if it's a file
        img = Image.open(filepath)

        # sharpening, BW
        edit = img.filter(ImageFilter.SHARPEN).convert('L')

        # contrast
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        # ADD MORE EDITS FROM DOCUMENTATION https://pillow.readthedocs.io/en/stable/

        clean_name = os.path.splitext(filename)[0]
        edited_filename = f"{clean_name}_edited.jpg"
        edited_filepath = os.path.join(pathOut, edited_filename)
        edit.save(edited_filepath)