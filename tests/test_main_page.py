import time
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(4)


# pytest -v --tb=line --language=en tests\test_main_page.py
# pytest --browser=firefox --language=es
# pytest --language=en
# pytest --browser=chrome --language=ru
# pytest --language=de
# pytest --language=fr

