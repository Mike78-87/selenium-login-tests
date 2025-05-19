import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password,expected_message", [
    ("admin", "password", "Успешно! Вход выполнен."),
    ("wronguser", "password", "Неверный логин или пароль"),
    ("admin", "wrongpass", "Неверный логин или пароль"),
])
def test_login(driver, username, password, expected_message):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.set_username(username)
    login_page.set_password(password)
    login_page.click_login()
    assert login_page.get_message() == expected_message
