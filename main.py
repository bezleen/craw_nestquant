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
            crawler.download_historical_data(category=key, symbol=token, location='./data')
            print("Lastest data: ", crawler.get_lastest_data(category=key, symbol=token))


if __name__ == '__main__':
    main()
