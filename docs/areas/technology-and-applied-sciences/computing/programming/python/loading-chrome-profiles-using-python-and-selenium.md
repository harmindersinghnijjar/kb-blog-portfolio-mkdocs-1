When using Python 

To launch Chrome with its default profile using Python's webdriver so that cookies and site preferences persist across sessions, you need to declare the 

This is what finally got it working for me.

```python
from selenium import webdriver

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Path") #Path to your chrome profile
w = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", options=options)
```

To find path to your chrome profile data you need to type `chrome://version/` into address bar . For ex. mine is displayed as `C:\Users\pc\AppData\Local\Google\Chrome\User Data\Default`, to use it in the script I had to exclude `\Default\` so we end up with only `C:\Users\pc\AppData\Local\Google\Chrome\User Data`.

Also if you want to have separate profile just for selenium: replace the path with any other path and if it doesn't exist on start up chrome will create new profile and directory for it.
