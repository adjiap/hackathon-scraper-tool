# UTF-8
"""
Original tutorial came from https://www.youtube.com/watch?v=XQgXKtPSzUI

@Author: Adji Arioputro

"""
import argparse
import datetime
from typing import List, Iterable
from bs4.element import ResultSet, Tag
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary  # Required import to give chromedriver PATH
import time
import pandas as pd
from collections import Counter

from selenium.common.exceptions import NoSuchElementException


def getArgs(argv=None):
    parser = argparse.ArgumentParser(description='Run Crawl Script to parse Hackathon.com website')
    parser.add_argument('-y', '--year', default=datetime.datetime.now().year,
                        help="Crawl for one particular year.")
    parser.add_argument('-c', '--country', default="germany",
                        help="Crawl for a particular country")
    argvars = vars(parser.parse_args())
    return argvars


def crawl_url(url: str) -> ResultSet(Tag):
    """
    This method uses Selenium WebDriver to run an automated Chrome Browser and crawl the page.
    This is required due to the Javascript in the Hackathon website which needs XHR requests
    to show all events in the year.

    Args:
        url:

    Returns:

    """
    # Use selenium WebDriver to run an automated Chrome Browser.
    # This is required due to the Javascript in the Hackathon website which needs XHR requests
    # to show all events in the year.
    driver = webdriver.Chrome()
    driver.get(url)
    # TODO: Use more efficient method for waiting.
    time.sleep(2)
    scroll_down(driver)
    try:
        more_button_xpath = "/html/body/div[6]/div[3]/div[3]/a"
        more_button = driver.find_element_by_xpath(more_button_xpath)
    except NoSuchElementException:
        more_button_xpath = "/html/body/div[6]/div[2]/div[3]/a"
        more_button = driver.find_element_by_xpath(more_button_xpath)
    while True:
        scroll_down(driver)
        # TODO: Use more efficient method for waiting
        time.sleep(0.7)
        # TODO: optimize Try-Except
        try:
            driver.find_element_by_xpath(more_button_xpath)
        except NoSuchElementException:
            break
        more_button.click()
    # Parse the read client by creating a BS4 object
    s_page = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    # container = s_page.findAll("div", {"class":"small-12 medium-6 large-12 column"})
    # We find the elements at the right side of the page
    container = s_page.find_all("div", {"class": ["ht-eb-card__right"]})
    # "row ht-idt-card__right__container"]})
    return container


def scroll_down(driver: webdriver.Chrome) -> None:
    """A method for scrolling the page.
    original code from https://stackoverflow.com/questions/48850974/
    selenium-scroll-to-end-of-page-indynamically-loading-webpage/48851166

    # HACK: Due to JavaScript issue where the More Button cannot be clicked unless seen on window

    Args:
        driver: The Web Driver to run Chrome

    """

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(1.5)
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def parse_keywords(container: ResultSet(Tag), year: int) -> Counter:
    """This method parses all the keywords that had shown up on the page.

    Args:
        year: year of the parsed url for dataframe.
        container: BeautifulSoup ResultSet with relevant Page Source to be processed

    Returns:
        A sorted Dataframe-Object with keywords and its descending number of occurrences.

    """
    keyword_list = []  # Type: str
    final_list = [] # Type: Any
    for tag in container:
        tag_link_list = tag.find_all("a", {"class": "ht-card-tag"})
        for tag_link in tag_link_list:
            keyword_list.append(tag_link.contents[0])
    for k,v in Counter(keyword_list).items():
        final_list.append([year, k, v])
    data_frame = pd.DataFrame(final_list, columns=["Year", "Tag", "Count"])
    return data_frame


def parse_cities(container: ResultSet(Tag), year: int) -> pd.DataFrame:
    """This method parses all the cities that had shown up on the page.

    Args:
        year: year of the parsed url for dataframe.
        container: BeautifulSoup ResultSet with relevant Page Source to be processed

    Returns:
        A sorted Dataframe-Object with city names and its descending number of occurrences.

    """
    keyword_list = []  # Type: str
    final_list = [] # Type: Any
    for tag in container:
        tag_link_list = tag.find_all("span", {"class": "ht-eb-card__location__place"})
        for tag_link in tag_link_list:
            keyword_list.append(tag_link.contents[0])
    for k,v in Counter(keyword_list).items():
        final_list.append([year, k, v])
    data_frame = pd.DataFrame(final_list, columns=["Year", "City", "Count"])
    return data_frame


def main():
    if args["year"]:
        final_year = args["year"]
    if args["country"]:
        country = args["country"]
    df_cities = pd.DataFrame()
    df_keywords = pd.DataFrame()
    for year in range(final_year - 5, final_year):
        main_url = f"https://www.hackathon.com/country/{country}/{year}"
        container = crawl_url(main_url)
        df_cities = df_cities.append(parse_cities(container, year), ignore_index=True)
        df_keywords = df_keywords.append(parse_keywords(container, year), ignore_index=True)
    df_cities.to_csv(r"C:/Temp/Cities.csv")
    df_keywords.to_csv(r"C:/Temp/Keywords.csv")


if __name__ == '__main__':
    args = getArgs()
    main()
