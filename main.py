import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import sys
import argparse


def main():
    load_dotenv()
    bitly_token = os.getenv("BITLY_TOKEN")
    headers = {"Authorization": f"Bearer {bitly_token}"}
    link = parse_arguments()
    if is_bitlink(headers, link):
        try:
            total_clicks = count_clicks(headers, link)
            print(f"По вашей ссылке прошли {total_clicks} раз(а)")
        except requests.exceptions.HTTPError:
            print("Указана длинная ссылка или неверный адрес")
    else:
        try:
            bitlink = shorten_link(headers, link)
            print(f"Битлинк: {bitlink}")
        except requests.exceptions.HTTPError:
            print("Указан неверный адрес")


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser_argument = parser.add_argument ('-l', '--link', required=True)
    argument = parser.parse_args()
    return argument.link


def is_bitlink(headers, link):
    parsed_url = urlparse(link)
    parsed_link = f'{parsed_url.netloc}{parsed_url.path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_link}'
    response = requests.get(url, headers=headers)
    return response.ok


def count_clicks(headers, link):
    parsed_url = urlparse(link)
    parsed_link = f'{parsed_url.netloc}{parsed_url.path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_link}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    total_clicks = response.json()['total_clicks']
    return total_clicks


def shorten_link(headers, link):
    url = "https://api-ssl.bitly.com/v4/shorten"
    response = requests.post(url, json={"long_url": link}, headers=headers)
    response.raise_for_status()
    short_link = response.json()['id']
    return short_link


if __name__ == '__main__':
    main()
