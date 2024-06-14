import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help='Choose language')


# Фикстура для запуска браузера в зависимости от языка
@pytest.fixture(scope="function")
def browser(request):
    print("\n==================== START CHROME BROWSER FOR TEST.. ====================")
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\n==================== QUIT BROWSER.. ====================")
    browser.quit()
