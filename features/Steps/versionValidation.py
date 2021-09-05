from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when('open the IH homepage')
def openHomePage(context):
    context.driver.get("https://the-internet.herokuapp.com/")


@then('click on AB testing link')
def clickOnABTesting(context):
    context.driver.find_element_by_link_text('A/B Testing').click()

@then('verify the version number')
def verifyVersion(context):
    get_version = context.driver.find_element_by_xpath('//*[@id="content"]/div/h3').text
    get_version = get_version.split()
    print(get_version)
    if len(get_version) == 4:
        version_number = get_version[3]
    else:
        version_number = get_version[0]

    if version_number == "1":
        return True
    else:
        print('No version number this time, sorry!')

@then('close the browser')
def closeBrowser(context):
   context.driver.close()

