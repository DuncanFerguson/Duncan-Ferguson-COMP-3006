# first need to make sure connector is installed:
#  pip install mysql-connector-python

import mysql.connector

class DBTest():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            user='root',
            passwd='64d^)4H6zsQ}',
            database='henry_books',
            host='127.0.0.1')

        self.mycur = self.mydb.cursor()

    def close(self):
        self.mydb.commit()
        self.mydb.close()

    def getCandy(self):
        
        # Perform the query
        sql = "SELECT * FROM henry_author;"
        self.mycur.execute(sql);

        # Display the results
        for row in self.mycur:
            cust_id = row[0]
            name = row[1]
            print("custID: " + str(cust_id) + ", name " + name);


# Testing code
test = DBTest()
# test.getCandy()
test.close()
