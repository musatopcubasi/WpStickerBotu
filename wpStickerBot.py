from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep

isim ="Egemen"
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

print('Karekodu telefondan okuttuktan sonra WhatsApp ekranının gelmesini bekleyin.')
sleep(7)

kisibul =driver.find_element_by_xpath('//span[@title="{}"]'.format(isim))
kisibul.click()
pyautogui.click(650,962)
sleep(1)
pyautogui.click(806,963)

sayi=0
x,y=760,682
while True:
    pyautogui.click(x,y)
    sleep(0.1)

    if sayi==25:
        break
    sayi+=1
