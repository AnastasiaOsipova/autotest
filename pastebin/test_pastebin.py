import unittest
from selenium import webdriver
from pages import YandexHeadPage, YandexResultPage, PastebinHeadPage, PastebinSecondPage

class TestPastebin(unittest.TestCase):

    driver = None
    url = 'https://yandex.ru/'
    path = 'chromedriver.exe'

    #переменные для последующего ввода в консоли
    content = 'anek pro zarplatu'
    name = 'pupa and lupa'
    language = 'C++'

    @classmethod
    def setUpClass(cls):
        path = 'C:\chromedriver\chromedriver.exe'
        cls.driver = webdriver.Chrome(path)
        cls.yandex_head_page = YandexHeadPage(cls.driver)
        cls.yandex_result_page = YandexResultPage(cls.driver)
        cls.pastebin_head_page = PastebinHeadPage(cls.driver)
        cls.pastebin_second_page = PastebinSecondPage(cls.driver)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get(self.url)

    def test_check_input(self):
        search_text = 'pastebin.com'

        #ввод текста в консоль
        self.yandex_head_page.search_query(search_text)
    
        #находим и кликаем нужную ссылку
        self.yandex_result_page.find_right_link(search_text)

        #переход на следующую страницу
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[1])
       
        #вводим описание проекта
        self.pastebin_head_page.input_description(self.content)

        #открываем список возможных языков
        self.pastebin_head_page.open_language_selection()

        #выбираем нужный язык
        self.pastebin_head_page.choose_right_language(self.language)

        #вводим имя 
        self.pastebin_head_page.input_name(self.name)
        
        #нажимаем кнопку регистрации
        self.pastebin_head_page.press_end_button()

        #проверяем язык
        self.pastebin_second_page.language_check(self.language)

        #проверяем описание
        self.pastebin_second_page.content_check(self.content)

        #проверяем имя
        self.pastebin_second_page.name_check(self.name)
        
    def tearDown(self):
        self.driver.close()
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[0])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() 

if __name__ == '__main__':
    unittest.main()
