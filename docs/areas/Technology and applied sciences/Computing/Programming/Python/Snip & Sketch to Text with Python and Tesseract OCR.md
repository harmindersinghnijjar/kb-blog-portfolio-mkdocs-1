## Using Google's free Tesseract OCR as the end-all for redundant screenshot hotkeys

Tesseract is a free and open-source OCR engine that can be used to extract text from images. With the help of Snip & Sketch, a built-in tool in Windows, Tesseract can be used to extract text from screen clips.

## Snip & Sketch

Microsoft Windows 10 has a screenshot tool called Snip and Sketch. It is easy to use and can take screenshots of the whole screen, a selected box, or a freehand selection.

![[snip 1.png]]

The screenshot can then be pasted anywhere, including on [Discord servers](https://discord.com/channels/840695460977311744/840695462088540192) and in [Reddit posts](https://www.reddit.com/user/Passivebot_py). This process is typically much faster than using the PrintScreen feature since it saves the user the effort of having to open another tool just to crop out what they want.

I personally use [ShareX](https://getsharex.com/) as my main screen capture tool because it can take care of modifying, uploading, and storing screenshots, screen records, and GIFs all in one place. However, I still have two different Window hotkeys (Win+Shift+S and Ctrl+PrtSc) for taking screenshots, which is redundant. This got me thinking about the different uses I could put the Snip and Sketch tool to.

### Snip&Sketch2Text with OCR

![[Portable_scanner_and_OCR_(video) 1.webm]]
Title: [Portable scanner and OCR (video).webm](https://commons.wikimedia.org/w/index.php?title=File%3APortable_scanner_and_OCR_(video).webm "Portable scanner and OCR (video).webm")  
Author: [Vassia Atanassova - Spiritia](https://commons.wikimedia.org/wiki/User:Spiritia "User:Spiritia")  
Date: 28 February 2017

OCR is a technology that allows you to convert documents, such as scanned paper documents, PDF files, or images captured by a digital camera, into editable and searchable data. The Tesseract Optical Character Recognition (OCR) engine by Google is arguably the most popular out-of-the-box solution for OCR.

It’s only fitting to remedy hotkey redundancy from open-source tools with open-source OCR. 

## About Google Tesseract 

Tesseract is a free software optical character recognition engine developed by Hewlett-Packard in the 1980s. In 2005, it became open source and had since been sponsored by Google. Tesseract has Unicode support and can recognize over 100 languages. It can also be trained to recognize other languages.

### Brief History

Tesseract was initially developed at Hewlett-Packard Laboratories Bristol and at Hewlett-Packard Co, Greeley Colorado between 1985 and 1994. Some additional changes were made in 1996 to port the software to Windows, and again in 1998 to convert some of the code to C++.

## Who Can Leverage OCR?

There are many benefits to digitizing documents using OCR data entry. This includes the ability to transfer important documents to tablets, computers, smartphones, etc. This can be helpful for businesses in various industries, including banking, mortgage, financial, legal, and healthcare. Some commonly digitized documents include invoices, industry articles, tax documents, payroll information, legal filings, contact information, business cards, flyers, and financial investments.

## OCR Pipeline

The process of copying text from an image using OCR involves three simple steps: 
1. Monitoring a folder for new screen clips. 
2. Passing the latest screen clip through the OCR system. 
3. Copying the results from Tesseract OCR to the clipboard.

![[Tesseract_OCR_pipeline_architecture 1.png]]

This can be done with a few lines of code using the [pyscreenshot](https://pypi.org/project/pyscreenshot/ "pyscreenshot"), [pytesseract](https://pypi.org/project/pytesseract/ "pytesseract"), and [pyperclip](https://pypi.org/project/pyperclip/ "pyperclip") libraries.
```python

```

This simple pipeline can be further automated using the [Watchdog](https://pypi.org/project/watchdog/ "Watchdog") library to monitor a folder for new screenshots and the [PyAutoGUI](https://pypi.org/project/PyAutoGUI/ "PyAutoGUI") library to handle hotkey bindings.

```python

```

The code above can be further extended to take advantage of the [Windows Task Scheduler](https://docs.microsoft.com/en-us/windows/win32/taskschd/about-the-task-scheduler "About the Task Scheduler") to start the OCR pipeline on startup.
```python

```

## Conclusion

Google Tesseract is a powerful OCR tool that can be used to convert images to text. With the help of Snip & Sketch and a few lines of code, it can be used to create a simple OCR pipeline that can be used to automate the process of extracting text from images.

## References

- [Tesseract (software)](https://en.wikipedia.org/wiki/Tesseract_(software) "Tesseract (software)")
- [Google Tesseract OCR](https://opensource.google/projects/tesseract "Google Tesseract OCR")
- [ShareX](https://getsharex.com/ "ShareX")
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/ "PyAutoGUI")
- [pyscreenshot](https://pypi.org/project/pyscreenshot/ "pyscreenshot")
- [pytesseract](https://pypi.org/project/pytesseract/ "pytesseract")
- [pyperclip](https://pypi.org/project/pyperclip/ "pyperclip")
- [Watchdog](https://pythonhosted.org/watchdog/ "Watchdog")
