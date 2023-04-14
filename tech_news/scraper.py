import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    links = select.css(
        'div.post-outer a.cs-overlay-link::attr(href)').getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    select = Selector(text=html_content)
    go_next_page = select.css('a.next.page-numbers::attr(href)').get()
    if not (go_next_page):
        None
    return go_next_page


# Requisito 4
def scrape_news(html_content):
    answer = {}
    select = Selector(text=html_content)
    answer = {
        'url': select.css('link[rel=canonical]::attr(href)').get(),
        'title': select.css('h1.entry-title::text').get().strip(),
        'timestamp': select.css('.meta-date::text').get(),
        'writer': select.css('.author > a::text').get(),
        'reading_time': int(
            select.css('.meta-reading-time::text').get().split()[0]
        ),
        'summary': select.css('.entry-content p')
        .xpath('string()').get().strip(),
        'category': select.css('.category-style > .label::text').get(),
    }

    return answer


# Requisito 5
def get_tech_news(amount):
    go_next_page = fetch('https://blog.betrybe.com/')
    links = scrape_updates(go_next_page)
    news = []

    new_page = scrape_next_page_link(go_next_page)

    while len(links) < amount:
        new_content = fetch(new_page)
        links.extend(scrape_updates(new_content))
        new_page = scrape_next_page_link(new_content)

    news = [
        scrape_news(fetch(link)) for link in links[:amount]
    ]

    create_news(news)
    return news
