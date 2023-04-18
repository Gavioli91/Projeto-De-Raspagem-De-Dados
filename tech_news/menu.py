from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category
)
from tech_news.analyzer.ratings import top_5_categories
import sys


# Requisitos 11 e 12
def analyzer_menu():
    options = input(
                 'Selecione uma das opções a seguir:\n'
                 ' 0 - Popular o banco com notícias;\n'
                 ' 1 - Buscar notícias por título;\n'
                 ' 2 - Buscar notícias por data;\n'
                 ' 3 - Buscar notícias por categoria;\n'
                 ' 4 - Listar top 5 categorias;\n'
                 ' 5 - Sair.'
    )

    match options:
        case '0':
            menu = input('Digite quantas notícias serão buscadas: ')
            get_tech_news(int(menu))
        case '1':
            menu = input('Digite o título: ')
            search_by_title(menu)
        case '2':
            menu = input('Digite a data no formato aaaa-mm-dd: ')
            search_by_date(menu)
        case '3':
            menu = input('Digite a categoria: ')
            search_by_category(menu)
        case '4':
            top_5_categories()
        case '5':
            print('Encerrando script')
        case _:
            sys.stderr.write('Opção inválida\n')
