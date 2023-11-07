# Extensions 101: Streamlining the Experience of Watching Dubbed Content on YouTube with the Eleven Labs Dubbing Extension

At [Passivebot](https://github.com/passivebot), we’re always looking for better and more efficient ways to improve user experience. In line with this goal, we are excited to get working on our latest project: the <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a> Dubbing Extension. This extension streamlines the experience of viewing dubbed content on YouTube by allowing users to easily switch between dubbed and original audio tracks with a single click.

# What Dubbing Is

Dubbing is a new technology but it is rapidly gaining traction and has already been used to create episodes of popular anime shows like Attack on Titan, [My Hero Academia](https://www.crunchyroll.com/series/G6NQ5DWZ6/my-hero-academia), and Boku no Hero Academia. It is the process of replacing one language with another in a movie or TV series. From Hollywood movies released in multiple languages to Japanese anime dubbed in Spanish, dubbing is now commonplace among content streaming services.

Dubbing has now become even more accessible thanks to AI dubbing, a technology developed by <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a>. AI dubbing makes it easier for content creators to offer their work in multiple languages by leveraging the power of artificial intelligence. It ensures that the original speaker's voice characteristics are preserved, which is especially important with dubbed content like film and anime.

# The Eleven Labs Dubbing Extension

Without an official release of a Dubbing API by <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a>, Passivebot independently developed a Chrome extension named "<a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a> Dubbing Extension." This tool facilitates the viewing of AI-dubbed content on YouTube, targeting content-creators who have not yet adopted AI dubbing technology. It simplifies the process for users to experience dubbed video content.

Requirements:

- [ ] Allow users to watch dubbed content on YouTube with a single click

The extension will need to simplify the process of having to enter the YouTube link of the video on <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a> to a single click.

We intend to do this by running a background script that will automatically detect if the user is on a YouTube video page. If the user is on a YouTube video page, the extension will display a button that will allow the user to automatically input the YouTube link of the video into the <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a> AI dubbing tool, wait for the video to be dubbed, and then switch the video to the dubbed version by changing the video stream to the link of the dubbed video.

### Design
 
Originally, textension will be designed to be as simple as possible. It will have a single button that will allow the user perform the following actions:

- [ ] Automatically input the YouTube link of the video into the <a href = "https://try.elevenlabs.io/c3516gvcplb3" target = "_blank" rel = "noopener noreferrer">ElevenLabs</a> AI dubbing tool
- [ ] Wait for the video to be dubbed
- [ ] Switch the video to the dubbed version by changing the video stream to the link of the dubbed video

### Implementation

We will be using the following technologies to implement the extension:

1. [ ] JavaScript
2. [ ] HTML
3. [ ] CSS




