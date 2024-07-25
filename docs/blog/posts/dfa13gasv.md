---
title: Setting Up Your Development Environment For DreamBot Scripting - Intellij IDEA
description: A step-by-step guide to setting up your development environment for DreamBot scripting using Intellij IDEA.
authors: [harmindersinghnijjar]
date: 2024-01-30
tags: [DreamBot, Java, Scripting, Intellij IDEA]
categories: [DreamBot, Java, Scripting, Intellij IDEA]
toc: true
comments: true
---

# Setting Up Your Development Environment For DreamBot Scripting: Intellij IDEA

In this tutorial, we'll guide you through the process of setting up your development environment for DreamBot scripting. This setup will enable you to create and execute your own scripts.

## Prerequisites

Before beginning, ensure you have:

1. The Java Development Kit (JDK) installed. Instructions are available in the [Installing JDK section](https://dreambot.org/guides/scripter-guide/script-dev/installing-jdk/).
2. DreamBot installed on your computer. Launch it at least once to access the client files.

## Integrated Development Environment (IDE)

Since DreamBot scripts are written in Java, using an Integrated Development Environment (IDE) like IntelliJ IDEA can be very helpful.

### Download and Install IntelliJ IDEA

- Visit the [JetBrains IntelliJ IDEA website](https://www.jetbrains.com/idea/download/#section=windows) and install the latest Community build version.

### Create a New Project
![](https://dreambot.org/guides/scripter-guide/script-dev/images/intellij_start.png
)
1. Open IntelliJ IDEA.
2. Click **New Project**.
3. Select Java, with IntelliJ as the build system.
4. Choose the JDK you downloaded earlier.
5. Name your script and set the project's save location.
6. Click **Create**.

![](https://dreambot.org/guides/scripter-guide/script-dev/images/intellij_newproject.png)

### Configure the Project

1. Right-click the **src** folder and choose **New -> Java Class**.
2. Name your class, e.g., "TestScript".

![](https://dreambot.org/guides/scripter-guide/script-dev/images/intellij_firstclass.png)

### Add Dependencies

1. Go to **File** -> **Project Structure**.
2. Under **Libraries**, click the "+" and select **Java**.
3. Navigate to the DreamBot BotData folder and choose the `client.jar` file.

### Add an Artifact

1. Go to **File** -> **Project Structure**.
2. Select **Artifacts**.
3. Click "+" and choose **JAR -> From modules with dependencies**.
4. Set the Output directory to the DreamBot Scripts folder.
    - Windows: `C:\Users\YOUR_USER\DreamBot\Scripts`
    - Linux/MacOS: `/home/YOUR_USER/DreamBot/Scripts`
5. Exclude `client.jar` from the artifact by removing it from the list.

![](https://dreambot.org/guides/scripter-guide/script-dev/images/intellij_artifact.png)



For detailed instructions on script setup and execution, refer to the [Running Your First Script](https://dreambot.org/guides/scripter-guide/script-dev/running-first-script/) guide.

## Summary and Expense Overview

Utilizing RAG and Langchain with GPT-4 for this blog post has been enlightening. The RAG AI Assistant has been invaluable in formulating ideas and providing project assistance. Below is the cost breakdown for using RAG AI Assistant:

- **Total Tokens Processed:** 1797
- **Tokens for Prompts:** 1285
- **Tokens for Completions:** 512
- **Overall Expenditure (USD):** $0.06927

This highlights the efficiency and cost-effectiveness of the RAG AI Assistant in content creation.


