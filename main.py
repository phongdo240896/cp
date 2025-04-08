from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Cấu hình headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Khởi tạo trình duyệt
driver = webdriver.Chrome(options=chrome_options)

# Mở trang
url = "https://cafef.vn/du-lieu/hose/fpt-cong-ty-co-phan-fpt.chn"
driver.get(url)

# Chờ trang tải
time.sleep(5)

# Lấy giá cổ phiếu FPT
try:
    price_element = driver.find_element(By.CSS_SELECTOR, ".price")
    price = price_element.text
    print(f"Giá cổ phiếu FPT: {price}")
except:
    print("Không tìm thấy giá trong HTML.")

# Đóng trình duyệt
driver.quit()
