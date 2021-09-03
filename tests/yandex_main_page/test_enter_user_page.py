import pytest
from page.yandex_main_page import YandexPage
from base.checks import Decorator


@Decorator.decorator_check_main_page
def test_authorisation(web_browser):
    page = YandexPage(web_browser)
    page.enter_in_user_page.click()
    page.enter_in_user_page.send_keys('Hello')

