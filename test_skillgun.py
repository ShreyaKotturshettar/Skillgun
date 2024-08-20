from selenium import webdriver
import time
driver = webdriver.Chrome()

#test case1 :testing student login functionality
def test_skillgun_login():
    driver.get('http://skillgun.com')
    time.sleep(5)

    mobile = driver.find_element('name', 'ctl00$ContentPlaceHolder1$tbPhoneNumber')
    mobile.send_keys('7892536133')
    time.sleep(5)  # to allow skillgunserver to check mobile no validity

    email = driver.find_element('id', 'ContentPlaceHolder1_tbEmail')
    email.send_keys('shreyakotturshettar06@gmail.com')

    pw = driver.find_element('name', 'ctl00$ContentPlaceHolder1$tbPassword')
    pw.send_keys('Shreya@133')
    cb = driver.find_element('xpath', '//*[@id="ckbkPolicyAgreement"]')
    cb.click()
    time.sleep(5)  # allow tester to enter captcha

    login = driver.find_element('id', 'ContentPlaceHolder1_btnLogin')
    login.click()
    time.sleep(5)  # allow skillgun server to validate login credentials

    assert 'Home' in driver.current_url


#test case2: testing if profile settings button is working or not
def test_skillgun_profilesettings():
    profile = driver.find_element('link text', 'profile settings')
    profile.click()
    time.sleep(5)  # wait for few seconds to open profile page
    assert 'ProfileSetting' in driver.current_url

#test case 3 :testing if edit contacts button is working or not
def test_skillgun_profile_editcontacts():
    edit = driver.find_element('id', 'ContentPlaceHolder1_hlEditContact')
    edit.click()
    time.sleep(5)
    assert 'EditContactDetails' in driver.current_url


#test case 4:testing if saving conatcts functionalities working or not
def test_skillgun_profile_savecontact():
    cur_add_line = driver.find_element('id', 'ContentPlaceHolder1_tbCALine1')
    cur_add_line.clear()  # it remove the current address
    cur_add_line.send_keys('Exotica pg')  # it adds new address 'hyderabad'

    cur_city = driver.find_element('id', 'ContentPlaceHolder1_tbCACity')
    cur_city.clear()
    cur_city.send_keys('Hyderabad')

    cur_state = driver.find_element('id', 'ContentPlaceHolder1_ddlCAState')
    cur_state.send_keys('Telagana')  # no need to clear the box bcz it is dropdown box

    save = driver.find_element('id', 'ContentPlaceHolder1_btnSubmit')
    save.click()
    time.sleep(5)  # wait for server to update in the database

