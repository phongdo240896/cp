from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/')
def get_stock_price():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.get("https://cafef.vn/du-lieu/hose/fpt-cong-ty-co-phan-fpt.chn")

        # Ví dụ đơn giản lấy tiêu đề trang
        title = driver.title
        driver.quit()

        return f"Tiêu đề trang là: {title}"
    except Exception as e:
        return f"Lỗi: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
