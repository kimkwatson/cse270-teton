# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSmokeTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_adminPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(2576, 1408)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Username:"
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("kim")
    self.driver.find_element(By.ID, "password").send_keys("password")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
  
  def test_directoryPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(2576, 1408)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
  
  def test_header(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1290, 1038)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
  
  def test_homePage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(2576, 1408)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
    assert len(elements) > 0
    assert self.driver.find_element(By.LINK_TEXT, "Join Us").text == "Join Us"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > .centered-image")
    assert len(elements) > 0
  
  def test_joinPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(2576, 1408)
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "First Name"
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("Kim")
    self.driver.find_element(By.NAME, "lname").send_keys("Watson")
    self.driver.find_element(By.NAME, "bizname").send_keys("Apple")
    self.driver.find_element(By.NAME, "biztitle").send_keys("Boss")
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Email"
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  