import os

from dotenv import load_dotenv

load_dotenv()
import constants as Consts
from crawl import Crawler


def main():
    crawler = Crawler(api_key=os.getenv('API_KEY'))  # Put your API key in .env file
    for key, value in Consts.CATEGORY.items():
        print(f"Category: {key}")
        for token in value:
            print(f"Token: {token}")
            crawler.download_historical_data(category="crypto", symbol="DYDX", location='./data')
            print("Lastest data: ", crawler.get_lastest_data(category="crypto", symbol="BTCUSDT"))


if __name__ == '__main__':
    main()
