---
title: Smartproxy Facebook Marketplace Scraper
description: Scraping Facebook Marketplace Vehicle Listings in Canada
authors: [harmindersinghnijjar]
tags: [Python, Web Scraping, Facebook Marketplace, Smartproxy]
toc: true
comments: true
---

# Advanced Python Scripting: Scraping and Storing Facebook Marketplace Vehicle Listings in Canada

## Introduction

In the realm of data collection and analysis, web scraping stands as a powerful tool to gather specific information from vast online sources. This blog post delves into a Python script I developed, focusing on scraping vehicle listings from Facebook Marketplace in Canadian cities and systematically storing the data in a SQL database. This tool exemplifies how Python's versatility can be harnessed for complex web scraping and data management tasks.

## The Concept

The script addresses a common challenge faced by many - accessing structured data from unstructured web sources like Facebook Marketplace. By automating the process of data extraction and storage, the script serves a variety of purposes, from market research to personal data aggregation.

## Technical Breakdown

### Core Technologies

- **Python**: A versatile programming language ideal for scripting and automation.
- **BeautifulSoup**: A Python library for parsing HTML and XML documents.
- **SQLite**: A lightweight, disk-based database that doesn't require a separate server process.
- **Asyncio**: Python’s built-in library for writing concurrent code using the async/await syntax.

### Script Structure

#### DatabaseManager Class

This class forms the backbone of the data storage mechanism, handling all interactions with the SQLite database. It ensures data integrity and efficient data handling.
```python
    class DatabaseManager:
        def __init__(self):
            self.conn = sqlite3.connect('market_listings.db')
            self.cursor = self.conn.cursor()
            self._prepare_database()

        def _prepare_database(self):
            """Create the database table if it does not exist."""
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS market_listings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    mileage REAL,
                    price REAL NOT NULL,
                    location TEXT NOT NULL,
                    url TEXT NOT NULL UNIQUE,
                    image TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            self.conn.commit()

        def listing_exists(self, url):
            self.cursor.execute("SELECT COUNT(1) FROM market_listings WHERE url = ?", (url,))
            return self.cursor.fetchone()[0] > 0

        def create_market_listing(self, title, mileage, price, location, url, image):
            if self.listing_exists(url):
                logger.info(f"Listing with URL {url} already exists. Skipping insert.")
                return None
            try:
                self.cursor.execute('''
                    INSERT INTO market_listings (title, mileage, price, location, url, image)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (title, mileage, price, location, url, image))
                self.conn.commit()
                return self.cursor.lastrowid
            except sqlite3.IntegrityError as e:
                logger.error(f"Unique constraint failed while inserting into database: {e}")
                return None
            except Exception as e:
                logger.error(f"An error occurred while inserting into database: {e}")
                return None

        def retrieve_all_listings(self):
            self.cursor.execute("SELECT * FROM market_listings")
            return self.cursor.fetchall()

        def close_connection(self):
            self.conn.close()

```

#### FacebookMarketplaceScraper Class

