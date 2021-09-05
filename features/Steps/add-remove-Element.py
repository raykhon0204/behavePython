from behave import *
#from selenium import webdriver

@then('click on Add/Remove Elements')
def clickAddlink(context):
    context.driver.find_element_by_link_text('Add/Remove Elements').click()

@then('click on add element button')
def clickAddButton(context):
    context.driver.find_element_by_xpath('//*[@id="content"]/div/button').click()


@when('new element Delete is added')
def verifyElement(context):
    try:
        text1 = context.driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/button[1]').text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if text1 == "Delete":
        assert True, "Test Passed"



@then('click on Delete and remove the element')
def removeElement(context):
    context.driver.find_element_by_xpath('//*[@id="elements"]/button').click()

