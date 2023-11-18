Python doesn’t have built-in mobile development capabilities, but there are packages you can use to create mobile applications, like Kivy, [PyQt](https://riverbankcomputing.com/software/pyqt/intro), or even Beeware’s [Toga](https://toga.readthedocs.io/en/latest/) library.

These libraries are all major players in the Python mobile space. However, there are some benefits you’ll see if you choose to create mobile applications with **Kivy**. Not only will your application look the same on all platforms, but you also won’t need to compile your code after every change. What’s more, you’ll be able to use Python’s clear syntax to build your applications.

**In this tutorial, you’ll learn how to:**

-   Work with Kivy widgets
-   Lay out the UI
-   Add events
-   Use the KV language
-   Create a calculator application
-   Package your application for iOS, Android, Windows, and macOS

This tutorial assumes you’re familiar with object-oriented programming. If you’re not, then check out [[Object-Oriented Programming (OOP) in Python 3]]

Let’s get started.

## Understanding the Kivy Framework
### Fresh[¶](https://kivy.org/doc/stable/philosophy.html#fresh "Permalink to this headline")

Kivy is made for today and tomorrow. Novel input methods such as Multi-Touch have become increasingly important. We created Kivy from scratch, specifically for this kind of interaction. That means we were able to rethink many things in terms of human computer interaction, whereas older (not to mean ‘outdated’, rather ‘well-established’) toolkits carry their legacy, which is often a burden. We’re not trying to force this new approach to using a computer into the corset of existing models (say single-pointer mouse interaction). We want to let it flourish and let you explore the possibilities. _This_ is what really sets Kivy apart.

### Fast[¶](https://kivy.org/doc/stable/philosophy.html#fast "Permalink to this headline")

Kivy is fast. This applies to both _application development_ and _application execution_ speeds. We have optimized Kivy in many ways. We implement time-critical functionality on the _C level_ to leverage the power of existing compilers. More importantly, we also use _intelligent algorithms_ to minimize costly operations. We also use the _GPU_ wherever it makes sense in our context. The computational power of today’s graphics cards surpasses that of today’s CPUs by far for some tasks and algorithms, especially drawing. That’s why we try to let the GPU do as much of the work as possible, thus increasing performance considerably.

### Flexible[¶](https://kivy.org/doc/stable/philosophy.html#flexible "Permalink to this headline")

Kivy is flexible. This means it can be run on _a variety of different devices_, including Android powered smartphones and tablets. We support _all major operating systems_ (Windows, Linux, OS X). Being flexible also means that Kivy’s fast-paced development allows it to _adapt to new technologies quickly_. More than once have we added support for new external devices and software protocols, sometimes even before they were released. Lastly, Kivy is also flexible in that it is possible to use it in combination with a great number of different third-party solutions. For example, on Windows we support WM\_TOUCH, which means that any device that has Windows 7 Pen & Touch drivers will _just work_ with Kivy. On OS X you can use Apple’s Multi-Touch capable devices, such as trackpads and mice. On Linux, you can use HID kernel input events. In addition to that, we support TUIO (Tangible User Interface Objects) and a number of other input sources.

### Free[¶](https://kivy.org/doc/stable/philosophy.html#free "Permalink to this headline")

Kivy is free to use. You don’t have to pay for it. You don’t even have to pay for it if you’re making money out of selling an application that uses Kivy.

## Installing Kivy
	python -m pip install Kivy
	

## Working With Kivy Widgets
A **widget** is an onscreen control that the user will interact with. All graphical user interface toolkits come with a set of widgets. Some common widgets that you may have used include buttons, combo boxes, and tabs. Kivy has many widgets built into its framework.

### Running a “Hello, Kivy!” Program
To see how Kivy works, take a look at the following “Hello, World!” application:


<iframe
		border=0
		frameborder=0
		height=400
		width=800 src="https://gist.github.com/passivebot/8ae9452b36ce28e00b82deb055ced438"></iframe>

