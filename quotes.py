import csv
import requests
from bs4 import BeautifulSoup

data = [
    ["name", "salary", "skills"],
    ["Garima", 50000, "python"],
    ["Rahul", 30000, "api"]
]

with open("employee.csv", "w", newline ="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print ("csv saved")

with open("skill.csv", "w", newline = "")as file:
    writer = csv.writer(file)
    writer.writerows(data)
  
with open("employee.csv", "r") as file:
    reader =csv.reader(file) 
    for row in reader:
        print(row) 
