from selenium.webdriver import Chrome
import time

webdriver = "E:\\chromedriver.exe"

driver = Chrome(webdriver)

# Dept Baby
# pages = 4
# for page in range(1,pages):
#     url = "https://qne.com.pk/baby?1=1&page=" + str(page)
#     driver.get(url)
#     time.sleep(2)
#
#
#     babies = driver.find_elements_by_tag_name('h4')
#     prices = driver.find_elements_by_class_name('productPromoPrice')
#     for baby in babies:
#         print(baby.get_attribute('title'))
#
#     for price in prices:
#         print(price.text)

# Dept Snack Beverages
# pages = 4
# for page in range(1,pages):
#     url = "https://qne.com.pk/snacks-beverages?1=1&page=" + str(page)
#     driver.get(url)
#     time.sleep(2)
#
#
#     babies = driver.find_elements_by_tag_name('h4')
#     prices = driver.find_elements_by_class_name('productPromoPrice')
#     for baby in babies:
#         print(baby.get_attribute('title'))
#
#     for price in prices:
#         print(price.text)

# Dept Grocery
# pages = 9
# for page in range(1,pages):
#     url = "https://qne.com.pk/grocery?1=1&page=" + str(page)
#     driver.get(url)
#     time.sleep(2)
#
#
#     babies = driver.find_elements_by_tag_name('h4')
#     prices = driver.find_elements_by_class_name('productPromoPrice')
#     for baby in babies:
#         print(baby.get_attribute('title'))
#
#     for price in prices:
#         print(price.text)

# Dept Frozen
# pages = 3
# for page in range(1,pages):
#     url = "https://qne.com.pk/frozen?1=1&page=" + str(page)
#     driver.get(url)
#     time.sleep(2)
#
#
#     babies = driver.find_elements_by_tag_name('h4')
#     prices = driver.find_elements_by_class_name('productPromoPrice')
#     for baby in babies:
#         print(baby.get_attribute('title'))
#
#     for price in prices:
#         print(price.text)

# Dept Fresh
# url = "https://qne.com.pk/fresh"
# driver.get(url)
# time.sleep(2)
#
#
# babies = driver.find_elements_by_tag_name('h4')
# prices = driver.find_elements_by_class_name('productPromoPrice')
# for baby in babies:
#     print(baby.get_attribute('title'))
#
# for price in prices:
#     print(price.text)

# Dept Pharmacy
# pages = 19
# for page in range(1,pages):
#     url = "https://qne.com.pk/pharmacy?1=1&page=" + str(page)
#     driver.get(url)
#     time.sleep(2)
#
#
#     babies = driver.find_elements_by_tag_name('h4')
#     prices = driver.find_elements_by_class_name('productPromoPrice')
#     for baby in babies:
#         print(baby.get_attribute('title'))
#
#     for price in prices:
#         print(price.text)

# Dept House Hold
# pages = 4
# for page in range(1,pages):
#     url = "https://qne.com.pk/households-pet-food?1=1&page=" + str(page)
#     driver.get(url)
#     time.sleep(2)
#
#
#     babies = driver.find_elements_by_tag_name('h4')
#     prices = driver.find_elements_by_class_name('productPromoPrice')
#     for baby in babies:
#         print(baby.get_attribute('title'))
#
#     for price in prices:
#         print(price.text)

# Dept Health & Beauty
# pages = 13
# for page in range(1,pages):
#     url = "https://qne.com.pk/beauty-personal-care?1=1&page=" + str(page)
#     driver.get(url)
#     time.sleep(2)
#
#
#     babies = driver.find_elements_by_tag_name('h4')
#     prices = driver.find_elements_by_class_name('productPromoPrice')
#     for baby in babies:
#         print(baby.get_attribute('title'))
#
#     for price in prices:
#         print(price.text)

# Dept Home & Living
# pages = 3
# for page in range(1,pages):
#     url = "https://qne.com.pk/home-living?1=1&page=" + str(page)
#     driver.get(url)
#     time.sleep(2)
#
#
#     babies = driver.find_elements_by_tag_name('h4')
#     prices = driver.find_elements_by_class_name('productPromoPrice')
#     for baby in babies:
#         print(baby.get_attribute('title'))
#
#     for price in prices:
#         print(price.text)


driver.close()