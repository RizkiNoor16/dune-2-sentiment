import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from langdetect import detect

def get_movie_rating_letterbox(movie_name:str, number_pages:int):
    """
    Fungsi untuk mendapatkan ulasan film dari situs Letterboxd berdasarkan nama film dan jumlah halaman.

    Args:
    - movie_name (str): Nama film yang akan dicari ulasannya.
    - number_pages (int): Jumlah halaman review yang akan diambil setiap ratingnya.

    Returns:
    - DataFrame: DataFrame berisi informasi ulasan film seperti nama author, tanggal, teks review, bahasa, dan rating bintang.

    """
    Author = []
    Text =[]
    Date = []
    Lang = []
    Star = []
    for star in range (1,6):
        for i in range(1,number_pages+1):
            url = f"https://letterboxd.com/film/{movie_name}/reviews/rated/{star}/by/added/page/{i}/"

            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')

            html = soup.find_all("div", "film-detail-content")

            for links in html :
                author = links.find("strong", "name").text
                Star.append(star)
                Author.append(author)
                # print(author)
                date = links.find("span", "_nobr").text
                Date.append(date)
                # print(date)
                text_all = links.find_all("div", "body-text -prose collapsible-text")
                for texts in text_all:
                    try :
                        text = texts.find("p").text
                        lang = detect(text)
                    except :
                        text = None
                        lang = None
                    Text.append(text)
                    Lang.append(lang)


    data = pd.DataFrame({"Author" : Author,
                            "Date" : Date,
                            "Text" :  Text,
                            "Lang" : Lang,
                            "Star" : Star})

    return data