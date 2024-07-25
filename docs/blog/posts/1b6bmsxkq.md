---
title: How to Write a Simple Woodcutting Script Using DreamBot API in 2024
description: A step-by-step guide to creating a simple woodcutting script using the DreamBot API in 2024.
authors: [harmindersinghnijjar]
date: 2024-01-30
tags: [DreamBot, Java, Woodcutting, Scripting]
categories: [DreamBot, Java, Woodcutting, Scripting]
toc: true
comments: true
---

# How to Write a Simple Woodcutting Script Using DreamBot API in 2024

In this tutorial, we will walk through the process of creating a simple woodcutting script using the DreamBot API. This script will allow your in-game character to autonomously chop trees, bank logs, and repeat this process indefinitely.

## Prerequisites

Before we begin, ensure you have the following:

- An Integrated Development Environment (IDE) of your choice. We will be using IntelliJ IDEA in this guide.
- A clean project containing your script's Main class.
- Basic understanding of Java.

## Setting Up Your Project

First, you need to set up your development environment. If you need help with this, you can visit [Setting Up Your Development Environment](https://dreambot.org/guides/scripter-guide/script-dev/setting-up-dev-env/).

Next, create a new project and define your script's Main class. For help with this, visit [Running Your First Script](https://dreambot.org/guides/scripter-guide/script-dev/running-first-script/).

## Creating a Woodcutting Script

Our woodcutting script will involve various tasks such as finding trees, chopping them, walking to the bank, and depositing logs. We will create different states to handle these tasks.

```
public enum State {
    FINDING_TREE,
    CHOPPING_TREE,
    WALKING_TO_BANK,
    BANKING,
    USEBANK,
    WALKING_TO_TREES
}
```

Now, we will create a method within our Main class that returns our current state:

```java
public State getState() {
    if (Inventory.isFull() && !BANK_AREA.contains(Players.getLocal())) {
        return State.WALKING_TO_BANK;
    }
    if (!Inventory.isFull() && !TREE_AREA.contains(Players.getLocal())) {
        return State.WALKING_TO_TREES;
    }
    if (Inventory.isFull() && BANK_AREA.contains(Players.getLocal())) {
        return State.BANKING;
    }
    if (!Inventory.isFull() && TREE_AREA.contains(Players.getLocal())) {
        return State.FINDING_TREE;
    }
    return null;
}
```

### Walking to the Bank

Define a method to handle the state of walking to the bank:

```java
if (Inventory.isFull() && !BANK_AREA.contains(Players.getLocal())) {
    return State.WALKING_TO_BANK;
}
```

Next, implement the logic for walking to the bank in your main loop:

```java
switch (getState()) {
    case WALKING_TO_BANK:
        if (!LocalPlayer.isMoving()) {
            BANK_AREA.getRandomTile().click();
        }
        break;
    // Other cases
}
```

### Banking

Now, let's handle the banking state. We'll start by interacting with the bank booth:

```java
if (!Bank.isOpen() && !LocalPlayer.isMoving()) {
    GameObjects.closest("Bank booth").interact("Bank");
}
```

Next, deposit the logs into the bank and close the bank interface:

```java
case BANKING:
    Bank.depositAll("Logs");
    Time.sleepUntil(() -> !Inventory.contains("Logs"), 2000);
    if (!Inventory.contains("Logs")) {
        Bank.close();
    }
    break;
```

### Walking Back to the Tree Area

To return to the tree area, we need to add a new state and corresponding logic:

```java
if (!Inventory.isFull() && !TREE_AREA.contains(Players.getLocal())) {
    return State.WALKING_TO_TREES;
}

case WALKING_TO_TREES:
    if (!LocalPlayer.isMoving()) {
        TREE_AREA.getRandomTile().click();
    }
    break;
```

### Finding and Chopping Trees

Finally, implement the code that finds and chops trees:

```java
case FINDING_TREE:
    GameObject tree = GameObjects.closest(t -> t.getName().equals("Tree"));
    if (tree != null && tree.interact("Chop down")) {
        Time.sleepUntil(LocalPlayer::isAnimating, 2000);
    }
    break;
```

## Wrapping Up

That's it! You've now created a basic woodcutting script using the DreamBot API. This script will autonomously navigate your character to chop trees, store logs in the bank, and repeat the process. Happy scripting!
