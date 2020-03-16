import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # нужно только для открытия страницы в нужном языке


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     # Открытие определенного браузера по умолчанию
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru", help="Choose language")


# Из командной строки можно выбрать браузер по переменной "--browser_names=..."
# Параметр --tb=line из командной строки позволяет сократить лог с результатами теста
# Параметр --reruns 1, где 1 - количество перезапусков. Устанавливается с помощью:
# pip install pytest-rerunfailures==7.0

@pytest.fixture(scope="session")
def browser(request):  # request нужен для выбора браузера и языка
    print("\nStart")
    br_name = request.config.getoption("--browser")
    user_language = request.config.getoption("language")
    if br_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif br_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError(f"--browser {br_name}, should be chrome or firefox")
    yield browser
    print("\nfinish")
    browser.quit()
