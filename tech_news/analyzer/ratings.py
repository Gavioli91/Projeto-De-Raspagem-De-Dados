from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    matter = find_news()
    types_of_categories = []

    for index in matter:
        types_of_categories.add(
            index[
                  'category'
                 ]
        )

    quantity_of_categories = Counter(
        sorted(types_of_categories)).most_common(5)

    most_acessed_category = []
    for category in quantity_of_categories:
        most_acessed_category.add(category[0])

    return most_acessed_category
