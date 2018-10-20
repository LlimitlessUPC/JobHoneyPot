# Script to authenticate InfoJobs
import requests
from requests.auth import HTTPBasicAuth

#def 

def authenticate():
    url = 'https://api.infojobs.net/api/7/offer'
    #s = requests.session()
    #r = s.get(url, params=values)
    r = requests.get(url,
                    auth=('926e44920bba4b959ae745c8221a7db6', 'sAnEd8eHCKST0/27j1xMEnpxBSerjUGHtevTIsfj6KJuApJ4hJ'))
    print(r.content)
authenticate()
