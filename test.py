print("Script started")

from playwright.sync_api import sync_playwright

print("Playwright imported")

with sync_playwright() as p:
    print("Playwright started")

    browser = p.chromium.launch(
        executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        headless=False
    )

    print("Chrome launched")

    page = browser.new_page()
    page.goto("https://example.com", timeout=30000)

    print("Title:", page.title())

    input("Press Enter to close Chrome...")
    browser.close()