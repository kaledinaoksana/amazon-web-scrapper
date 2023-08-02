import requests
from bs4 import BeautifulSoup
import settings as s

def connect(URL):
    page = requests.get(URL, headers=s.headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    return BeautifulSoup(soup1.prettify(), 'html.parser')