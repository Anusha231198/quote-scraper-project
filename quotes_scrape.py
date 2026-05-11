import requests
from bs4 import BeautifulSoup
import json

response = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div" , class_= "quote" )

all_quotes =[]

for quote in quotes:
    quote_text = quote.find("span", class_= "text" ).text 
    author = quote.find("small",class_ = "author").text 
    print(f"{quote_text} - {author}")
    
    all_quotes.append({quote_text: author})
    
with open("quotes.json", "w") as file:
    json.dump(all_quotes, file)