from base.base import WebPage
from base.elements import WebElement


class YandexPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://yandex.ru/'
        super().__init__(web_driver, url)

    enter_in_user_page = WebElement(xpath='//*[@id="text"]')
