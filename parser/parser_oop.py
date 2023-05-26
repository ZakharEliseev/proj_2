import pprint

from imports import *


class GetDataByBrowserSession:

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')  # Запуск в фоновом режиме
        self.driver = webdriver.Firefox(options=options)


    def close(self):
        self.driver.quit()


    def find_element_with_digits(self, data):
        for element in data:
            for char in element:
                if char.isdigit():
                    return element
        return 'МФУ недоступно'


    def is_printer_available(self, printer_address):
        return ping(printer_address) is not None

    def get_data_arm_1(self, url1):
        self.driver.get(url1)
        elems = self.driver.find_elements(By.CLASS_NAME, 'style363')
        elem_list = [elem.text for elem in elems]
        return elem_list

    def get_data_arm_2(self, url2):
        self.driver.get(url2)
        elems = self.driver.find_elements(By.CLASS_NAME, 'style363')
        elem_list = [elem.text for elem in elems]
        return elem_list

    def get_data_arm_3_by_bs4(self, url3):
        self.driver.get(url3)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 1)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_arm_4_by_bs4(self, url4):
        self.driver.get(url4)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_arm_5_by_bs4(self, url5):
        self.driver.get(url5)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_arm_6_by_bs4(self, url6):
        self.driver.get(url6)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_arm_adm_by_bs4(self, url7):
        self.driver.get(url7)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_arm_it_by_bs4(self, url8):
        self.driver.get(url8)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_bak_1(self, url9):
        self.driver.get(url9)
        wait = WebDriverWait(self.driver, 10)
        elems = wait.until(self.driver.find_elements(By.CLASS_NAME, 'style363'))
        elem_list = [elem.text for elem in elems]
        return elem_list

    def get_data_bak_2(self, url10):
        self.driver.get(url10)
        elems = self.driver.find_elements(By.CLASS_NAME, 'style363')
        elem_list = [elem.text for elem in elems]
        return elem_list


def calculate_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции '{func.__name__}': {end_time - start_time:.5f} секунд")
        return result
    return wrapper


@calculate_time
def main():
    session = GetDataByBrowserSession()

    # if session.is_printer_available(arm_bak_1):
    #     arm_bak_1_1 = session.find_element_with_digits(session.get_data_bak_2(bak1))
    # else:
    #     arm_bak_1_1 = None
    #
    # if session.is_printer_available(arm_bak_2):
    #     arm_bak_2_2 = session.find_element_with_digits(session.get_data_bak_2(bak2))
    # else:
    #     arm_bak_2_2 = None

    if session.is_printer_available(address_arm_1):
        arm1 = session.find_element_with_digits(session.get_data_arm_1(url1))
    else:
        arm1 = None

    if session.is_printer_available(address_arm_2):
        arm2 = session.find_element_with_digits(session.get_data_arm_2(url2))
    else:
        arm2 = None

    # if session.is_printer_available(address_arm_3):
    #     arm3 = session.get_data_arm_3_by_bs4(url3)
    # else:
    #     arm3 = None
    #
    # if session.is_printer_available(address_arm_4):
    #     arm4 = session.get_data_arm_4_by_bs4(url4)
    # else:
    #     arm4 = None
    #
    # if session.is_printer_available(address_arm_5):
    #     arm5 = session.get_data_arm_5_by_bs4(url5)
    # else:
    #     arm5 = None
    #
    # if session.is_printer_available(address_arm_6):
    #     arm6 = session.get_data_arm_6_by_bs4(url6)
    # else:
    #     arm6 = None
    #
    # if session.is_printer_available(arm_adm):
    #     arm_adm_7 = session.get_data_arm_adm_by_bs4(url7)
    # else:
    #     arm_adm_7 = None
    #
    # if session.is_printer_available(arm_it):
    #     arm_it_8 = session.get_data_arm_it_by_bs4(url8)
    # else:
    #     arm_it_8 = None

    session.close()
    pp.pp(f'Окно1 = {arm1}, Окно2 = {arm2}')
    # pp.pprint(f'Окно1 = {arm1}, Окно2 = {arm2}, Окно3 = {arm3}, Окно4 = {arm4}, Окно5 = {arm5}, '
    #            f'Окно6 = {arm6}, Админы = {arm_adm_7}, ИТ = {arm_it_8}, Бэк1 = {arm_bak_1_1} Бэк2 = {arm_bak_2_2}')


if __name__ == "__main__":
    main()
