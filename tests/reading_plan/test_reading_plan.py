from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import MagicMock
import pytest


news_mock = (
        'https://blog.betrybe.com/novidades/noticia-bacana',
        'Notícia bacana',
        '04/04/2021',
        'Eu',
        4,
        'Algo muito bacana aconteceu',
        'Ferramentas',
),
(
        'https://blog.betrybe.com/novidades/noticia-longa-demais',
        'Notícia longa',
        '07/02/2022',
        'Eles',
        80,
        'Política financeira',
        'Economia',
)

mock_response = {
    'readable': [
        {
            'unfilled_time': 1,
            'chosen_news': [('Notícia bacana', 4)],
        }
    ],
    'unreadable': [('Notícia longa', 80)],
}


def test_reading_plan_group_news():
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(False)

    ReadingPlanService._db_news_proxy = MagicMock(return_value=news_mock)

    answer = ReadingPlanService.group_news_for_available_time(15)

    assert len(answer['readable']) == 1
    assert answer['readable'][0]['unfilled_time'] == 12
    assert len(answer['unreadable']) == 1
