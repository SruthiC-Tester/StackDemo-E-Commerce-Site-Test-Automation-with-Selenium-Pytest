
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class TestStackDemo:

 @pytest.fixture(scope="function")

 def setup(self):
  self.driver = webdriver.Chrome()
  self.driver.get("https://bstackdemo.com/")
  assert self.driver.title == "StackDemo"
  self.driver.maximize_window()
  self.wait = WebDriverWait(self.driver, 20)
  yield self.driver
  self.driver.quit()

 def test_should_go_to_browerstack_page(self,setup):
  assert self.driver.title == "StackDemo"

 def test_should_donot_go_to_browerstack_page(self,setup):
  assert self.driver.title == "StackDemo123"

 def test_selecting_an_item(self,setup):
  driver = setup
  driver.maximize_window()

  wait = WebDriverWait(self.driver, 10)

 # first login
  signin_button = driver.find_element(By.ID, "signin")
  signin_button.click()

 # USERNAME dropdown
  username_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]/div/div[1]')))
  username_dropdown.click()

  username_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='demouser']")))
  username_option.click()

 # PASSWORD dropdown
  password_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div/div[1]')))
  password_dropdown.click()

  password_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='testingisfun99']")))
  password_option.click()

 # Submit button
  login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-btn")))
  login_button.click()

  WebDriverWait(driver, 30).until(EC.url_contains("signin=true"))
  assert "StackDemo" in driver.title
  assert driver.current_url == "https://bstackdemo.com/?signin=true"

 # Click "Add to cart"
  search_ADDTOCART_text_box = driver.find_element(By.XPATH, '//*[@id="1"]/div[4]')
  search_ADDTOCART_text_box.click()

 # Click "Checkout"
  checkout_text_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]/div[3]')))
  checkout_text_box.click()

  WebDriverWait(driver, 30).until(EC.url_contains("checkout"))
  assert "StackDemo" in driver.title
  assert driver.current_url == "https://bstackdemo.com/checkout"

  search_firstname_text_box = driver.find_element(By.ID, "firstNameInput")
  search_firstname_text_box.send_keys("sruthi")
  search_firstname_text_box.send_keys(Keys.ENTER)

  search_lastname_text_box = driver.find_element(By.ID, "lastNameInput")
  search_lastname_text_box.send_keys("c")
  search_lastname_text_box.send_keys(Keys.ENTER)

  search_address_text_box = driver.find_element(By.ID, "addressLine1Input")
  search_address_text_box.send_keys("india")
  search_address_text_box.send_keys(Keys.ENTER)

  search_state_text_box = driver.find_element(By.ID, "provinceInput")
  search_state_text_box.send_keys("kerala")
  search_state_text_box.send_keys(Keys.ENTER)

  search_state_text_box = driver.find_element(By.ID, "postCodeInput")
  search_state_text_box.send_keys("678583")

  submit_text_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout-shipping-continue"]')))
  submit_text_box.click()

  WebDriverWait(driver, 30).until(EC.url_contains("confirmation"))
  assert "StackDemo" in driver.title
  assert driver.current_url == "https://bstackdemo.com/confirmation"

  downloadorderreceipt_button = wait.until(EC.element_to_be_clickable((By.ID, "downloadpdf")))
  downloadorderreceipt_button.click()

  continueshopping_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button--tertiary.optimizedCheckout-buttonSecondary")))
  continueshopping_button.click()








