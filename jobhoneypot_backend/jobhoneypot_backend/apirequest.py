# Script to authenticate InfoJobs
import requests
import json

# Function to get authentication keys
def get_keys():
    return ('926e44920bba4b959ae745c8221a7db6', 'sAnEd8eHCKST0/27j1xMEnpxBSerjUGHtevTIsfj6KJuApJ4hJ')


# Convert Json from API to Python values
def convto_jsons(json_values):
    return json.loads(json_values.content)


# Function which send request to InfoJobs API
def request_api(url_string):
    r = requests.get(url_string, auth=get_keys())
    first_page = convto_jsons(r)

    noOfResults = first_page["totalResults"]
    if noOfResults > 700:
        noOfResults = 700

    job_results = requests.get(url_string + "&maxResults=" + str(noOfResults), auth=get_keys())

    return convto_jsons(job_results)

def get_alljobs():
    url = 'https://api.infojobs.net/api/7/offer?'
    r = requests.get(url, auth=get_keys())
    return convto_jsons(r)

# Get Job with specific setting.
def get_job(skill_list=None, industry=None, nationality=None):
    url = 'https://api.infojobs.net/api/7/offer?'
    if skill_list is not None:
        for skill in skill_list:
            url += "q=" + skill + '&'

    if industry is not None:
        for i in industry:
            url += "category=" + i + "&"

    if nationality is not None:
        url += "category" + nationality + "&"

    return request_api(url)
    #return convto_jsons(r)



