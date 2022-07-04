from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Helpers:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, selector, wait_time=5):
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector), "Не дождались появления элемента")

    def find_elements(self, selector, wait_time=5):
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_all_elements_located(selector), "Не дождались появления элемента")

class YandexHeadPage(Helpers):
    """Главная страница Яндекса"""

    def __init__(self, driver):
        Helpers.__init__(self, driver)

    input_console = (By.CSS_SELECTOR, '#text')
    proposed_results = (By.CSS_SELECTOR, '.mini-suggest__item')
    

    def search_query(self, text):
        """ввести текст в строку поиска и нажать enter"""

        query = self.find_element(self.input_console)
        query.send_keys(text)
        query.send_keys(Keys.ENTER)



class YandexResultPage(Helpers):
    """страница с результатами поиска"""

    def __init__(self, driver):
        Helpers.__init__(self, driver)

    results = (By.CSS_SELECTOR, '.Path')
    text_link = (By.CSS_SELECTOR, 'b')

    def find_right_link(self, text):
        """найти верную ссылку на странице"""
        links = self.find_elements(self.results)
        for link in links:
            link_name = link.find_element(self.text_link[0], self.text_link[1])
            if link_name.text == text:
                link_name.click()
                break
                
class PastebinHeadPage(Helpers):
    """главная страница пастебина"""

    def __init__(self, driver):
        Helpers.__init__(self, driver)

    text_box = (By.CSS_SELECTOR, '#postform-text')
    selection_box = (By.CSS_SELECTOR, '.select2-selection__arrow')
    language_list = (By.CSS_SELECTOR, '.select2-results__option')
    name_box = (By.CSS_SELECTOR, '#postform-name')
    end_button = (By.CSS_SELECTOR, '.btn.-big')

    def input_description(self, content):
        """ввести описание файла в большое окно"""

        self.find_element(self.text_box).send_keys(content)

    
    def open_language_selection(self):
        """открываем список языков"""

        self.find_element(self.selection_box).click()

    
    def choose_right_language(self, language):
        """выбираем из списка нужный язык"""

        language_list = self.find_elements(self.language_list)    
        for lang in language_list:
            if lang.text == language:
                lang.click()
                break


    def input_name(self, name):
        """находим окно для ввода имени"""

        self.find_element(self.name_box).send_keys(name)

    def press_end_button(self):
        """нажимаем кнопку завершения регистрации""" 

        self.find_element(self.end_button).click() 



class PastebinSecondPage(Helpers):
    """страница с результатами обработки"""

    def __init__(self, driver):
        Helpers.__init__(self, driver)

    language_button = (By.CSS_SELECTOR, '.highlighted-code .btn')
    content_position = (By.CSS_SELECTOR, '.de1')
    name_position = (By.CSS_SELECTOR, 'div.info-top h1')


    def language_check(self, language):
        """проверяем верный ли язык"""

        lang_button = self.find_element(self.language_button)
        assert lang_button.text == language, 'выбран неверный язык'

    def content_check(self, content):
        """проверяем описание"""

        description = self.find_element(self.content_position)
        assert description.text == content, 'неверное описание'

    def name_check(self, name):
        """проверка имени"""

        fact_name = self.find_element(self.name_position)
        assert fact_name.text == name, 'неверное имя'        


         
        