The scraper class is the script's workhorse, responsible for sending HTTP requests, parsing the received HTML, and extracting the necessary data from the Facebook Marketplace.
```python
    class FacebookMarketplaceScraper:
        def **init**(self, city, query, db_manager):
            self.city = city
            self.query = query
            self.db_manager = db_manager
    
        def scrape_city(self, city, query):
            """Scrape a single city."""
            url = "https://scraper-api.smartproxy.com/v2/scrape"
            logger.info(f"Scraping {city}.")
            payload = {
                "target": "universal",
                "locale": "en-US",
                "device_type": "desktop",
                "headless": "html",
                "url": f"https://www.facebook.com/marketplace/{city}/search/?query={query}&exact=false",
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": "YOUR_API_KEY",
            }
    
            logger.info(f"payload: {payload}")
            logger.info(f"headers: {headers}")
    
            response = requests.post(url, data=json.dumps(payload), headers=headers)
    
            # Get the enitre response
            logger.info(f"response.text: {response.text}")
            logger.info(f"response.status_code: {response.status_code}")
    
            # Get the JSON response
            json_response = response.json()
    
            if response.content == "null":
                logger.error(
                    f"Error while scraping: {response.status_code}, {response.text}"
                )
                return []
    
            try:
                json_response = response.json()
            except ValueError as e:
                logger.error(f"Error decoding JSON: {e}")
                return []
    
            listings_content = json_response.get("results", [])
            if not listings_content:
                logger.info("No results found in the response.")
                return []
    
            first_result_content = listings_content[0].get("content")
            if not first_result_content:
                logger.info("No content found in the first result.")
                return []
    
            soup = BeautifulSoup(first_result_content, "html.parser")
            soup_listings = soup.find_all(
                "div",
                class_="x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e x1iorvi4 xjkvuk6 xnpuxes x291uyu x1uepa24",
            )
    
            if not soup_listings:
                logger.info("No listings found in the parsed HTML.")
                return []
    
            logger.info(f"Found {len(soup_listings)} listings.")
            return soup_listings
    
        def parse_listings(self, soup_listings):
            new_listings = []  # Initialize an empty list to collect new listings
            for soup_listing in soup_listings:
                # Extract data from each listing
                try:
                    # Extract price using regex
                    price = self.extract_price(soup_listing)
    
                    # Extract mileage using regex
                    mileage = self.extract_mileage(soup_listing)
    
                    # Extract title
                    title = self.extract_title(soup_listing)
    
                    # Extract image URL
                    image = self.extract_image(soup_listing)
    
                    # Extract location
                    location = self.extract_location(soup_listing)
    
                    # Extract post URL
                    post_url = self.extract_post_url(soup_listing)
    
                    # Validate extracted data
                    if not self.is_valid_listing(title, price, location, post_url):
                        continue
                    
                    # Check if the listing already exists in the database
                    if self.db_manager.listing_exists(post_url):
                        continue
                    
                    # Add new listing to the database
                    listing_id = self.db_manager.create_market_listing(
                        title, mileage, price, location, post_url, image
                    )
                    if listing_id:
                        new_listings.append(
                            (title, mileage, price, location, post_url, image)
                        )
                except Exception as e:
                    logger.error(f"Error processing listing: {e}")
                    continue
            logger.info(f"Found {len(new_listings)} new listings.")
            return new_listings
    
        def extract_price(self, soup_listing):
            text = soup_listing.get_text(strip=True)
    
            # Match prices potentially followed by a year in the range 1950-2024
            price_match = re.search(r"(\$\d{1,3}(?:,\d{3})?)(?=(1950|19[6-9]\d|20[0-1]\d|202[0-4])?)", text)
            if price_match:
                return price_match.group(1)
    
            # If the above pattern does not match, fall back to the original patterns
            # Canadian dollar sign, without year
            price_match = re.search(r"(\$\d+,\d+)", text)
            if price_match:
                return price_match.group(1)
    
            # US dollar sign, without year
            price_match = re.search(r"(\$\d+)", text)
            if price_match:
                return price_match.group(1)
    
            return None
    
        def extract_mileage(self, soup_listing):
            mileage_match = re.search(r"(\d+K) km", soup_listing.get_text(strip=True))
            return mileage_match.group(1) if mileage_match else None
    
        def extract_title(self, soup_listing):
            title_elem = soup_listing.find(
                "span", class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6"
            )
            return title_elem.get_text(strip=True) if title_elem else None
    
        def extract_image(self, soup_listing):
            image_elem = soup_listing.find(
                "img", class_="xt7dq6l xl1xv1r x6ikm8r x10wlt62 xh8yej3"
            )
            return image_elem["src"] if image_elem else None
    
        def extract_location(self, soup_listing):
            # Extract location in the form of an Uppercase followed by Lowercase letters until a comma is found and than two uppercase letters
            location_match = re.search(
                r"([A-Z][a-z]+(?: [A-Z][a-z]+)*), [A-Z]{2}",
                soup_listing.get_text(strip=True),
            )
            location = location_match.group(1) if location_match else None
            return location
    
        def extract_post_url(self, soup_listing):
            url_elem = soup_listing.find(
                "a",
                class_="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu           x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1lku1pv",
            )
            return "https://www.facebook.com" + url_elem["href"] if url_elem else None
    
        def is_valid_listing(self, title, price, location, url):
            # Log why a listing is invalid if it is
            if not title or not price or not location or not url:
                missing_info = []
                if not title:
                    missing_info.append("title")
                if not price:
                    missing_info.append("price")
                if not location:
                    missing_info.append("location")
                if not url:
                    missing_info.append("url")
                # If all four are missing, go to the next listing without logging
                if len(missing_info) == 4:
                    pass
            # Check if the listing is valid
            is_valid = title and price and location and url
            if not is_valid:
                pass
            return is_valid
    
```

#### Asynchronous Operation

Utilizing asyncio, the script is capable of performing scraping operations at predetermined intervals, allowing for up-to-date data collection without manual intervention.
```python
    async def scrape_city_and_save_periodically(self, city, query, interval, duration):
        start_time = datetime.now()
        logger.info(f"Starting periodic scraping at {start_time}.")
        end_time = start_time + timedelta(hours=duration)
        logger.info(f"Periodic scraping will end at {end_time}.")
        while datetime.now() < end_time:
            try:
                # Scrape the city
                soup_listings = self.scrape_city(city, query)
                logger.info(f"Scraped {city} at {datetime.now()}.")
                logger.info(f"Scraped {len(soup_listings)} listings.")
                if not soup_listings:
                    logger.info("No listings found to process.")
                    continue
                # Parse the listings
                new_listings = self.parse_listings(soup_listings)
                if not new_listings:
                    logger.info("No new listings found to upload.")
                    continue
                logger.info(f"Found {len(new_listings)} new listings.")
                logger.info(f"new_listings: {new_listings}")
                # Upload the listings to SQL database
                for new_listing in new_listings:
                    title, mileage, price, location, url, image = new_listing
                    # Upload the listing to the database
                    listing_id = self.db_manager.create_market_listing(
                        title, mileage, price, location, url, image
                    )
                    if listing_id:
                        logger.info(f"Uploaded listing {listing_id} to database.")
                    else:
                        logger.error(f"Failed to upload listing {listing_id} to database.")
            except Exception as e:
                logger.error(f"Error while scraping: {e}")
                continue
            finally:
                # Wait for the specified interval
                await asyncio.sleep(interval)
```

