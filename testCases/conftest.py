from selenium import webdriver
import pytest
#step 3 to 6
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

# #step-7.1
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("Lunching Chrome browser")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#         print("Lunching Firefox browser")
#     else:
#         driver = webdriver.Ie()
#         print("Lunch Default browser")
#     return driver
#
# def pytest_addoption(parser):          # this will get the value from CLI/hooks
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):                        # this will return the browser value to setup method
#     return request.config.getoption("--browser")

# step-8.1
# It is hooked for adding Environment info to HTML Reports
'''def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['tester'] = "Bikash" '''

# It is hook for delete/modify Environment info to HTML Report
'''@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)'''