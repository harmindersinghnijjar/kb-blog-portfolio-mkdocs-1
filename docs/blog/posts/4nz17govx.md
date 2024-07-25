---
title: Downloading Teri Meri Doriyaann using Python and BeautifulSoup
description: A step-by-step guide to downloading the latest Teri Meri Doriyaann episode using Python and BeautifulSoup.
authors: [harmindersinghnijjar]
date: 2023-12-31
tags: [Python, BeautifulSoup, Teri Meri Doriyaann, Hindi Serials, Star Network]
categories: [Python, BeautifulSoup]
toc: true
comments: true
---

# Downloading Teri Meri Doriyaann using Python and BeautifulSoup

![Teri Meri Dooriyann](https://www.desi-serials.cc/wp-content/uploads/2023/03/Teri-Meri-Dooriyann-300x169.jpg)

## Overview

In today's streaming-dominated era, accessing specific international content like the Hindi serial "Teri Meri Doriyaann" can be challenging due to regional restrictions or subscription barriers. This blog delves into a Python-based solution to download episodes of "Teri Meri Doriyaann" from a website using BeautifulSoup and Selenium.

## Disclaimer

**Important Note**: This tutorial is intended for educational purposes only. Downloading copyrighted material without the necessary authorization is illegal and violates many websites' terms of service. Please ensure you comply with all applicable laws and terms of service.

## Prerequisites

- A working knowledge of Python.
- Python environment set up on your machine.
- Basic understanding of HTML structures and web scraping concepts.

## Setting Up the Scraper

The script provided utilizes Python with the Selenium package for browser automation and BeautifulSoup for parsing HTML. Here’s a step-by-step breakdown:

### Setup Logging

The first step involves setting up logging to monitor the script's execution and troubleshoot any issues.

```python
import logging
# Setup Logging

def setup_logger():
logger = logging.getLogger(**name**)
logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("teri-meri-doriyaann-downloader.log", mode="a")
    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - [%(levelname)s] [%(pathname)s:%(lineno)d] - %(message)s - [%(process)d:%(thread)d]"
    )
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()

```

### Selenium Automation Class

Selenium simulates browser interactions. The `SeleniumAutomation` class contains methods for opening web pages, extracting video links, and managing browser tasks.

```python
from selenium import webdriver
    
    # Selenium Automation

    class SeleniumAutomation:
    def **init**(self, driver):
    self.driver = driver

        def open_target_page(self, url):
            self.driver.get(url)
            time.sleep(5)

    
```

### Extracting Video Links

The `extract_video_links` method in the `SeleniumAutomation` class is crucial. It navigates web pages and extracts video URLs.

```python
    def extract_video_links(self):
        results = {"videos": []}
        try: # Current date in the desired format DD-Month-YYYY
        current_date = datetime.datetime.now().strftime("%d-%B-%Y")

                    link_selector = f'//*[@id="content"]/div[5]/article[1]/div[2]/span/h2/a'
                    if WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, link_selector))
                    ):
                        self.driver.find_element(By.XPATH, link_selector).click()
                        time.sleep(30)  # Adjust the timing as needed

                        first_video_player = "/html/body/div[1]/div[2]/div/div/div[1]/div/article/div[3]/center/div/p[14]/a"
                        second_video_player = "/html/body/div[1]/div[2]/div/div/div[1]/div/article/div[3]/center/div/p[12]/a"

                        for player in [first_video_player, second_video_player]:
                            if WebDriverWait(self.driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, player))
                            ):
                                self.driver.find_element(By.XPATH, player).click()
                                time.sleep(10)  # Adjust the timing as needed
                                # Switch to the new tab that contains the video player
                                self.driver.switch_to.window(self.driver.window_handles[1])
                                elements = self.driver.find_elements(By.CSS_SELECTOR, "*")
                                for element in elements:
                                    if element.tag_name == "iframe" and element.get_attribute("src"):
                                        logger.info(f"Element: {element.get_attribute('outerHTML')}")
                                        try:
                                            video_url = element.get_attribute("src")
                                        except Exception as e:
                                            logger.error(f"Error getting video URL: {e}")
                                            continue
                                        
                                        self.driver.get(video_url)
                                        elements = self.driver.find_elements(By.CSS_SELECTOR, "*")
                                        for element in elements:
                                            if element.tag_name == "video" and element.get_attribute("src") and element.get_attribute("src").endswith(".mp4"):
                                                logger.info(f"Element: {element.get_attribute('outerHTML')}")
                                                try:
                                                    video_url = element.get_attribute("src")
                                                except Exception as e:
                                                    logger.error(f"Error getting video URL: {e}")
                                                    continue
                                                
                                                logger.info(f"Video URL: {video_url}")
                                                response = requests.get(video_url, stream=True)
                                                with open(f"E:\\Plex\\Teri Meri Doriyaann\\{datetime.datetime.now().strftime('%m-%d-%Y')}.mp4", "wb") as f:
                                                    for chunk in response.iter_content(chunk_size=1024*1024):
                                                        logger.info(f"Writing chunk {chunk}")
                                                        if chunk:
                                                            f.write(chunk)
                                                            logger.info(f"Chunk {chunk} written")
                                                            break
                                                        
                except Exception as e:
                    logger.error(f"Error in extract_video_links: {e}")

            def close_browser(self):
                self.driver.quit()

```

### Video Scraper Class

`VideoScraper` manages the scraping process, from initializing the web driver to saving the extracted video links.

```python
    # Video Scraper
    class VideoScraper:
    def **init**(self):
    self.user = os.getlogin()
    self.selenium = None

        def setup_driver(self):
            # Set up ChromeDriver service
            service = Service()
            options = webdriver.ChromeOptions()
            options.add_argument(f"--user-data-dir=C:\\Users\\{self.user}\\AppData\\Local\\Google\\Chrome\\User Data")
            options.add_argument("--profile-directory=Default")
            return webdriver.Chrome(service=service, options=options)

        def start_scraping(self):
            try:
                self.selenium = SeleniumAutomation(self.setup_driver())
                self.selenium.open_target_page("https://www.desi-serials.cc/watch-online/star-plus/teri-meri-doriyaann/")
                videos = self.selenium.extract_video_links()
                self.save_videos(videos)
            finally:
                if self.selenium:
                    self.selenium.close_browser()

        def save_videos(self, videos):
            with open("desi_serials_videos.json", "w", encoding="utf-8") as file:
                json.dump(videos, file, ensure_ascii=False, indent=4)

```


### Running the Scraper

The script execution brings together all the components of the scraping process.

```python
    if **name** == "**main**":
        os.system("taskkill /im chrome.exe /f")
        scraper = VideoScraper()
        scraper.start_scraping()

```


## Conclusion

This script demonstrates using Python's web scraping capabilities for specific content access. It highlights the use of Selenium for browser automation and BeautifulSoup for HTML parsing. While focused on a specific TV show, the methodology is adaptable for various web scraping tasks.

Use such scripts responsibly and within legal and ethical boundaries. Happy scraping and coding!

### References

- [GitHub Repository](https://github.com/harmindersinghnijjar/teri-meri-doriyaann-downloader)




