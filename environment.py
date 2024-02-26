from playwright.sync_api import sync_playwright
import os
import shutil

# Global Playwright instance
playwright = None

# Path to the screenshot folder
screenshot_folder = 'reports/playwright/screenshots'
trace_folder = 'reports/playwright/traces'


def before_all(context):
    # Check if the screenshot folder exists
    if os.path.exists(screenshot_folder):
        # Delete the screenshot folder
        shutil.rmtree(screenshot_folder)

    if os.path.exists(trace_folder):
        # Delete the screenshot folder
        shutil.rmtree(trace_folder)

    global playwright
    playwright = sync_playwright().start()


def before_scenario(context, scenario):
    # setup base URL
    context.base_url = os.getenv('BASE_URL', 'https://dev.smartagency.bmshub.de')

    # determine if the test should run headless
    headless = os.getenv('HEADLESS_MODE', 'True').lower() == 'true'

    # Initialize the browser and browser context
    context.browser = playwright.chromium.launch(headless=headless)
    context.browser_context = context.browser.new_context()

    # Create a new page in the browser context
    context.page = context.browser_context.new_page()

    # Set default timeout and start tracing
    context.page.set_default_timeout(10 * 1000)
    context.page.context.tracing.start(screenshots=True, snapshots=True)

    # Navigate to the base URL and click the 'Starten' button
    context.page.goto(context.base_url)
    context.page.evaluate(f"sessionStorage.setItem('isAuthenticated', 'true')")
    context.page.reload()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        # Capture and log the error details
        print(f"Test Failed: {scenario.name}")

        # Take a screenshot
        os.makedirs(screenshot_folder, exist_ok=True)
        screenshot_file = os.path.join(screenshot_folder, f"{scenario.name.replace(' ', '_')}_failure.png")
        context.page.screenshot(path=screenshot_file)

        # Optionally, capture Playwright trace
        os.makedirs(trace_folder, exist_ok=True)
        trace_file = os.path.join(trace_folder, f"{scenario.name.replace(' ', '_')}_failure.zip")
        context.page.context.tracing.stop(path=trace_file)

    # Close the browser after each scenario
    if context.browser:
        context.browser.close()


def after_all(context):
    if playwright:
        playwright.stop()
