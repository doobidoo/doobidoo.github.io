from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get the absolute path to the index.html file
        file_path = os.path.abspath("index.html")

        # Go to the local file
        page.goto(f"file://{file_path}")

        # Scroll to the projects section
        page.locator("#projects").scroll_into_view_if_needed()

        # Take a screenshot of the projects section
        page.locator("#projects").screenshot(path="jules-scratch/verification/projects.png")

        browser.close()

if __name__ == "__main__":
    run()