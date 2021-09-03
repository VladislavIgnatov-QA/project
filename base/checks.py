from base.base import WebPage
from page.yandex_main_page import YandexPage
from conftest import web_browser


class Decorator(WebPage):
    def __init__(self, func, web_driver, url=''):
        self._web_driver = web_driver
        self.func = func
        self.web_browser = web_browser
        super().__init__(web_driver, url)

    def __call__(self):
        self.func()

#Как в декоратор засунуть действия функции, чтоб те выполнялись после запуска страницы
    def decorator_check_main_page(func):
        def decorated(web_browser, assert_number='Не та страница'):
            page = YandexPage(web_browser)
            func(web_browser)
            assert page.get_current_url() == 'https://yandex.ru/', assert_number
        return decorated