[[MineDojo - Creating Embodied AI Agents with Unlimited Knowledge from the Internet |MineDojo]] is a novel AI research framework that facilitates the development of embodied agents capable of open-ended learning. The framework comprises an extensive simulation suite built on Minecraft that offers a diverse set of tasks, and provides unrestricted access to an internet-scale knowledge base consisting of 730K YouTube videos, 7K Wiki pages, and 340K Reddit posts.

With MineDojo, AI agents can engage in unconstrained exploration of a procedurally generated 3D world characterized by varied terrains, abundant mining resources, crafting tools, structural possibilities, and enigmatic wonders. Unlike traditional isolation-based learning, MineDojo enables agents to tap into the collective wisdom of millions of human players worldwide, thereby facilitating knowledge transfer and skill acquisition.

### Contents
1. Installation
2. Getting Started
3. Benchmarking Suite
	1. Programmatic Tasks
	2. Creative Tasks
	3. Playthrough Tasks


### Installation
To use MineDojo, you will need a computer with Python version 3.9 or later installed. MineDojo has been added on two types of computers: one that uses Ubuntu 20.04 and another that uses Mac OS X. Before you install MineDojo, you must first install some other programs that it needs to work properly. One of these programs is called JDK 8, which is necessary for running the Minecraft backend. To make sure that installing MineDojo does not affect other programs on your computer, it is recommend that you create a new Conda virtual environment to keep everything separate.

If you find all of this too difficult, there is a pre-built Docker image that you can use instead. To install MineDojo, all you need to do is follow these simple steps:

To install the stable version of MineDojo, you can use a program called "pip" by entering the following command:

``` Python
pip install minedojo
```

This will download and install MineDojo onto your computer, allowing you to use it for your AI research.

%%If you want to install the latest version of MineDojo directly from the main branch of the repository, you can do so by following these steps:

1.  Open a command prompt or terminal on your computer.
2.  Enter the command "git clone https://github.com/MineDojo/MineDojo && cd MineDojo" to download the MineDojo repository and navigate to its directory.
3.  Enter the command "pip install -e ." to install MineDojo onto your computer.

These commands will allow you to download and install the latest version of MineDojo, which may include new features or improvements that are not yet available in the stable version.

To ensure that MineDojo has been installed correctly on your computer, you can run the following script:

``` Bash
python minedojo/scripts/validate_install.py
```

Please note that the initial run of this script may take some time to compile the Java code. Once the compilation is complete, a Minecraft window will appear on your screen, featuring the same gaming interface that human players use. If everything has been installed correctly, you will see the message "\[INFO] Installation Success".%%


