from playwright.sync_api import Page


def test_TC1(page:Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()
    assert "Successfully" in page.content()