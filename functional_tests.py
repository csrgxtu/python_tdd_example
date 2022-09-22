from selenium import webdriver

# browser = webdriver.Firefox()
# download chrome driver and place it into your path https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52/
# in mac make chromedriver runnable by setting perm: xattr -d com.apple.quarantine path/chromedriver
# install geckodriver: brew install geckodriver
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
