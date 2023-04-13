import requests
import time
from parsel import Selector


BASE_URL = 'https://blog.betrybe.com/'


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url,
            timeout=2,
            headers={"user-agent": "Fake user-agent"}
            )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    select = Selector(text=html_content)
    link = select.css(
        'div.post-outer a.cs-overlay-link::attr(href)').getall()
    return link


# Requisito 3
def scrape_next_page_link(html_content):
    select = Selector(text=html_content)
    go_next_page = select.css('a.next.page-numbers::attr(href)').get()
    if not (go_next_page):
        None
    return go_next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
# Iniciando projeto
