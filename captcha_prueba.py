from PIL import Image
from selenium import webdriver

# PARA RESOLVER LOS CAPTCHAS TIPO IMAGEN CON TEXTOS, NUMEROS Y/O SIMBOLOS CON 2CAPTCHA API
def get_captcha(driver, element, path):
    # now that we have the preliminary stuff out of the way time to get that image :D
    location = element.location
    size = element.size
    # saves screenshot of entire page
    driver.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x']
    top = location['y'] 
    right = location['x'] + size['width']
    bottom = location['y'] + size['height'] 

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'png')  # saves new cropped image


driver = webdriver.Firefox(executable_path=r"c:\se\geckodriver.exe")
driver.get("http://forum.geonames.org/gforum/user/insert.page")


# download image/captcha
img = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td/form/table[2]/tbody/tr[7]/td[2]/img")
get_captcha(driver, img, r"C:\Users\Xenofungus\Desktop\selenium\captcha.png")
