#!/usr/bin/env python3
"""
Crop OG image to exactly 1200x630 pixels
Removes excess height from top and bottom equally
"""

from PIL import Image
import sys

def crop_to_og_size(input_path, output_path):
    """Crop image to 1200x630 for OG image spec"""
    try:
        # Open image
        img = Image.open(input_path)
        current_width, current_height = img.size

        print(f"Current dimensions: {current_width}x{current_height}")

        # Target dimensions
        target_width = 1200
        target_height = 630

        # Calculate crop box (center crop)
        if current_height > target_height:
            # Crop from top and bottom equally
            excess_height = current_height - target_height
            top_crop = excess_height // 2
            bottom_crop = current_height - (excess_height - top_crop)

            # Crop box: (left, top, right, bottom)
            crop_box = (0, top_crop, current_width, bottom_crop)

            # Perform crop
            img_cropped = img.crop(crop_box)

            # Save
            img_cropped.save(output_path, 'JPEG', quality=90, optimize=True)

            final_width, final_height = img_cropped.size
            print(f"✓ Cropped to: {final_width}x{final_height}")
            print(f"✓ Saved to: {output_path}")
            print(f"✓ File size: {img_cropped.size}")

            return True
        else:
            print("Image is already correct height or too small")
            return False

    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    input_file = "og-primary.jpg"
    output_file = "og-primary-final.jpg"

    print("Cropping OG image to 1200x630...")
    success = crop_to_og_size(input_file, output_file)

    if success:
        print("\n✓ Done! Use og-primary-final.jpg for your website")
    else:
        print("\n✗ Crop failed")
