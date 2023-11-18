---
title: Dub with ElevenLabs Google Chrome Extension
description: Dub with ElevenLabs Google Chrome Extension to easily dub YouTube videos with a single click.
authors: [harmindersinghnijjar]
date: 2023-11-07
tags: [ElevenLabs, Dubbing, AI, Chrome Extension, YouTube]
categories: [ElevenLabs, Dubbing, AI, Chrome Extension, YouTube]
comments: true

---

# Dub with ElevenLabs Google Chrome Extension

At [Passivebot](https://github.com/passivebot), we’re always looking for better and more efficient ways to improve user experience. In line with this goal, we are excited to get working on our latest project: Dub with <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a> Google Chrome Extension. This extension streamlines the experience of viewing dubbed content on YouTube by allowing users to easily switch between dubbed and original audio tracks with a single click.

## Dubbing

Dubbing is a new technology but it is rapidly gaining traction and has already been used to create episodes of popular anime shows like Attack on Titan, [My Hero Academia](https://www.crunchyroll.com/series/G6NQ5DWZ6/my-hero-academia), and Boku no Hero Academia. It is the process of replacing one language with another in a movie or TV series. From Hollywood movies released in multiple languages to Japanese anime dubbed in Spanish, dubbing is now commonplace among content streaming services.

Dubbing has now become even more accessible thanks to AI dubbing, a technology developed by <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a>. AI dubbing makes it easier for content creators to offer their work in multiple languages by leveraging the power of artificial intelligence. It ensures that the original speaker's voice characteristics are preserved, which is especially important with dubbed content like film and anime.


## Dub with ElevenLabs

Without an official release of a Dubbing API by <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a>, Passivebot independently developed a Chrome extension named "Dub with "<a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a> ." This tool facilitates the viewing of AI-dubbed content on YouTube, targeting content-creators who have not yet adopted AI dubbing technology. It simplifies the process for users to experience dubbed video content.

Requirements:

- [ ] Allow users to watch dubbed content on YouTube with a single click

The extension will need to simplify the process of having to enter the YouTube link of the video on <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a> to a single click.

We intend to do this by running a background script that will automatically detect if the user is on a YouTube video page. If the user is on a YouTube video page, the extension will display a button that will allow the user to automatically input the YouTube link of the video into the <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a> AI dubbing tool, wait for the video to be dubbed, and then switch the video to the dubbed version by changing the video stream to the link of the dubbed video.


### Design
 
Originally, textension will be designed to be as simple as possible. It will have a single button that will allow the user perform the following actions:

- [x] Automatically input the YouTube link of the video into the <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a> AI dubbing tool
- [ ] Wait for the video to be dubbed
- [ ] Switch the video to the dubbed version by changing the video stream to the link of the dubbed video


### Implementation

We will be using the following technologies to implement the extension:

1. [x] JavaScript
2. [ ] HTML
3. [ ] CSS


### Progress

#### 2023-11-10 12:52 

I've created a [repository](https://github.com/passivebot/dub-with-elevenlabs/) for the project and added the following files:<br>
1. `manifest.json`: This file contains the metadata for the extension along with what files to load and what permissions to request.<br>
2. `background.js`: This file contains the background script that will run in the background and detect if the user is on a YouTube video page.<br>
3. `content.js`: This file contains the content script that will run on the YouTube video page and display the button to the user.<br>


I've been able to successfully load the extension in developer mode and have the background script detect if the user is on a YouTube video page. I've also been able to successfully open a new tab with ElevenLabs and input the YouTube link of the video into the AI dubbing tool. I'm currently working on waiting for the video to be dubbed and then switching the video to the dubbed version by changing the video stream to the link of the dubbed video.

#### 2023-11-11 20:29 


<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7128575862542647297" height="750" width="100%" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>


The project is on pause for my subscription to renew and for new credits to be added to my account. At the current subscription prices, it costs $11 per hour of dubbing using the Creator plan at $22/mo and $8.25 per hour using the Growing Business plan at $330/mo. In the meantime, I'll be look into free alternatives to <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a>.







