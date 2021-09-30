from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t

# define driver and browser
#ptions = webdriver.SafariOptions()
#options.add_argument("start-maximized")
#options.add_argument("disable-infobars")
#options.add_argument("--disable-extensions")
#driver = webdriver.Safari(safari_options=options)
driver = webdriver.Safari()
driver.get('https://www.udemy.com')


def wait(element):
	try:
		element1 = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, element)))
		return element1
	except:
		print("Exception might have occurred......??????")


# check for correct title text
billboard = driver.find_element_by_class_name('headline__main-text')
#print('billboard_id: ', billboard.id)
print("Checking headline is 'A broad selection of courses'...")
assert "A broad selection of courses" in billboard.text

# clear searchbox
searchbox = driver.find_element_by_class_name("udlite-text-input-large")
t.sleep(1)
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "udlite-text-input-large"))).click() #object not clickable...

searchbox.clear()
# enter some text in search box using send_keys
search_text = 'sausages'
searchbox.send_keys(search_text)
#check the text
print('Checking text entered in search field...')
form = driver.find_element_by_class_name("udlite-search-form-autocomplete-input-group")
print('Text is: ', searchbox.get_attribute('value'))
assert search_text in searchbox.get_attribute('value')
# print(dir(form))

# click on a button
submit_button = driver.find_element_by_xpath("//*[@id='udemy']/div[1]/div[3]/div[2]/div/div[2]/div/form/button")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='udemy']/div[1]/div[3]/div[2]/div/div[2]/div/form/button"))).click()
submit_button.submit()
print('Search form submitted. Wait 5sec...')

# check that when button was pressed navigates to search result page and displays correct search
t.sleep(5)  # give time for page to load
print('Search redirect URL is: ', driver.current_url)
output_message = driver.find_element_by_class_name("udlite-heading-xl")
print('Checking that text was used to search...')
print(output_message.text)
assert search_text in output_message.text
print('NOTE: when last tested the Udemy search no longer works using Selenium. It redirects to homepage :(')

#close window
driver.quit()
