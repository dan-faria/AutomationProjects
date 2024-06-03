# Image Editing Script

This Python script processes all images in a specified folder by applying a series of enhancements and saves the edited images to another folder. It uses the Pillow library for image manipulation.

## Features

- Reads images from a specified input directory.
- Applies sharpening and converts images to black and white.
- Enhances the contrast of the images.
- Saves the edited images to a specified output directory with a modified filename.

## Prerequisites

Ensure you have Python installed on your system. This script requires the Pillow library, which can be installed using pip.

## Installation

Upgrade pip and install the Pillow library using the following commands:

- python -m pip install --upgrade pip
- python -m pip install --upgrade Pillow

## Usage
- Place the images you want to edit in the ./imgs folder.
- Run the script.
- The script will process each image, apply the specified enhancements, and save the edited images in the ./editedImgs folder.