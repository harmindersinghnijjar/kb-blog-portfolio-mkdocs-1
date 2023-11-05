---
title: Downloading Media
description: Learn how to download all media from a specific Instagram profile along with captions and hashtags, then store this data in a SQLite database.
authors: [Harminder Singh Nijjar]
date: 2023-11-05
tags: [Instagram, Instagrapi, Python, Social Media, Automation]
toc: true
robots: noindex, nofollow
hide: false
permalink: /projects/Social-media-automation/Instagram/Downloading-Media/
---
# Downloading Media

## Introduction

In this tutorial, we will be covering how to download all media from a specific Instagram profile along with captions and hashtags, then store this data in a SQLite database. This will allow us to store the data we scrape from Instagram to later be uploaded to Truth Social. We will be using the following tools:

- [Instagrapi](https://subzeroid.github.io/instagrapi/)
- [SQLite](https://docs.python.org/3/library/sqlite3.html)
### Project Description

Due to the recent actions of mainstream technology giants against figures like Alex Jones and then-President Donald Trump, alternative digital ecosystems have grown in popularity. Platforms like Truth Social endorse unrestricted speech, attracting users looking for alternatives to the mainstream. By utilizing tools like Instagrapi and SQLite, we can store the data we scrape from Instagram to later be uploaded to Truth Social. 

#### Project Objectives

- [x] Download, at minimum, 100 media from a specific Instagram profile along with captions and hashtags, then store this data in a SQLite database.

#### Deadline

- [x] Achieve the project goals by 2023-10-13.

## Choosing a Platform

### Truth Social

<script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/3461_RC01/embed_loader.js"></script> <script type="text/javascript"> trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"Truth Social","geo":"US","time":"today 12-m"},{"keyword":"Parler","geo":"US","time":"today 12-m"},{"keyword":"Gettr","geo":"US","time":"today 12-m"},{"keyword":"Gab","geo":"US","time":"today 12-m"}],"category":0,"property":""}, {"exploreQuery":"geo=US&q=Truth%20Social,Parler,Gettr,Gab&hl=en&date=today 12-m,today 12-m,today 12-m,today 12-m","guestPath":"https://trends.google.com:443/trends/embed/"}); </script><script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/3461_RC01/embed_loader.js"></script>

Based on the Google Trends data, Truth Social currently leads in popularity among alternative platforms. This indicates a potentially large user base, making it the ideal choice for profile replication.

## Selecting a Profile to Replicate
### Nicole Wolf
Our initial step involves the careful selection of a profile to replicate. In the context of this tutorial, we have chosen to replicate the profile of a well-known Instagram influencer, Nicole Wolf, a professional web developer and dancer, known as @joeel56. With over 176,000 followers and a public profile, Nicole's online presence is significant. Given that her German background aligns with the demographics of Truth Social, this profile is ideal for replication.

![@Joeel56](chrome_sv2FM6ThyT.png)



## Creating a SQLite Database
### Installation
SQLite is a relational database management system that is embedded into the Python programming language. This database management system is well-documented and can be accessed [here](https://docs.python.org/3/library/sqlite3.html). We will be using this database management system to store the data we scrape from Instagram. The following sections will outline the steps required to create a SQLite database.

Install the "sqlite3" library if you haven't already. You can install it using pip:
    
```python
pip install sqlite3
```

### Database Initialization
After installing the "sqlite3" library, we will need to create a SQLite database. This database will store the data we scrape from Instagram. To create a SQLite database, we will need to import the `sqlite3` library. We will then need to initialize a connection to this database. This will create a SQLite database that we can use to store the data we scrape from Instagram.

```python
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect("instagram_data.db")
```

### Creating a Table for Media Data
After creating a SQLite database, we will need to create a table in this database. This table will store the data we scrape from Instagram. To create a table in a SQLite database, we will need to create a cursor object. We will then need to execute a SQL query to create a table in our SQLite database. This will create a table in our SQLite database that we can use to store the data we scrape from Instagram.

```python
# Define cursor

cursor = conn.cursor()

# Establish a table structure

cursor.execute('''
CREATE TABLE IF NOT EXISTS media_data (
id INTEGER PRIMARY KEY,
media BLOB NOT NULL,
caption TEXT,
hashtags TEXT
)
''')

# Commit changes and close connection

conn.commit()
conn.close()
```

## Replicating an Instagram Profile with Instagrapi
### Instagrapi Installation
Instagrapi is a Python library that can be used to programmatically interact with Instagram. This library is well-documented and can be accessed [here](https://subzeroid.github.io/instagrapi/). We will be using this library to replicate our Instagram profile. The following sections will outline the steps required to replicate our Instagram profile.

Install the "instagrapi" library if you haven't already. You can install it using pip:
    
```python
pip install instagrapi
```
### Creating an Instagram Session
To download all media from a specific Instagram profile along with captions and hashtags, then store this data in a Notion database, we will first need to create an Instagram session. This session will allow us to programmatically interact with Instagram. To create an Instagram session, we will need to import the `Client` class from the `instagrapi` library. We will then need to create an instance of this class and pass in our Instagram username and password. This will create an Instagram session that we can use to programmatically interact with Instagram.

```python
from instagrapi import Client

# Initialize the client
client = Client()
```

### Authenticating an Instagram Session
After creating an Instagram session, we will need to authenticate this session. This will allow us to programmatically interact with Instagram. To authenticate an Instagram session, we will need to call the `login` method on our Instagram session and pass in our Instagram username and password. This will authenticate our Instagram session and allow us to programmatically interact with Instagram.

```python
# Authenticate the client
client.login("username", "password")
```

### Downloading Media from an Instagram Profile
After downloading all media from a specific Instagram profile, we will need to store this data in a SQLite database. This will allow us to store the data we scrape from Instagram. To store this data in a SQLite database, we will need to create a connection to our SQLite database. We will then need to create a cursor object. We will then need to execute a SQL query to insert this data into our SQLite database. This will store this data in our SQLite database and allow us to store the data we scrape from Instagram.

```python
def download_media_from_profile(username, max_count=100):
    user_info = cl.user_info_by_username(username)
    user_id = user_info.pk
    # Get the user's media
    medias = cl.user_medias(user_id, amount=max_count)
    for media in medias:
        media_id = media.pk
        caption = media.caption_text  # Get the caption
        hashtags = [tag.strip("#") for tag in caption.split() if tag.startswith("#")]  # Extract hashtags
        hashtags = ", ".join(hashtags)  # Convert hashtags to a string
        # Initialize media_blob as None to handle unexpected media types
        media_blob = None
        # Download the media (photo or video) and convert it to binary
        if media.media_type == 1:  # Photo
            path = cl.photo_download(media_id, folder=f"{os.getcwd()}")
            media_blob = convert_to_binary(path)
        elif media.media_type == 2:  # Video
            path = cl.video_download(media_id, folder=f"{os.getcwd()}")
            media_blob = convert_to_binary(path)
        # Check if the media_blob is already in the database
        cursor.execute("SELECT id FROM media_data WHERE media = ?", (media_blob,))
        existing_media = cursor.fetchone()
        # If the media doesn't exist in the database, insert it
        if not existing_media and media_blob:
            cursor.execute("INSERT INTO media_data (media, caption, hashtags) VALUES (?, ?, ?)", (media_blob, caption, hashtags))
            conn.commit()
            # Optionally, remove the downloaded file to save space
            os.remove(path)
            logger.info(f"Downloaded media with caption: {caption}")
            logger.info(f"Hashtags: {hashtags}\n")
        elif existing_media:
            logger.info(f"Media already exists in the database. Skipping download for media with caption: {caption}")
```

### Closing an Instagram Session
After downloading all media from a specific Instagram profile, we will need to close this Instagram session. This will allow us to store the data we scrape from Instagram. To close an Instagram session, we will need to call the `logout` method on our Instagram session. This will close our Instagram session and allow us to store the data we scrape from Instagram.

```python
# Close the client
client.logout()
```
## Conclusion
![](chrome_esWANpqp9C.png)

By following the above steps, one can efficiently download all media from a specific Instagram profile along with captions and hashtags, then store this data in a SQLite database. This will allow one to store the data we scrape from Instagram to later be uploaded to Truth Social. 


