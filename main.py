import requests
from bs4 import BeautifulSoup

def get_stock_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'  # fix tiếng Việt
        soup = BeautifulSoup(response.text, 'html.parser')

        # In HTML ra Render console để test nếu cần
        # print(soup.prettify())

        # Tìm đến block chứa giá hiện tại (dựa trên class nhìn thấy trên web)
        price_block = soup.select_one('.current-price') or soup.select_one('.price')  # fallback

        if price_block:
            price = price_block.text.strip()
            print(f'✅ Giá hiện tại là: {price}')
        else:
            print("❌ Không tìm thấy giá trong HTML.")

    except Exception as e:
        print(f"Lỗi: {str(e)}")

if __name__ == "__main__":
    get_stock_price("https://cafef.vn/du-lieu/hose/fpt-cong-ty-co-phan-fpt.chn")
