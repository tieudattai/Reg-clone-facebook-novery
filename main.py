from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from model.get_Name import cre_name
from model.get_Phone import cre_phone
from model.get_Email import cre_email
from model.get_PassWord import cre_password
import random
import requests

height = 1000
weight = 450

mobile_emulation = {
    "deviceMetrics": { "width": weight, "height": height, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 5.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}

# setup chrome
def run():
	ip = requests.get('https://ipinfo.io/ip').text
	options = webdriver.ChromeOptions()
	options.add_argument("--mute-audio")
	options.add_experimental_option("mobileEmulation", mobile_emulation)
	driver = webdriver.Chrome(options=options)
	driver.set_window_rect(0,0,weight,height)

	# get infomation
	firstname = cre_name(1)
	lastname = cre_name(2)
	phone = cre_phone()
	email = cre_email(firstname + ' ' + lastname)
	password = cre_password()
	# login tới trang
	driver.get('https://m.facebook.com/reg/')
	sleep(2)

	# điền họ
	driver.find_element(By.NAME, 'firstname').send_keys(firstname)
	sleep(1)

	# điền tên
	driver.find_element(By.NAME, 'lastname').send_keys(lastname)
	sleep(1)

	# ấn tiếp tục
	driver.find_element(By.XPATH, '//*[@id="mobile-reg-form"]/div[9]/div[2]/button[1]').click()
	sleep(2)

	# chọn ngày 1 - 28
	driver.find_element(By.NAME, 'birthday_day').click()
	sleep(2)
	driver.find_element(By.XPATH, f'//*[@id="day"]/option[{random.randint(1,28)}]').click()
	sleep(2)

	# chọn tháng 1 - 12
	driver.find_element(By.NAME, 'birthday_month').click()
	sleep(2)
	driver.find_element(By.XPATH, f'//*[@id="month"]/option[{random.randint(1,12)}]').click()
	sleep(2)

	# chọn năm 1993 - 2004
	driver.find_element(By.NAME, 'birthday_year').click()
	sleep(2)
	driver.find_element(By.XPATH, f'//*[@id="year"]/option[{random.randint(19,30)}]').click()
	sleep(2)

	# ấn tiếp tục
	driver.find_element(By.XPATH, '//*[@id="mobile-reg-form"]/div[9]/div[2]/button[1]').click()
	sleep(2)

	# điền số điện thoại
	driver.find_element(By.NAME, 'reg_email__').send_keys(phone)
	sleep(2)

	# ấn tiếp tục
	driver.find_element(By.XPATH, '//*[@id="mobile-reg-form"]/div[9]/div[2]/button[1]').click()
	sleep(2)

	# chọn giới tính
	driver.find_element(By.XPATH, '//*[@id="sex"]/div/div[3]/div/label[1]/div').click()
	sleep(2)

	# ấn tiếp tục
	driver.find_element(By.XPATH, '//*[@id="mobile-reg-form"]/div[9]/div[2]/button[1]').click()
	sleep(2)

	# điền mật khẩu
	driver.find_element(By.NAME, 'reg_passwd__').send_keys(password)
	sleep(2)

	# ấn tiếp tục
	driver.find_element(By.XPATH, '//*[@id="mobile-reg-form"]/div[9]/div[2]/button[4]').click()

	sleep(15)
	uid = driver.get_cookies()[0]['value']
	if 'checkpoint' in driver.current_url:
		status = 'checkpoint'
	else:
		status = 'ok'
	with open('acc_facebook.csv', 'a') as w:
		w.write(f'{uid},{password},{phone},{ip},{status}\n')
	w.close()
	print(f"{uid}|{phone}|{password}|{ip}|{status}")
	driver.quit()

for i in range(10):
	run()
	sleep(10)