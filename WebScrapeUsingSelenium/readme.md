### Install Selenium and ChromeDriver

[https://chromedriver.chromium.org/downloads]
[Note: Please check the `version` of your `Google Chrome` Browser before downloading the `ChromeDriver`]

###### install and activate your virutal environment

```console
python -m venv env or python -m venv venv (any name you can give to the name of the env folder)
```

```console
source env/bin/activate (for linux users)
```

###### install the selenium in your terminal

```console
pip install selenium
```

Congratulations! You have successfully installed the Selenium framework on your device...

### Importing Libraries and Creating The Driver

```python
from selenium import webdriver # helps us to create driver that help us scrape websites
```

### XPath Syntax

//tagName[@AttributeName="Value"]
