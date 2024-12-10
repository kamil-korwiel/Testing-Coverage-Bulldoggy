from playwright.sync_api import Page, expect

def test_title_login_page(page: Page):
    page.goto("http://127.0.0.1:8000/login")
    expect(page).to_have_title("Login | Bulldoggy reminders app")