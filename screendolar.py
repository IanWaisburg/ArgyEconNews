from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
from PIL import Image

def screen(url,class_name,png_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)
    driver.get(url)
    time.sleep(2)
    element = driver.find_element_by_class_name(class_name)
    width = 1928
    height = element.size['height'] + 1000
    driver.set_window_size(width,height)
    time.sleep(2)
    driver.save_screenshot(png_name)
    driver.quit()

screen("https://www.dolarhoy.com","table-responsive","dolar2.png")

im = Image.open("dolar2.png")
width, height = im.size
# Setting the points for cropped image 
left = 400
top = 130
right = 1150
bottom = 530
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
  
# Shows the image in image viewer 
im1.save("dolar2_recortada.png") 