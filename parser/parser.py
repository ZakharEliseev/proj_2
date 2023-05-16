from imports import *


def calculate_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции '{func.__name__}': {end_time - start_time:.5f} секунд")
        return result
    return wrapper


def get_data_arm_1(url1) -> list:
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(url1)
    elems = driver.find_elements(By.CLASS_NAME, 'style363')
    elem_list = [elem.text for elem in elems]
    driver.quit()
    return elem_list


def get_data_arm_2(url2):
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(url2)
    elems = driver.find_elements(By.CLASS_NAME, 'style363')
    elem_list = [elem.text for elem in elems]
    driver.quit()
    return elem_list


def get_data_arm_3_by_bs4(url3):
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(url3)
        elem = driver.find_element(By.ID,'DEVICE')
        driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(driver, 60)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
    finally:
        driver.close()
        driver.quit()
    return result.strip()


def get_data_arm_4_by_bs4(url4) -> str:
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(url4)
        elem = driver.find_element(By.ID,'DEVICE')
        driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
    finally:
        driver.close()
        driver.quit()
    return result.strip()


def get_data_arm_5_by_bs4(url5):
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(url5)
        elem = driver.find_element(By.ID,'DEVICE')
        driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(driver, 60)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
    finally:
        driver.close()
        driver.quit()
    return result.strip()


def get_data_arm_6_by_bs4(url6):
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(url6)
        elem = driver.find_element(By.ID,'DEVICE')
        driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(driver, 60)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
    finally:
        driver.close()
        driver.quit()
    return result.strip()


def get_data_arm_adm_by_bs4(url7):
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(url7)
        elem = driver.find_element(By.ID,'DEVICE')
        driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(driver, 60)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
    finally:
        driver.close()
        driver.quit()
    return result.strip()


def get_data_arm_it_by_bs4(url8):
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(url8)
        elem = driver.find_element(By.ID,'DEVICE')
        driver.execute_script('arguments[0].click();', elem)
        wait = WebDriverWait(driver, 60)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style="height: 20px; line-height: 20px;"]')))
        soup = bs(driver.page_source, 'html.parser')
        result = soup.find_all('div', attrs={'style': 'height: 20px; line-height: 20px;'})[0].get_text()
    finally:
        driver.close()
        driver.quit()
    return result.strip()


def get_data_bak_1(url10):
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(url1)
    elems = driver.find_elements(By.CLASS_NAME, 'style363')
    elem_list = [elem.text for elem in elems]
    driver.quit()
    return elem_list


def get_data_bak_2(url9):
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(url1)
    elems = driver.find_elements(By.CLASS_NAME, 'style363')
    elem_list = [elem.text for elem in elems]
    driver.quit()
    return elem_list


def find_element_with_digits(data) -> str:
    for element in data:
        for char in element:
            if char.isdigit():
                return element
    return 'МФУ недоступно'


@calculate_time
def main():
    print(arm1 := find_element_with_digits(get_data_arm_1(url1)))
    # arm2 = find_element_with_digits(get_data_arm_2(url2))
    # arm3 = get_data_arm_3_by_bs4(url3)
    # arm4 = get_data_arm_4_by_bs4(url4)
    # arm5 = get_data_arm_5_by_bs4(url5)
    # arm6 = get_data_arm_6_by_bs4(url6)
    # arm7 = get_data_arm_6_by_bs4(url7)
    # arm8 = get_data_arm_6_by_bs4(url8)
    # arm10 = find_element_with_digits(get_data_bak_1(url10))
    # arm9 = find_element_with_digits(get_data_bak_2(url9))
    # pp.pprint(f'Окно1 = {arm1}, Окно2 = {arm2}, Окно3 = {arm3}, Окно4 = {arm4}, Окно5 = {arm5}, '
    #           f'Окно6 = {arm6}, Админы = {arm7}, ИТ = {arm8}, Бэк1 = {arm9} Бэк2 = {arm10}')


if __name__ == '__main__':
    main()