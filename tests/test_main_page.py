import time
from pages.main_page import MainPage
import pytest


lnk = "http://selenium1py.pythonanywhere.com/"
lnk2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"


# @pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = lnk2
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор
                                     # экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    # time.sleep(2)


def test_guest_should_see_login_link(browser):
    link = lnk2
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()





# pytest -v --tb=line --language=en tests\test_main_page.py
# pytest --browser=firefox --language=es
# pytest --language=en
# pytest --browser=chrome --language=ru -v --tb=line
# pytest --language=de
# pytest --language=fr

