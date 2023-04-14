from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    matter = search_news(
        {
         'title': {
            '$regex': title,
            '$options': 'i',
         }
        }
    )
    list = []

    for reportage in matter:
        index = reportage['title'], reportage['url']
        list.append(index)

    return list


# Requisito 8
def search_by_date(date):
    try:
        matter = search_news(
            {
             'timestamp': datetime.fromisoformat(date).strftime('%d/%m/%Y')
            }
        )
        list = []

        for reportage in matter:
            index = reportage['title'], reportage['url']
            list.append(index)

        return list

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    matter = search_news(
        {
         'category': {
            '$regex': category,
            '$options': 'i',
         }
        }
    )
    list = []

    for reportage in matter:
        index = reportage['title'], reportage['url']
        list.append(index)

    return list
