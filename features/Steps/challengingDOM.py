from behave import *

@then('click on Challenging DOM link')
def challengDOM(context):
    context.driver.find_element_by_link_text('Challenging DOM').click()


@then('verify the number of rows')
def verifyRows(context):
    rows = context.driver.find_elements_by_tag_name('tr')
    numRows = len(rows)
    print(numRows)

@then('Verify the canvas element exists')
def step_impl(context):
    canvas = context.driver.find_element_by_id('canvas')
    test1 = canvas.text
    print(test1)