from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/')
def get_stock_price():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://cafef.vn/du-lieu/hose/fpt-cong-ty-co-phan-fpt.chn")
    html = driver.page_source
    driver.quit()

    if "Công ty Cổ phần FPT" in html:
        return "✅ Đã load trang thành công!"
    else:
        return "❌ Không lấy được dữ liệu!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
