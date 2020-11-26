from bs4 import BeautifulSoup
import requests


def apstrada_datni(datne):
    with open(datne, encoding="UTF-8") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup


def apstrada_lapu(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup