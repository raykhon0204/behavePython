from behave import *
from selenium import webdriver


@then('click on basic auth')
def clickOnbasicAuth(context):
    context.driver.find_element_by_xpath('//*[@id="content"]/ul/li[3]/a').click()
    print('test')

@when('login with username and pass')
def switchToLogin(context):
    username = 'admin'
    password = 'admin'
    URL = "https://" +username +":" +password +"@"+ "the-internet.herokuapp.com/basic_auth"
    context.driver.get(URL)
    title = context.driver.title
    print("The page title is: " + title)
    text = context.driver.find_element_by_tag_name("p").text
    print(text)

@when('verify that user logged in successfully')
def verifyAuth(context):
    text = context.driver.find_element_by_xpath('/html/body/div[2]/div/div/p').text
    assert text == 'Congratulations! You must have the proper credentials.'
