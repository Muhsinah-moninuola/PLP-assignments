"""
This is a food preservation techniques images fetcher.
You type/paste links to food preservation images (from articles, blogs, etc.)
The script fetches and organizes them into a folder.
Purpose: helps students/researchers collect reference images 
"""

import requests as rq #library for making HTTP requests
import os #library for file and folder management
from urllib.parse import urlparse as up #helps to extract filename from URL
from PIL import Image
from io import BytesIO as BIO
import re

def fetch_images(urls, category="General"):
    # Create base directory
    base_dir = os.path.join("Fetched_Images", category)
    os.makedirs(base_dir, exist_ok=True)

    # Create a log file
    log_path = os.path.join(base_dir, "download_log.txt")
    log_file = open(log_path, "a")

    for url in urls:
        try:
            # Fetch the image with headers
            headers = {"User-Agent": "UbuntuImageFetcher/1.0"}
            response = rq.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # Check content type header before saving
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"Skipping (not an image): {url}")
                continue

            # Extract filename or auto-generate
            parsed_url = up(url)
            filename = os.path.basename(parsed_url.path)

            if not filename or "." not in filename:
                ext = content_type.split("/")[-1]
                filename = f"{category.lower()}_{abs(hash(url))}.{ext}"

            filepath = os.path.join(base_dir, filename)

            # Prevent duplicates
            if os.path.exists(filepath):
                print(f"Duplicate skipped: {filename}")
                continue

            # Save image
            with open(filepath, "wb") as f:
                f.write(response.content)

            # Log the download
            log_file.write(f"{url} ; {filename}\n")

            #success message

            print(f"Successfully fetched: {filename}")
            print(f"Image saved to {filepath}")

            # Preview image (optional)
            img = Image.open(BIO(response.content))
            img.show()

        except rq.exceptions.RequestException as e:
            print(f"Connection error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    log_file.close()
    print("\nConnection strengthened. Community enriched. Thank you for your contributions")

def main():
    print('Welcome to the Unbutu Image Fatcher')
    print("A tool for mindfully collecting images from the web")

    category = input("Enter a category name (e.g., Canning, Freezing, Drying): ")
    print("Paste multiple image URLs (separated by commas):")
    url_input = input("> ")

    # Remove any illegal filename characters
    category = re.sub(r'[<>:"/\\|?*^]', '', category)

    # If category becomes empty, fallback to "Default"
    if not category:
        category = "Default"

    urls = [u.strip() for u in url_input.split(",") if u.strip()]
    if not urls:
        print("No URLs provided. Exiting.")
        return

    fetch_images(urls, category)

if __name__ == "__main__":
    main()