from bs4 import BeautifulSoup
import re

from locators.companies import CompaniesLocator
from parsers.company import Company


class CompanyList:
    def __init__(self, html_page):
        self.soup = BeautifulSoup(html_page, "html.parser")

    @property
    def companies(self):
        locator = CompaniesLocator.group
        company_list = self.soup.select(locator)
        return [Company(c) for c in company_list]

    @property
    def page_len(self):
        locator = CompaniesLocator.len
        len_element = self.soup.select_one(locator)
        max_pages = re.findall("[0-9]+$", len_element.attrs["href"])
        return int(max_pages[0])
