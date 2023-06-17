# Quick Scraper

This is a simple script to automate the scraping of articles via Mercury-Parser.

> Requirements:

Requires a valid Node installation (tested on v10.19.0)

Requires Minimum Python3 v3.8.10

> Packages:


```
yarn add @postlight/mercury-parser
```

```
python3 -m pip install argparse
```


----

Instructions:

1. Input some blog urls into params.txt

2. run `node scrape.js`

3. Enjoy the output json

JSON should save down into the /data/ folder as individual files, in the following format:

```
title
author
date_published
dek
lead_image_url
content
next_page_url
url
domain
excerpt
word_count
direction
total_pages
rendered_pages
```

4. Within the pipeline repository, run `bash runjob.sh` to start the pipeline (check pipeline README.md for installation).

5. Within this repo, run `send_payload.py --url --project` where the url points to the inbound API endpoint route (the default is `inbound/add_article`) and project designates the specific project name (default is `None`, so ensure you specify one particularly if you hope to store multiple projects within the same database)


6. The Rss feed link will gather most recent articles from the blogs and show them, then at this point we need to request the URLS, save them down and pass them to the pipeline