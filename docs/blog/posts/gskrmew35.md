---
title: Setting Up RuneLite for Building with IntelliJ IDEA
description: A step-by-step guide to setting up RuneLite for building with IntelliJ IDEA.
authors: [harmindersinghnijjar]
date: 2024-02-04
tags: [RuneLite, IntelliJ IDEA, JDK 11, Maven]
categories: [RuneLite, IntelliJ IDEA, JDK 11, Maven]
toc: true
comments: true
---

Setting up RuneLite for building with IntelliJ IDEA involves several steps. Here's a step-by-step guide to get you started:

### Getting Started

1. **Download and Install IntelliJ IDEA**: If you haven't already, download and install IntelliJ IDEA. The Community Edition is free and sufficient for RuneLite development.

2. **Install JDK 11**: RuneLite is built using JDK 11. You can install this JDK version through IntelliJ IDEA itself by selecting the Eclipse Temurin (AdoptOpenJDK HotSpot) version 11 during the setup.

### Importing the Project

3. **Clone RuneLite Repository**: Open IntelliJ IDEA and select `Check out from Version Control` > `Git`. Then, in the URL field, enter RuneLite's repository URL: `https://github.com/runelite/runelite`. If you plan to contribute, fork the repository on GitHub and clone your fork instead.

4. **Open the Project**: After cloning, IntelliJ IDEA will ask if you want to open the project. Confirm by clicking `Yes`.

### Installing Lombok

5. **Install Lombok Plugin**: RuneLite uses Lombok, which requires a plugin in IntelliJ IDEA.
   - Go to `File` > `Settings` (on macOS `IntelliJ IDEA` > `Preferences`) > `Plugins`.
   - In the Marketplace tab, search for `Lombok` and install the plugin.
   - Restart IntelliJ IDEA after installation.

### Building the Project

6. **Build with Maven**: RuneLite uses Maven for dependency management and building.
   - Locate the `Maven` tab on the right side of IntelliJ IDEA.
   - Expand the `RuneLite (root)` project, navigate to `Lifecycle`, and double-click `install`.
   - After building, click the refresh icon in the Maven tab to ensure IntelliJ IDEA picks up the changes.

### Running the Project

7. **Run RuneLite**:
   - In the `Project` tab on the left, navigate to `runelite -> runelite-client -> src -> main -> java -> net -> runelite -> client`.
   - Right-click the `RuneLite` class and select `Run 'RuneLite.main()'`.

### Conclusion

You've now set up and run RuneLite using IntelliJ IDEA! If you encounter any issues, consult the `Troubleshooting` section of the RuneLite wiki for common solutions. Remember to keep both your JDK and IntelliJ IDEA up to date to avoid potential issues.
