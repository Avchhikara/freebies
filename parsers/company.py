import re
from locators.company import CompanyLocator

class Company:
    def __init__(self, company):
        self.company = company

    def __repr__(self):
        return f"<{self.name}, {self.country}, {self.website}>"

    @property
    def website(self):
        locator = CompanyLocator.website
        website_element = self.company.select_one(locator)
        if website_element:
            website = re.findall("(?![www\.])[0-9a-zA-Z-]+[/.]+[a-zA-Z]{2,}", website_element.attrs["href"])
            return website[0]

    @property
    def country(self):
        locator = CompanyLocator.country
        country_element = self.company.select_one(locator)
        country_string = country_element.string
        if len(country_string) == 2:
            return "USA"
        return country_string

    @property
    def name(self):
        locator = CompanyLocator.name
        name_element = self.company.select_one(locator)
        return name_element.string
