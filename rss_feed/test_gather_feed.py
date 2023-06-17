import feedparser
import xml.etree.ElementTree as ET

"""
Gathers recent blog articles on an RSS reader.

This is good, it provides the following:
example
Title: Gain Insights With Impact at sparkConf 2023
Published: 2023-06-08T14:30:00-05:00
Link: https://8thlight.com/insights/announcing-sparkconf-2023

We could parse the link and send it to the scrape.js function, then send the payload over to the pipeline for processing

"""

def read_ompl_file(file_path):
    with open(file_path, 'r') as file:
        ompl_content = file.read()
    return ompl_content

def extract_blog_urls(ompl_content):
    urls = []
    root = ET.fromstring(ompl_content)
    for outline in root.findall('.//outline'):
        if 'xmlUrl' in outline.attrib:
            url = outline.attrib['xmlUrl']
            urls.append(url)
    return urls

def display_blog_feeds(blog_urls):
    for url in blog_urls:
        feed = feedparser.parse(url)
        print(f"Feed Title: {feed.feed.title}")
        if 'description' in feed.feed:
            print(f"Feed Description: {feed.feed.description}")
        else:
            print("Feed Description: N/A")
        print("Recent Posts:")
        for entry in feed.entries[:5]:  # Displaying the latest 5 posts
            print(f"Title: {entry.title}")
            print(f"Published: {entry.published}")
            print(f"Link: {entry.link}")
            print(f"Summary: {entry.summary}")
            print("-" * 50)

# Path to your OPML file
ompl_file_path = 'single.opml'

# Read OPML file
ompl_content = read_ompl_file(ompl_file_path)

# Extract blog URLs from OMPL file
blog_urls = extract_blog_urls(ompl_content)

# Display blog feeds
display_blog_feeds(blog_urls)
