from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class TspInteractor:

    def __init__(self):
        self.__accept_cookies_xpath = "//iframe[@title='Iframe title']"
        self.__accept_btn_xpath = "//button[@title='Alle akzeptieren']"

        self.__offer_iframe_xpath  = "//iframe[@allow='payment']"
        self.__close_btn_id = "closeBtn"
        self.__checkbox_class = "tspA6i3 visually-hidden"

        self.x_post_iframes = "//iframe[@title='X Post']"
        self.x_post_xpath = "//a[@aria-label='Diesen Post auf X besuchen']"

    def __start(self,url:str):
      #  print("__start()")
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('headless')
        driver : WebDriver | None = None
        try:
            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.get(url)
            driver.implicitly_wait(3)
        except Exception as e:
            print(f"Fehler beim Starten des Webdrivers: {e}")
        return  driver


    def __accept_cookies(self, driver: WebDriver):
        print("____accept_cookies)")
        # cookies akzeptieren
        try:
            iframe = driver.find_element(By.XPATH, self.__accept_cookies_xpath)
            if iframe is not None:
            #    print("iframe is not None")
                driver.switch_to.frame(iframe)
                driver.implicitly_wait(2)
                accept_btn = driver.find_element(By.XPATH, self.__accept_btn_xpath )
                accept_btn.click()
                driver.switch_to.default_content()
        except Exception as e:
            print(f"AGB nicht vorhanden: {e}")

    def __close_offer_dialog(self,driver: WebDriver):
    # schließe angebots iframe
      #  print("__close_offer_dialog)")
        try:
            offer_iframe = driver.find_element(By.XPATH, self.__offer_iframe_xpath)
            if offer_iframe is not None:
           #     print("offer_iframe is not None")
                driver.switch_to.frame(offer_iframe)
            #    driver.implicitly_wait(2)
                close_btn = driver.find_element(By.ID, self.__close_btn_id)
                if close_btn is not None:
            #       print("close_btn is not None")
                   close_btn.click()
            driver.switch_to.default_content()
            driver.implicitly_wait(2)
        except Exception as e:
            print(f"Fehler bei >> close_offer_dialog() << \n{e}")

    def __access_therd_party_cookis(self, driver: WebDriver):
       # print("__access_dsgvo)")
        # akzeptiren dsgvo checkbox
        try:
            checkboxes = driver.find_elements(By.CLASS_NAME, self.__checkbox_class)
            if len(checkboxes) > 0:
              #  print("checkbox is not None")
                [checkbox.click() for checkbox in checkboxes]
            driver.implicitly_wait(3)
        except Exception as e:
            print(f"Fehler bei >> access_dsgvo() << \n{e}")

    def __find_x_posts(self,driver: WebDriver):  # xposts finden
      #  print(" __find_x_posts)")
        x_post_links = []
        try:
            x_post_iframes = driver.find_elements(By.XPATH,self.x_post_iframes)
            if len(x_post_iframes) != 0:
               for iframe in x_post_iframes:
                    driver.switch_to.frame(iframe)
                    driver.implicitly_wait(2)
                    x_post_links.append(driver.find_element(By.XPATH,self.x_post_xpath).get_property("href"))
                    driver.switch_to.default_content()
        except Exception as e:
            print(f"Fehler bei >> find_x_posts() << \n{e}")
        print(x_post_links)
        return x_post_links

    #TODO implement search function for other platforms


    def search_for_x_posts(self,url: str):
        driver = self.__start(url)
        self.__accept_cookies(driver)
        self.__close_offer_dialog(driver)
        self.__access_therd_party_cookis(driver)
        self.__find_x_posts(driver)
        driver.quit()

