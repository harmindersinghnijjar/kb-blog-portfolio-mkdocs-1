---
title: Unfollow Non-Followers on Instagram Using Instagrapi
description: Learn how to use Instagrapi to unfollow users who do not follow you back on Instagram.
authors: [Harminder Singh Nijjar]
date: 2023-11-04
tags: [Instagram, Instagrapi, Python, Social Media, Automation]
toc: true
robots: noindex, nofollow
hide: false
permalink: /projects/Social-media-automation/Instagram/Unfollowing-non-followers/Unfollowing_non-followers/


---
# Unfollow Non-Followers on Instagram Using Instagrapi

**Disclaimer**: Before proceeding, it's important to note that using unofficial APIs can lead to potential violations of Instagram's terms of service. Such actions may result in restrictions on your account, up to and including a permanent ban. The information provided here is for educational purposes, and I strongly advise against misusing it in any way.

## Introduction

In the world of Instagram, engagement and follower count are often seen as measures of popularity and influence. It's not uncommon for users to seek a balanced follower-to-following ratio. If you're looking to clean up your Instagram following list and unfollow users who do not follow you back, Instagrapi—a powerful, unofficial Instagram API wrapper for Python—can help automate this process.


## Code

### Install Instagrapi

First and foremost, Instagrapi needs to be installed in your Python environment. It can be installed easily using pip, Python's package installer. Simply run the following command in your terminal or command prompt:

```bash
pip install instagrapi
```

This command downloads and installs the Instagrapi library, making its functionality available for your Python scripts.

### Create an Instagrapi Client

To interact with Instagram, you must create an instance of the Instagrapi client. This is your gateway to performing API calls:

```python
from instagrapi import Client

client = Client()
```

This snippet imports the `Client` class from the Instagrapi package and instantiates it.

### Login to Instagram

Next, you'll need to authenticate with Instagram. Replace "username" and "password" with your actual Instagram credentials:

```python
client.login("username", "password")
```

The `login` method signs you into Instagram, allowing your script to act on your behalf. Remember to keep your credentials secure and never share them with anyone.

### Get Your Followers and Following

Now, retrieve the list of user IDs for both your followers and the accounts you follow:

```python
followers = client.user_followers(client.user_id)
following = client.user_following(client.user_id)
```

These methods return a dictionary of users who are your followers and users you are following, respectively.

### Identify Users to Unfollow

With both lists at your disposal, you can now identify which users you follow that do not follow you back:

```python
users_to_unfollow = [user for user in following if user not in followers]
```

This line of code uses a list comprehension to create a new list of user IDs that represents people you follow who aren't following you back.

### Unfollow Users

Once you have the list of non-followers, you can loop through it and unfollow each user:

```python
for user_to_unfollow in users_to_unfollow:
    client.user_unfollow(user_to_unfollow)
```

This loop calls the `user_unfollow` method for each user in the `users_to_unfollow` list, effectively cleaning up your following list.

### Logout (Optional)

After the script has completed its task, you may choose to log out of the client session:

```python
client.logout()
```

Logging out is a good practice to end the session, especially when running the script periodically.

## Conclusion

This script serves as a tool for managing your social media presence more effectively especially if you have a large following. It can be run periodically to keep your following list clean and balanced.


