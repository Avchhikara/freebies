import requests

from pages.companies_list import CompanyList

it_services = requests.get("https://clutch.co/web-developers")


companies = CompanyList(it_services.content).companies
# print(len(companies))
for company in companies:
    print(company)