### Deep Dive into Code

#### Setting Up Logging

Effective logging is crucial for monitoring the script's performance and debugging. The script is configured to log both to a file and the console, ensuring comprehensive tracking of events.
```python
    # Set up logging    
    logger = logging.getLogger(**name**)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("scraper.log")
    log_format = logging.Formatter(
    "%(asctime)s - %(name)s - [%(levelname)s] [%(pathname)s:%(lineno)d] - %(message)s - [%(process)d:%(thread)d]"
    )
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    logger.info("Logger initialized.")
```

#### Database Operations

The script initializes the database and defines a schema for storing listing data. It includes robust error handling and data validation to maintain database integrity.

```python
    # Initialize the database
    db_manager = DatabaseManager()
    logger.info("Database initialized.")

    # Create a table for storing market listings
    db_manager.create_market_listings_table()
    logger.info("Market listings table created.")

    # Retrieve all listings from the database
    listings = db_manager.retrieve_all_listings()
    logger.info(f"Retrieved {len(listings)} listings from the database.")
```



#### Data Scraping and Parsing

The script makes use of BeautifulSoup to parse HTML content fetched from Facebook Marketplace. It navigates the DOM structure to extract details such as title, price, and location of the vehicle listings.
```python
    # Scrape the city
    soup_listings = scraper.scrape_city(city, query)
    logger.info(f"Scraped {city} at {datetime.now()}.")
    logger.info(f"Scraped {len(soup_listings)} listings.")
    if not soup_listings:
        logger.info("No listings found to process.")
        continue
    # Parse the listings
    new_listings = scraper.parse_listings(soup_listings)
    if not new_listings:
        logger.info("No new listings found to upload.")
        continue
    logger.info(f"Found {len(new_listings)} new listings.")
    logger.info(f"new_listings: {new_listings}")
```

#### Handling Asynchronous Tasks

The script utilizes asyncio to perform scraping operations at predetermined intervals. This allows for up-to-date data collection without manual intervention.
```python
    # Scrape the city and save periodically
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        scraper.scrape_city_and_save_periodically(city, query, interval, duration)
    )
    loop.close()
```

## Usage Scenario

The script can be used to collect data for a variety of purposes, from market research to personal data aggregation. It can be adapted to scrape data from other Facebook Marketplace categories and locations.

## Challenges and Solutions

### Challenge: Scraping Dynamic Content

Facebook Marketplace is a dynamic website that loads content dynamically using JavaScript. This makes it difficult to scrape using traditional methods.

### Solution: Smartproxy

Smartproxy is a rotating residential proxy network that allows you to send requests from a pool of over 40 million residential proxies. This allows you to bypass anti-scraping measures and scrape dynamic content with ease.

### Challenge: Parsing HTML Content

The script uses BeautifulSoup to parse HTML content fetched from Facebook Marketplace. It navigates the DOM structure to extract details such as title, price, and location of the vehicle listings.

### Solution: Regular Expressions

Regular expressions are used to extract specific patterns from the HTML content. This allows for efficient and accurate data extraction.

### Challenge: Data Storage

The script uses SQLite to store the scraped data. It ensures data integrity and efficient data handling.

### Solution: DatabaseManager Class

The DatabaseManager class forms the backbone of the data storage mechanism, handling all interactions with the SQLite database. It ensures data integrity and efficient data handling.

## Future Enhancements

- **Scrape Other Categories**: The script can be adapted to scrape other categories of Facebook Marketplace, such as electronics and clothing.
- **Scrape Other Locations**: The script can be adapted to scrape other locations of Facebook Marketplace, such as the United States and the United Kingdom.
- **Scrape Other Platforms**: The script can be adapted to scrape other platforms, such as Kijiji and Craigslist.

## Conclusion

This Python script stands as a testament to the power of programming in automating and streamlining data collection processes. It is not just a tool but a framework that can be adapted to various other scraping needs, showcasing Python's flexibility and efficiency.

### GitHub Repository

For a detailed view of the code and to try it out, visit the [GitHub repository](https://github.com/harmindersinghnijjar/fb-marketplace-smartproxy-scraper).

### Disclaimer
This tool is designed for educational and research purposes. Users must comply with Facebook's terms of service and applicable laws when scraping data.

