import json
    
    
    
    
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com")
    quotes = page.locator(".quote")
    count = quotes.count()
    print(count)
    
    all_quotes =[]
    
    while True:
        quotes = page.locator(".quote")
        count = quotes.count()
    
        for i in range(count):
            quote = quotes.nth(i)
            quote_text = quote.locator(".text").text_content()
            author = quote.locator(".author").text_content()
            
            print(f"{quote_text} - {author}")
            
            all_quotes.append({"quotes":quote_text, "author": author})
        
        next_button  = page.locator(".next a")
        if next_button.count()>0:
            next_button.click()
            page.wait_for_timeout(2000)
            
            print(count)
            
        else:
            break
        
        with open("quotes.json", "w") as file:
            json.dump(all_quotes, file, indent=4)
        
        browser.close()      
        