import asyncio
from imports import *
import pprint as pp


class GetDataByBrowserSession:

    async def init(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)

    def open_new_tab(self, url):
        self.driver.execute_script(f'window.open("{url}");')

    def close(self):
        self.driver.quit()

    async def find_element_with_digits(self, data):
        for element in data:
            for char in element:
                if char.isdigit():
                    return element
        return 'МФУ недоступно'

    async def is_printer_available(self, printer_address):
        return ping(printer_address) is not None

    async def get_data_arm_1(self, url1):
        self.driver.get(url1)
        elems = self.driver.find_elements(By.CLASS_NAME, 'style363')
        elem_list = [elem.text for elem in elems]
        return elem_list

    async def get_data_arm_2(self, url2):
        self.open_new_tab(url2)
        elems = self.driver.find_elements(By.CLASS_NAME, 'style363')
        elem_list = [elem.text for elem in elems]
        return elem_list


def calculate_time_async(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции '{func.__name__}': {end_time - start_time:.5f} секунд")
        return result

    return wrapper


@calculate_time_async
async def main():
    session = GetDataByBrowserSession()
    await session.init()
    if await session.is_printer_available(url1):
        arm1 = await session.find_element_with_digits(await session.get_data_arm_1(url1))
        arm2 = await session.find_element_with_digits(await session.get_data_arm_2(url2))
    else:
        arm1 = None
        arm2 = None
    session.close()
    pp.pp(f'Окно1 = {arm1}, Окно2 = {arm2}')


if __name__ == "__main__":
    asyncio.run(main())
