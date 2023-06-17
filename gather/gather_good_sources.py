import re

# Open the text file and read its contents
with open('extractfile.txt', 'r') as file:
    data = file.readlines()

# Iterate over each line and extract the htmlUrl tag
html_urls = []
for line in data:
    match = re.search(r'xmlUrl="[^"]+"\s+htmlUrl="([^"]+)"', line)
    if match:
        html_url = match.group(1)
        html_urls.append(html_url)

# Save the extracted htmlUrls to a text file
if html_urls:
    with open('html_urls.txt', 'w') as output_file:
        for html_url in html_urls:
            output_file.write(html_url + '\n')
        print("htmlUrls extracted and saved to html_urls.txt")
else:
    print("No htmlUrls found in the file.")
