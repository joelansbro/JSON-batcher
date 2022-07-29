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

JSON should save down into the /data/ folder.

4. Within the pipeline repository, run `bash runjob.sh` to start the pipeline (check repo README.md for installation)

5. Within this repo, run `send_payload.py`
