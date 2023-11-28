---
title: Transferring Script Files to Local System or VPS
description: This document outlines the process for transferring a Python script and setting it up on your local system. The script, in this case, is a Facebook Marketplace Scraper that allows you to collect and manage data from online listings.
authors: [harmindersinghnijjar]
date: 2023-11-27
tags: [Facebook Marketplace Scraper, Python, Google Sheets API, SQLite, Telegram Bot API, Smartproxy]
categories: [Facebook Marketplace Scraper, Python, Google Sheets API, SQLite, Telegram Bot API, Smartproxy]
toc: true
comments: true
---

# Transferring Script Files to Local System or VPS

## Local System Setup Process (Windows)

This document outlines the process for transferring a Python script and setting it up on your local system. The script, in this case, is a Facebook Marketplace Scraper that allows you to collect and manage data from online listings.

### Prerequisites

Before proceeding with the setup, ensure you have the following prerequisites ready:

- Python installed on your system (Python 3.6 or higher is recommended).
- Access to a Google Cloud project with required credentials for Google Sheets API.
- SQLite database support.
- A Telegram bot token (if you wish to receive notifications).
- Dependencies listed in the `requirements.txt` file provided with the script.

## Setup Steps

### Step 1: Obtain Script Files

1.1. Obtain the necessary script files from your source, typically provided as a ZIP archive or downloadable files.
1.2. Ensure you have the following script files:

- `fb_parser.py`: The main Python script.
- `requirements.txt`: A file containing the required Python dependencies.

### Step 2: Install Dependencies

2.1. Open a terminal/command prompt and navigate to the directory containing the script files.
2.2. Install the required Python dependencies using the following command:
```bash
pip install -r requirements.txt
```
This command installs packages such as `requests`, `beautifulsoup4`, and others.

### Step 3: Configure Credentials

3.1. Set up Google Cloud credentials for accessing the Google Sheets API:

- Create or use an existing Google Cloud project.
- Enable the Google Sheets API for your project.
- Create OAuth 2.0 credentials for a desktop application and download the `credentials.json` file.
- Place the `credentials.json` file in the same directory as the script.

### Step 4: Initialize the Database

4.1. Initialize the SQLite database by running the following command in the script's directory:
```bash
python fb_parser.py --initdb
```

This command creates the SQLite database file (`market_listings.db`) in the script's directory.

### Step 5: Configure Telegram Bot Token (Optional)

5.1. If you want to receive notifications via Telegram, edit the `fb_parser.py` script and update the `bot_token` and `bot_chat_id` variables with your own values.

### Step 6: Run the Scraper

6.1. Start the scraper by running the following command in the script's directory:
```bash
python fb_parser.py
```

The scraper will begin collecting data from Facebook Marketplace listings, and notifications will be sent if configured.

### Step 7: Monitor and Review

7.1. Monitor the script's output for any messages or errors.
7.2. Review the Google Sheets document to ensure that it's collecting data accurately.

### Step 8: Ongoing Management

8.1. Consider setting up automated scheduling, if required, to run the scraper at specific intervals.


# VPS Setup Process

## Overview

This document outlines the process for transferring a Python script and setting it up on your VPS (Virtual Private Server). The script, in this case, is a Facebook Marketplace Scraper designed to collect and manage data from online listings.

### Prerequisites

Before proceeding with the setup, ensure you have the following prerequisites ready:

1. **Access to a VPS**: You should have access to a VPS with administrative privileges. You can obtain VPS services from providers like AWS, DigitalOcean, or any other preferred hosting provider.

2. **Operating System**: The VPS should be running a compatible operating system, preferably a Linux distribution such as Ubuntu or CentOS.

3. **Python Installed**: Python 3.6 or higher should be installed on your VPS. You can check the installed Python version using the `python3 --version` command.

4. **Access to SSH**: Ensure you can access your VPS via SSH (Secure Shell) with a terminal or SSH client.

5. **Script Files**: Obtain the necessary script files for the Facebook Marketplace Scraper. These files are typically provided as a ZIP archive or downloadable files.

6. **Dependencies**: Review the script's documentation to identify and install any required Python dependencies.

## Setup Steps

### Step 1: Access Your VPS

- Log in to your VPS using SSH. You should have received SSH credentials from your hosting provider.
```bash
ssh username@hostname
```
Replace `username` with your VPS username and `your-vps-ip` with the actual IP address or hostname of your VPS.

### Step 2: Upload Script Files

- Transfer the necessary script files to your VPS. You can use secure file transfer methods like SCP or SFTP to upload files from your local machine to the VPS.

### Step 3: Install Python Dependencies

- Install the required Python dependencies on your VPS. Use the package manager appropriate for your Linux distribution. For example, on Ubuntu, you can use `apt-get`:
```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install -r requirements.txt
```
Replace `requirements.txt` with the actual filename containing the dependencies.

### Step 4: Configure Credentials

- Set up any necessary credentials for the script. This may include configuring API keys, OAuth tokens, or other authentication details required for your specific use case.

#### Google Sheets API

1. Go to the Google Cloud Console.
2. Create a new project if you don't have one.
3. In the project dashboard, navigate to "APIs & Services" > "Credentials."
4. Click on "Create credentials" and choose "OAuth client ID."
5. Configure the OAuth consent screen with the necessary details.
6. Select "Desktop App" as the application type.
7. Create the OAuth client ID.
8. Download the JSON credentials file (usually named credentials.json).

#### Telegram Bot API (Chat ID)

1. Message the parser bot on Telegram.
2. Navigate to the following URL in your browser:
```bash
https://api.telegram.org/bot<yourtoken>/getUpdates
```
Replace `<yourtoken>` with your bot's token.
3. Look for the "chat" object in the response. The "id" value is your chat ID.


### Step 5: Execute the Script

- Run the Python script on your VPS. Navigate to the directory where you uploaded the script files and execute it.
```bash
python3 fb_parser.py
```
Replace `fb_parser.py` with the actual filename of the script.

- Monitor the script's output for any messages or errors. Depending on your VPS setup, you may choose to run the script in the background using tools like `nohup` or within a screen session for detached operation.

### Step 6: Ongoing Management

- Consider setting up automated scheduling, if required, to run the scraper at specific intervals. You can use tools like `cron` for scheduling periodic tasks on your VPS.


## Conclusion
Transferring script files to your local system or VPS to set up a Facebook Marketplace Scraper is a straightforward process. By following the steps outlined in this document, you can quickly get started with the scraper and begin collecting data from online listings.

## References
- [Facebook Marketplace Scraper](https://github.com/passivebot/facebook-marketplace-scraper)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [SQLite](https://www.sqlite.org/index.html)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Python](https://www.python.org/)
- [Smartproxy](dashboard.smartproxy.com/register?referral_code=d046100a8046fb2848f5d458bd1124de8d30d5f9)













