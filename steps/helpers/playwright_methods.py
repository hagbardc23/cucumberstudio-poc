import time

from playwright.sync_api import sync_playwright, Page, Browser


def page_by_title(browser: Browser, title: str) -> Page:
    for context in browser.contexts:
        for page in context.pages:
            if title in page.title():
                return page
    return None

def login(context, username, password):
    browser = context['browser']
    page = browser.new_page()
    page.goto("https://www.d.sma.bmshub.de")
    login_button = page.locator("button:has-text('Login'):nth-of-type(1)")
    login_button.wait_for(timeout=10000)
    login_button.click()
    popup: Page = page_by_title(browser, "Sign up or sign in")
    # Wait for the popup to open
    i_count = 0
    while popup is None and i_count < 5:
        time.sleep(1)
        popup = page_by_title(browser, "Sign up or sign in")
        i_count += 1
        pass
    if popup is None:
        raise Exception("Popup did not open")
    # Now the popup is open, handle the login
    popup.locator("button:has-text('Sign in')").wait_for(timeout=10000)
    popup.fill("#email", username)
    popup.fill("#password", password)
    popup.click("button:has-text('Sign in')")
    page = page_by_title(browser, "Vite App")
    page.locator("nav").get_by_text("logout").wait_for(timeout=10000, state="attached")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        context = {}
        context['browser'] = playwright.chromium.launch(headless=False, slow_mo=500)
        login(context, "email.michaeladler+smad1@gmail.com", "Passwort_01!")
