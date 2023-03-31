
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fastapi.responses import JSONResponse
from selenium.webdriver.common.by import By
from io import BytesIO
from PIL import Image
import langdetect
import requests
import pdb

async def scrapping(url:str):
    print("comienza")
    pdb.set_trace()

    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('disable-translate')
    driver = webdriver.Chrome(options=chrome_options)

    #receive url for scrapping
    driver.get(url)
    pdb.set_trace()

    #validate language
    language = await Language(driver)

    if language == "hi":
        hindi = True
    else:
        hindi = False
    #validate drop down

    #validate hd images
    hd = await ImagesValidate(driver)
    pdb.set_trace()
    driver.quit()

    response = ""
    if hindi == True and hd == True:
        response = {"value":True, "description":"PASS"}
    if hindi == False and hd == True:
        response = {"value":False, "description":"FAIL Translate"}
    if hindi == True and hd == False:
        response = {"value":False, "description":"FAIL HD Images"}
    else:
        response = {"value":False, "description":"FAIL"}
    return JSONResponse(content=response, status_code=200, media_type="application/json")


async def Language(driver):
    text = driver.find_element(By.TAG_NAME, 'body').text
    detect_language = langdetect.detect(text)
    print(detect_language)
    return detect_language

async def ImagesValidate(driver):
    imgs = []
    for elem in driver.find_elements(By.TAG_NAME, "img"):
       imgs.append(elem.get_attribute("src"))
    hd_imgs = []
    for img in imgs:
        try:
            response = requests.get(img, stream=True)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                width, height = image.size
                img_size = int(response.headers['Content-Length'])
                check = 0
                if width or height <= 50:
                    if img_size < 1000:
                        pass
                    else:
                        hd_imgs.append(img)
                        check=1
                if (width or height > 50) and (width or height <= 100):
                    if check==1:
                        pass
                    else:
                        if img_size < 5000:
                            pass
                        else:
                            hd_imgs.append(img)
                            check=1
                if width or height > 200:
                    if check==1:
                        pass
                    else:
                        if img_size < 10000:
                            pass
                        else:
                            hd_imgs.append(img)
                            check=1               
        except:
            pass
    hd = (len(imgs) == len(hd_imgs))
    print(hd)
    return hd
    

async def DropDown(driver):
    return "in process"