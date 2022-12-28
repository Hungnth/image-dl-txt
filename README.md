# Image Downloader via TXT file 
This script reads a list of URLs from a file called `links.txt`, and then downloads the images at those URLs to a folder called image. If an error occurs while trying to download an image from one of the URLs, the script logs the error message to a file called `error_log.txt` and prints an error message to the console. If there are any URLs that couldn't be downloaded, the script also prints the row numbers of those URLs at the end.

## Requirements
- Python 3
- `requests` library

## Usage
1. Place the script in the same directory as the links.txt file.
2. Run the script with the following command:
```commandline
python image_downloader.py
```

The script will create the `image` folder if it doesn't already exist, and then start downloading the images.