import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def sign_in_ui_test(email, password, acc_type):
    driver.get('http://localhost:3000/auth')
    driver.maximize_window()
    time.sleep(2)
    email_field = driver.find_element(By.ID, "user-email")
    pwrd_field = driver.find_element(By.ID, 'password')
    submit_btn = driver.find_element(By.XPATH, '//*[@id="radix-:r1:-content-sign-in"]/div/div[3]/button')

    email_field.send_keys(email)
    pwrd_field.send_keys(password)
    submit_btn.click()

    time.sleep(3)

    if driver.current_url == ('http://localhost:3000/' + acc_type + "-ui"):
        return True
    return False


def sign_up_ui_test(email, pnum, fname, lname, gender, acc_type, pwrd):
    driver.get('http://localhost:3000/auth')
    driver.maximize_window()
    time.sleep(2)

    reg_tab = driver.find_element(By.ID, "radix-:r1:-trigger-register")
    reg_tab.click()

    email_field = driver.find_element(By.ID, "user-reg-email")
    pnum_field = driver.find_element(By.ID, "user-reg-phone")
    fname_field = driver.find_element(By.ID, "user-reg-fname")
    lname_field = driver.find_element(By.ID, "user-reg-lname")
    gender_field = driver.find_element(By.XPATH,
                                       '//*[@id="radix-:r1:-content-register"]/div/div[2]/div[4]/div[1]/button')
    acc_type_field = driver.find_element(By.XPATH,
                                         '//*[@id="radix-:r1:-content-register"]/div/div[2]/div[4]/div[2]/button')
    pwrd_field = driver.find_element(By.ID, "user-reg-pwrd")
    pwrd_conf_field = driver.find_element(By.ID, "user-reg-conf-pwrd")
    submit_btn = driver.find_element(By.XPATH, '//*[@id="radix-:r1:-content-register"]/div/div[3]/button')

    email_field.send_keys(email)
    pnum_field.send_keys(pnum)
    fname_field.send_keys(fname)
    lname_field.send_keys(lname)
    gender_field.send_keys(gender)
    acc_type_field.send_keys(acc_type)
    pwrd_field.send_keys(pwrd)
    pwrd_conf_field.send_keys(pwrd)

    submit_btn.click()

    time.sleep(3)

    if driver.current_url == ('http://localhost:3000/' + acc_type + "-ui"):
        return True
    return False


if __name__ == "__main__":
    signed_in_success = sign_in_ui_test('', '', '')
    signed_up_success = sign_up_ui_test('', '', '', '', '', '','')
    print(signed_in_success)
    print(signed_up_success)
