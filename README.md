# quote-scraper-project
Beginner Python web scraping project using BeautifulSoup


from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com")
    page.click("text=Login")
    page.fill('input[name = "username"]', "garima")
    page.fill('input[name = "password"]', "12345")
    page.click('input[type = "submit"]')
    page.wait_for_timeout(3000)
    
    page.wait_for_selector(".flash-error")
    error = page.locator(".flash-error").text_content()
    print(error)
    browser.close()