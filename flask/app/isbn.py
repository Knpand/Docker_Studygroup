import requests
import time

RAKUTEN_BOOKS_API_URL = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
RAKUTEN_APP_ID = "1022405786460309384"
RAKUTEN_BOOKS_G_API_URL="https://app.rakuten.co.jp/services/api/IchibaGenre/Search/20120723?applicationId=[アプリID]&genreId=0"

class RAKUTENAPI:
  def get_book_info_by_isbn(self, isbn):
    time.sleep(0.5)
    response = requests.get("{}?applicationId={}&isbn={}".format(RAKUTEN_BOOKS_API_URL, RAKUTEN_APP_ID, isbn))
    print("{}?applicationId={}&amp;isbnjan={}".format(RAKUTEN_BOOKS_API_URL, RAKUTEN_APP_ID, isbn))
    if response.status_code != requests.codes.ok:
      print("Requests failed")
    elif response.json()["count"] == 0:
      print("No book found: isbn {}".format(isbn))
    else:
      print("Book found: {}".format(response.json()["Items"][0]["Item"]["author"]))
      info = response.json()["Items"][0]["Item"]
      # data = {
      #   "title" : info["title"],
      #   "ISBN" : info["isbn"],
      #   "author" : info["author"],
      #   "author_kana" : info["authorKana"],
      #   "publisher" : info["publisherName"],
      #   "overview" : info["itemCaption"],
      #   "image_url" : info["largeImageUrl"]
      # }
      data = []
      data.append(info["title"])
      data.append(info["isbn"])
      data.append(info["author"])
      data.append(info["authorKana"])
      data.append(info["publisherName"])
      data.append(info["itemCaption"])
      data.append(info["largeImageUrl"])
      
      return data
