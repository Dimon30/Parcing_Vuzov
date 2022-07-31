import requests

def get_data(url):
  headers = {
      'authority': 'abitlk.itmo.ru',
      'accept': 'application/json',
      'accept-language': 'ru,en;q=0.9',
      'authorization': 'Basic undefined',
      'origin': 'https://abit.itmo.ru',
      'referer': 'https://abit.itmo.ru/',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.1.806 Yowser/2.5 Safari/537.36'
  }

  params = {
      'program_id': '16021',
      'manager_key': ''
  }

  response = requests.get('https://abitlk.itmo.ru/api/v1/9e2eee80b266b31c8d65f1dd3992fa26eb8b4c118ca9633550889a8ff2cac429/rating/bachelor/budget', params=params, headers=headers)

def main():
  get_data("https://abit.itmo.ru/rating/bachelor/budget/16021")

if __name__ == '__main__':
  main()