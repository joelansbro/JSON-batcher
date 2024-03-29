from distutils.log import error
import requests
import glob
import os
import time
import json
import argparse

"""
Take the json saved within data/ and send it to the pipeline inboundAPI, sleep between put requests
"""


# Collects the saved json, runs manipulations and stores in a list ready to send
def prepare_json_payload(project_name):
    all_files = []

    for root, dirs, files in os.walk('./data/'):
        files = glob.glob(os.path.join(root,'*.json'))
        
        for f in files:
            with open(os.path.abspath(f)) as json_file:
                try:
                    json_to_pass = json.load(json_file)
                except:
                    print("There's an error here below:")
                    print(json_file)
                    continue
                data = clean_json(
                    json_to_pass,
                    project_name
                    )
                
                all_files.append(data)

    return all_files

# Applying basic data cleaning techniques so that we pass the inboundAPI schema
def clean_json(json, project_name):
    json['project'] = project_name
    del json['dek']
    
    if json['author'] == None:
        json['author'] = "Unknown Author"
    
    return json


def make_request(url, json):
    res = requests.post(url, json=json)
    try:
        if res.ok:
            return res.content
    except:
        return 'Shame thsat'


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Send json batch payload into the pipeline")
    
    parser.add_argument("--url", type=str, nargs="?", help="Destination url to point payload", default="http://localhost:5000/inbound/add_article")
    parser.add_argument("--project", type=str, nargs="?", help="Name of the project that the URLs are a part of", default="None",)
    args = parser.parse_args()
    url = args.url

    files_list = prepare_json_payload(args.project)
    print(url)

    for file in files_list:
        response = make_request(url, file)
        time.sleep(1)