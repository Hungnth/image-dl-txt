import os
import requests

# Create the "image" directory if it does not exist
if not os.path.exists("image"):
    os.makedirs("image")

# List to store the row numbers of skipped URLs
skipped_urls = []

# Open the links.txt file in read mode and read its contents
with open("links.txt", "r") as txt_file:
    # Read the URLs from the file, one per line
    urls = txt_file.read().strip().split("\n")

# Open a file in write mode and create a file object
with open("error_log.txt", "w") as log_file:
    # Iterate over the URLs in the list
    for i, url in enumerate(urls):
        # Make a request to the URL
        response = requests.get(url)

        # Check if there was an error
        if not response.ok:
            # Write the error message to the log file in the specified format
            log_file.write(f"{i+1}, {url}\n")
            # Print an error message
            print(f"Error: Could not download image from URL {url}")

            # Add the row number of the skipped URL to the list
            skipped_urls.append(i+1)

            # Skip the rest of the loop
            continue

        # Extract the file name from the URL
        file_name = url.split("/")[-1]

        # Open a file with the "write binary" mode and write the image data to it
        # Use the os.path.join() method to specify the path to the image folder
        with open(os.path.join("image", file_name), "wb") as f:
            f.write(response.content)

        # Print a message showing the progress
        print(f"Downloaded image {i+1} of {len(urls)}: {file_name}")

# Print the row numbers of the skipped URLs
if len(skipped_urls) > 0:
    print(f"Skipped URLs at row(s): {', '.join(str(i) for i in skipped_urls)}")
