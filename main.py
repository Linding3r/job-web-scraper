import requests
import os
from bs4 import BeautifulSoup

criteria = input("Write job search criteria: ")

URL = "https://www.jobindex.dk/jobsoegning?q=" + criteria
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("div", class_="jobsearch-result")


with open("job_data.txt", "w", encoding="utf-8") as file:
    for result in results:
        title_element = result.find("h4").find("a") if result.find("h4") else None
        company_element = result.find("div", class_="jix-toolbar-top__company").find("a")
        location_element = result.find("div", class_="jobad-element-area").find("span") if result.find("div", class_="jobad-element-area") else None
        link_element = result.find("a", class_="btn btn-sm btn-primary")
        
        if title_element is not None and company_element is not None and location_element is not None:
            title = title_element.text.strip()
            company = company_element.text.strip()
            location = location_element.text.strip()
            job_URL = link_element.get("href")
            
            file.write(f"Title: {title}\n")
            file.write(f"Company: {company}\n")
            file.write(f"Location: {location}\n")
            file.write(f"Job URL: {job_URL}\n\n")

print("Job data has been written to job_data.txt")