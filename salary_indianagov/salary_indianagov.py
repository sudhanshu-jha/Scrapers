from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import pandas as pd

salary_df = pd.DataFrame()
driver = webdriver.Firefox()
driver.get("http://www.in.gov/apps/gov/salaries/search")
time.sleep(5)


agency = Select(driver.find_element_by_name("agency"))
agency.select_by_visible_text("INSURANCE")


search = driver.find_element_by_xpath('//*[@id="searchTable"]/tbody/tr[4]/td[2]/input')
search.click()
time.sleep(5)

while True:
    try:
        html_source = driver.page_source
        salaryinfo = BeautifulSoup(html_source, "lxml")
        salary_table = salaryinfo.findAll("table")
        salary_rows = salary_table[1].findAll(lambda tag: tag.name == "tr")
        salary_rows.pop(0)

        for i in salary_rows:
            employee = i.findAll("td")
            firstname = employee[0].text
            lastname = employee[1].text
            agency = employee[2].text
            status = employee[3].text
            salary = employee[4].text

            salary_df = salary_df.append(
                {
                    "FirstName": firstname,
                    "LastName": lastname,
                    "Agency": agency,
                    "Status": status,
                    "Salary": salary,
                },
                ignore_index=True,
            )
        nextlist = driver.find_element_by_class_name("nextLink")
        nextlist.click()
        time.sleep(5)
    except Exception as e:
        if "Unable to locate element" in str(e):
            salary_df.to_csv("salaries.csv", index=False)
            print("Wrote data to salaries.csv")
        else:
            print("Error")
        break
