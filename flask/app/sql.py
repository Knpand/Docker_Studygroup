import mysql.connector as mysql
import sqlalchemy as db
import time
import datetime

dt_now = datetime.datetime.now()


user_name = "light"
password = "light"
host = "database"  # docker-composeで定義したMySQLのサービス名
database_name = "books_db"

conn = mysql.connect(
    host="database",
    user="light",
    passwd="light",
    port=3306,
    database="books_db"
)
class sql_arg:
    def insert_book_data(self, values):
        conn.ping(reconnect=True)
        cur = conn.cursor()
        sql = "insert into books values (NULL ,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,values)
        conn.commit()

    def get_all_book_data(self):
        conn.ping(reconnect = True)
        cur = conn.cursor()
        sql = "select title,author,author_kana,publisher,overview from books"
        cur.execute(sql)
        book_data = cur.fetchall()
        return book_data
    
    def get_rented_book_data(self,student_id):
        conn.ping(reconnect = True)
        cur = conn.cursor()
        sql = "select bookid from rent_hist where renterid = %s"
        cur.execute(sql,student_id)
        result_id = cur.fetchall()
        rented_books = []

        for i in range(len(result_id)):
            sql = "select title, author, author_kana, publisher, overview from books where id = ?"
            cur.execute(sql,result_id[i])
            rented_books.append(cur.fetchall())
        
        return rented_books
    
    def return_book(self,id,isbn):
        conn.ping(reconnect = True)
        cur = conn.cursor()
        sql = "select id from books where ISBN="+str(isbn[0])
        cur.execute(sql)
        result_name = cur.fetchall()
        # print(result_name)
        rented = []
        rentable = []
        for result in result_name:

            # sql = "select id from rent_hist "
            sql = "select id from rent_hist where bookid="+str(result[0]) + "&& returned = "+str('0')

            cur.execute(sql)
            search_result = cur.fetchall()
            print(search_result)
            if search_result != []:
                # continue
            # else:
                print("returning"+str(search_result[0][0]))
                sql = "update rent_hist set returned = 1 where id = "+str(search_result[0][0]) + "&& renterid = "+str(id)
                # sql1 = "UPDATE `rent_hist` SET `returned` = '1' WHERE `rent_hist`.`id` = 29"
                cur.execute(sql)
                conn.commit()

    def get_name(self,stdid):
        conn.ping(reconnect = True)
        cur = conn.cursor()
        sql = "select name from students where id="+str(stdid)
        cur.execute(sql)
        result_name = cur.fetchall()
        return result_name   

    def get_userid(self,email):
        conn.ping(reconnect = True)
        cur = conn.cursor()
        sql = 'select id from students where email= "'+email+'"'
        cur.execute(sql)
        result_name = cur.fetchall()
        print(result_name)
        return result_name[0][0]   
    
    def get_bookinfo(self,isbn):
        conn.ping(reconnect = True)
        cur = conn.cursor()
        sql = "select name from books where ISBN="+str(isbn)
        cur.execute(sql)
        result_name = cur.fetchone()
        sql = "select author from books where ISBN="+str(isbn)
        cur.execute(sql)
        result_author = cur.fetchone()
        sql = "select publisher from books where ISBN="+str(isbn)
        cur.execute(sql)
        result_publisher = cur.fetchone()
        return result_name, result_author, result_publisher



    def get_userinfo(self,stdid):
        renthistory_books = []
        rented_books=[]
        conn.ping(reconnect = True)
        cur = conn.cursor()

        sql = "select id from rent_hist where renterid = "+str(stdid) + "&& returned = 1"
        cur.execute(sql)
        history = cur.fetchall()
        sql = "select id from rent_hist where renterid = "+str(stdid)+ "&& returned = 0"
        cur.execute(sql)
        cur_rent = cur.fetchall()
        print("current{}  history{}".format(cur_rent,history))
        for rents in history:
            sql = "select bookid from rent_hist where id = "+str(rents[0])
            cur.execute(sql)
            history_books = cur.fetchone()
            print("history book {}".format(history_books))
        
        for rents in cur_rent:
            sql = "select bookid from rent_hist where id = "+str(rents[0])
            print(sql)
            cur.execute(sql)
            cur_rent_books = cur.fetchone()
            sql = "select title from books where id = "+str(cur_rent_books[0])
            cur.execute(sql)
            cur_rent_book_title = cur.fetchone()
            print("rented book {}".format(cur_rent_book_title[0]))
            sql = "select author from books where id = "+str(cur_rent_books[0])
            cur.execute(sql)
            cur_rent_book_author = cur.fetchone()
            print("rented book {}".format(cur_rent_book_author[0]))
            sql = "select publisher from books where id = "+str(cur_rent_books[0])
            cur.execute(sql)
            cur_rent_book_publisher = cur.fetchone()
            print("rented book {}".format(cur_rent_book_publisher[0]))
            book = {'title': cur_rent_book_title[0],'author':cur_rent_book_author[0],'publisher':cur_rent_book_publisher[0]}
            print(book)
            rented_books.append(book)

        for rents in history:
            sql = "select bookid from rent_hist where id = "+str(rents[0])
            print(sql)
            cur.execute(sql)
            cur_rent_books = cur.fetchone()
            sql = "select title from books where id = "+str(cur_rent_books[0])
            cur.execute(sql)
            cur_rent_book_title = cur.fetchone()
            print("rented book {}".format(cur_rent_book_title[0]))
            sql = "select author from books where id = "+str(cur_rent_books[0])
            cur.execute(sql)
            cur_rent_book_author = cur.fetchone()
            print("rented book {}".format(cur_rent_book_author[0]))
            sql = "select publisher from books where id = "+str(cur_rent_books[0])
            cur.execute(sql)
            cur_rent_book_publisher = cur.fetchone()
            print("rented book {}".format(cur_rent_book_publisher[0]))
            book = {'title': cur_rent_book_title[0],'author':cur_rent_book_author[0],'publisher':cur_rent_book_publisher[0]}
            print(book)
            renthistory_books.append(book)
        
        cur.close()
        print(renthistory_books)
        print(rented_books)
       
        return rented_books, renthistory_books       


    
    def rent_book(self, id, isbn):
        conn.ping(reconnect = True)
        cur = conn.cursor()
        sql = "select id from books where ISBN="+str(isbn)
        cur.execute(sql)
        result_name = cur.fetchall()
        # print(result_name)
        rented = []
        rentable = []
        for result in result_name:
            sql = "select bookid from rent_hist where bookid="+str(result[0]) + "&& returned = 0"
            cur.execute(sql)
            search_result = cur.fetchall()
            if search_result == []:
                rentable.append(result[0])
            else:
                rented.append(search_result[0][0])
        d_today = "{0}{1:02d}{2:02d}".format(dt_now.year,dt_now.month,dt_now.day)
        returndate = datetime.date.today() + datetime.timedelta(weeks = 2)
        d_return = "{0}{1:02d}{2:02d}".format(returndate.year,returndate.month,returndate.day)
        sql = "insert into rent_hist values (NULL ,{},{},{},{},0)".format(rentable[0],str(id),d_return,d_today)
        cur.execute(sql)
        conn.commit()



       

# conn.ping(reconnect=True)
# print(conn.is_connected())


# cur.execute("SELECT * FROM books")
# result = cur.fetchall()
# print(result)