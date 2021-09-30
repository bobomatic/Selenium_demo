from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# define driver and browser
driver = webdriver.Safari()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


def wait(element):
	try:
		element1 = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, element)))
		return element1
	except:
		print("Exception might have occurred......??????")


# check for correct title text
assert 'Selenium Easy' in driver.title

# enter some text using send_keys
test_text = 'WAYHEYYYYYYY!!!!!'
user_message = driver.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys(test_text)
# print(user_message)

# click on a button
show_msg_button = driver.find_element_by_class_name('btn-default')
# print(show_msg_button.get_attribute('innerHTML'))
show_msg_button.click()

# check that when button was pressed correct text was outputted
output_message = driver.find_element_by_id("display")
# print(output_message.text)
assert test_text in output_message.text


driver.quit()
