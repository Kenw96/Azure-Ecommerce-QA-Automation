from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.saucedemo.com")


def login():

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    print("Login Successful")


def cart_test():

    login()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    print("Item Added To Cart")


def checkout_test():

    login()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    driver.find_element(By.ID, "checkout").click()

    print("Checkout Started")


choice = input(
    "Choose test: login / cart / checkout : "
)

if choice == "login":
    login()

elif choice == "cart":
    cart_test()

elif choice == "checkout":
    checkout_test()

else:
    print("Invalid Choice")


time.sleep(5)

driver.quit()
