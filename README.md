# Selenium Login Tests

Автоматизированные UI-тесты для [https://berpress.github.io/selenium-login-demo/](https://berpress.github.io/selenium-login-demo/) с использованием Python, Selenium и Pytest.

## Структура

- **pages/** — Page Object Model для страницы логина
- **tests/** — Тесты (1 позитивный, 2 негативных)
- **conftest.py** — фикстура pytest для WebDriver
- **requirements.txt** — зависимости

## Установка

1. Клонируй проект:
```bash
git clone https://your-repo-url
cd selenium_login_test
```

2. Установи зависимости:
```bash
pip install -r requirements.txt
```

3. Установи ChromeDriver, если ещё не установлен:
   - Скачать: https://chromedriver.chromium.org/downloads
   - Убедись, что он в PATH

## Запуск тестов

```bash
pytest
```

Для просмотра в браузере (удалить `--headless` в `conftest.py`):
```bash
pytest -s
```

## Пример вывода

```
tests/test_login.py::test_login[admin-password-успешно] PASSED
tests/test_login.py::test_login[wronguser-password-неверно] PASSED
tests/test_login.py::test_login[admin-wrongpass-неверно] PASSED
```
