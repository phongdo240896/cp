# file: main.py
import requests
from bs4 import BeautifulSoup

def get_stock_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        # Tìm giá hiện tại
        price = soup.select_one('.price').text.strip()
        change = soup.select_one('.price-diff').text.strip()
        percent = soup.select_one('.price-percent').text.strip()

        return {
            'Giá': price,
            'Thay đổi': change,
            'Phần trăm': percent
        }
    except Exception as e:
        return {'Lỗi': str(e)}

if __name__ == "__main__":
    url = "https://cafef.vn/du-lieu/hose/fpt-cong-ty-co-phan-fpt.chn"
    result = get_stock_price(url)
    print(result)
