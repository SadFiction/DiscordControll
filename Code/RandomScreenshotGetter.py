from os import path
from selenium import webdriver as driver
from selenium.webdriver.common.by import By
import asyncio, random, string , urllib

class screenshotGetter:
    
    async def get(self, location = None):
        if location == None:
            return

        
        try:
            name = await self.generate_id()
            url = await self.__generate()
            web = driver.Chrome("C:\Program Files\Google\chromedriver.exe")
            web.minimize_window()
            
            web.get(url=url)
            web.find_element(By.CLASS_NAME, "css-1hy2vtq").click()
            
            place = web.find_element(by=By.CLASS_NAME , value="under-image")
        #location = web.find_element_by_class_name("under-image")
            image = place.find_element(by=By.TAG_NAME , value = "img")
            #return image.screenshot_as_png
        #image = location.find_element_by_tag_name("img")
            
            
            with open(f"{location}screenshot{ name}.png","xb") as f:
                f.write(image.screenshot_as_png)
                f.close()
                #print(name)
            return name
        except(Exception):
            pass
    async def generate_id(self):
        ids = ""
        for i in range(9):
            ids = ids + str(random.randint(0, 9))

        return ids
    async def __generate(self):
        url = "https://prnt.sc/"
        letters = ""
        numbers = ""
        for _ in range(2):
            letters = letters +random.choice(string.ascii_lowercase)
        
        for _ in range(4):
            numbers = numbers + str(random.randint(0, 9))
        
        return (url + letters + numbers)

        








if __name__ == "__main__":
    main = screenshotGetter()
    asyncio.run(main.get(location="C:/Users/trool/OneDrive/Documents/BoBa.saurus.BOT/BoBa.data/"))