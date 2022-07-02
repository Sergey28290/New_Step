from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('Open the Account login page')
def step_impl(context):
    link = 'https://bumbleby.ru'
    context.driver.implicitly_wait(6)
    context.driver.get(link)


@when('Enter login "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.XPATH, "//*[@placeholder='Почта']").send_keys(user)
    context.driver.find_element(By.XPATH, "//*[@placeholder='Пароль']").send_keys(pwd)


@when('Click on the Submit button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@class='btn fill']").click()


@when('Click on the Profile button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@class='avatar_icon']").click()


@when('Verify that the Last name field present on a page')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//*[text()[contains(., 'Фамилия')]]").is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('Verify that the First name field present on a page')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//*[text()[contains(., 'Имя')]]").is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('Verify that the Patronymic field present on a page')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//*[text()[contains(., 'Отчество')]]").is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('Verify that the Postal address field present on a page')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//*[text()[contains(., 'адрес')]]").is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('Verify that the Email field present on a page')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//*[text()[contains(., 'Email')]]").is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('Verify that the Telephone field present on a pages')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//*[text()[contains(., 'Телефон')]]").is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('Verify that the Date of birth field present on a page')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//*[text()[contains(., 'Дата рождения')]]").is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when('Verify that the Category field present on a page')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//*[text()[contains(., 'Категория')]]").is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"


@then('Bumbleby UI meets the technical specification')
def step_impl(context):
    context.driver.close()
