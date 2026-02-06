#!/usr/bin/env python3
"""
Convert logo images to WebP format for better performance
Reduces file sizes while maintaining quality
"""

from PIL import Image
import os

def convert_to_webp(input_path, output_path, quality=85):
    """Convert image to WebP format"""
    try:
        img = Image.open(input_path)

        # Convert RGBA to RGB if needed (WebP handles both, but RGB is smaller)
        if img.mode == 'RGBA':
            # Keep RGBA for images that need transparency
            img.save(output_path, 'WEBP', quality=quality, method=6)
        else:
            # Convert to RGB for non-transparent images
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(output_path, 'WEBP', quality=quality, method=6)

        # Get file sizes
        original_size = os.path.getsize(input_path) / 1024  # KB
        new_size = os.path.getsize(output_path) / 1024  # KB
        savings = ((original_size - new_size) / original_size) * 100

        print(f"[OK] {os.path.basename(output_path)}")
        print(f"  {original_size:.1f}KB -> {new_size:.1f}KB (saved {savings:.0f}%)")

        return True
    except Exception as e:
        print(f"[ERROR] Error converting {input_path}: {e}")
        return False

if __name__ == "__main__":
    print("Converting logo images to WebP format...\n")

    # Images to convert
    conversions = [
        ("rising-sun-logo.png", "images/logo.webp"),
        ("rising-sun-logo-white.png", "images/logo-white.webp"),
        ("rising-sun-logo-black.png", "images/logo-black.webp"),
        ("rising-sun-logo-circle.png", "images/logo-circle.webp"),
        ("og-primary.jpg", "images/og-image.webp"),
    ]

    success_count = 0
    for input_file, output_file in conversions:
        if os.path.exists(input_file):
            if convert_to_webp(input_file, output_file, quality=85):
                success_count += 1
            print()
        else:
            print(f"[WARN] Skipping {input_file} (not found)\n")

    print(f"\n[OK] Converted {success_count}/{len(conversions)} images successfully")
    print("\nNext steps:")
    print("1. Update HTML files to reference new WebP images")
    print("2. Keep PNG fallbacks for older browsers if needed")
    print("3. Move original PNG files to _archive/")
