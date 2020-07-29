from personal_data import *
from selenium import webdriver
import os
import sys

path="/Users/davig/Documents/PROYECTS/"
url="https://github.com/login"

browser= webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
browser.get(url)

folder_name=str(sys.argv[1])

def create_folder_local():
    # os.chdir(path)
    folder_path= path + folder_name
    succesfully=False
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        succesfully=True
    else:
        print("The file is alredy exist")
    return succesfully

def create_github_repository():
    # loggin
    xpath_email_input= '//*[@id="login_field"]'
    email_input= browser.find_element_by_xpath(xpath_email_input)
    email_input.send_keys(email)

    xpath_password_input= '//*[@id="password"]'
    password_input= browser.find_element_by_xpath(xpath_password_input)
    password_input.send_keys(password)

    xpath_submit= '//*[@id="login"]/form/div[4]/input[9]'
    submit_button=  browser.find_element_by_xpath(xpath_submit)
    submit_button.click()

    # navigating to creating repository
    browser.get('https://github.com/new')
    browser.find_element_by_xpath('//*[@id="repository_name"]').send_keys(folder_name)
    browser.find_element_by_xpath('//*[@id="new_repository"]/div[6]/button').submit()

    # quit browser
    browser.quit()


# def browser_close():
#     condition= str(input("Para cerrar ingrese C:"))
#     while(condition != "C"):
#         condition= str(input("Para cerrar ingrese C:"))
#     browser.close()


if __name__ == '__main__':
    succes=create_folder_local()
    
    # if(succes):
    #     create_github_repository()
