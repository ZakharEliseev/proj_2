import pprint

from imports import *


class GetDataByBrowserSession:

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)

    def open_new_tab(self, url):
        self.driver.execute_script(f'window.open("{url}");')

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
        # self.open_new_tab(url1)
        # self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url1)
        elems = self.driver.find_elements(By.CLASS_NAME, 'style363')
        elem_list = [elem.text for elem in elems]
        return elem_list

    def get_data_arm_2(self, url2):
        self.open_new_tab(url2)
        elems = self.driver.find_elements(By.CLASS_NAME, 'style363')
        elem_list = [elem.text for elem in elems]
        return elem_list

    def get_data_arm_3_by_bs4(self, url3):
        self.open_new_tab(url3)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_arm_4_by_bs4(self, url4):
        self.open_new_tab(url4)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_arm_5_by_bs4(self, url5):
        self.open_new_tab(url5)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_arm_6_by_bs4(self, url6):
        self.open_new_tab(url6)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_arm_adm_by_bs4(self, url7):
        self.open_new_tab(url7)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_arm_it_by_bs4(self, url8):
        self.open_new_tab(url8)
        elem = self.driver.find_element(By.ID, 'DEVICE')
        self.driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(self.driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
        return result.strip()

    def get_data_bak_1(self, url9):
        self.open_new_tab(url1)
        elems = self.driver.find_elements(By.CLASS_NAME, 'style363')
        elem_list = [elem.text for elem in elems]
        return elem_list

    def get_data_bak_2(self, url10):
        self.open_new_tab(url10)
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
    if session.is_printer_available(url1):
        arm1 = session.find_element_with_digits(session.get_data_arm_1(url1))
        arm2 = session.find_element_with_digits(session.get_data_arm_2(url2))
    else:
        arm1 = None
        arm2 = None

    session.close()
    pprint.pp(f'Окно1 = {arm1}, Окно2 = {arm2}')


if __name__ == "__main__":
    main()
