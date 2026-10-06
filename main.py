from playwright.sync_api import sync_playwright, Error as PlaywrightError
import config


class Browser:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def launch(self):
        try:
            self.playwright = sync_playwright().start()

            if config.BROWSER == "chromium":
                self.browser = self.playwright.chromium.launch(
                    executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    headless=config.HEADLESS
                )
            elif config.BROWSER == "firefox":
                self.browser = self.playwright.firefox.launch(
                    headless=config.HEADLESS
                )
            elif config.BROWSER == "webkit":
                self.browser = self.playwright.webkit.launch(
                    headless=config.HEADLESS
                )
            else:
                raise ValueError("Invalid browser selected")

            self.context = self.browser.new_context(
                viewport={
                    "width": config.WINDOW_WIDTH,
                    "height": config.WINDOW_HEIGHT
                }
            )

            self.page = self.context.new_page()
            self.page.set_default_timeout(config.DEFAULT_TIMEOUT)

            print("Browser launched successfully.")

        except Exception as e:
            print("Browser launch failed:", e)

    def open_url(self, url):
        try:
            if not url.startswith(("http://", "https://")):
                raise ValueError("Invalid URL")

            self.page.goto(url, wait_until="load")

            print("URL opened successfully:", url)
            print("Title:", self.page.title())

        except ValueError as e:
            print("Invalid URL:", e)

        except PlaywrightError as e:
            print("Navigation failed:", e)

    def close(self):
        try:
            if self.context:
                self.context.close()

            if self.browser:
                self.browser.close()

            if self.playwright:
                self.playwright.stop()

            print("Browser closed successfully.")

        except Exception as e:
            print("Browser shutdown failed:", e)


browser = Browser()

try:
    browser.launch()
    browser.open_url(config.DEFAULT_URL)

finally:
    browser.close()
