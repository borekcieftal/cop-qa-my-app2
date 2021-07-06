from flask import Flask, render_template
import json
import requests
import sqlite3
import unittest

app = Flask(__name__)


@app.route('/api2/purchases')
def getPurchases():
    return purchaseDatabase.getPurchases()


class PurchaseDatabase():
    def getPurchases(self):
        cursor = sqlcon.execute("SELECT item_id, cust_id, date from PURCHASES")
        json = "["
        for d in cursor:
            json = json + '{"item_id":"' + str(d[0]) + '","cust_id":"' + str(d[1]) + '","date":"' + d[2] + '"},'
        json = json[:-1] + "]"
        return json


if __name__ == "__main__":
    # Prepare in memory database.
    global sqlcon
    sqlcon = sqlite3.connect(':memory:', check_same_thread=False)
    cursor = sqlcon.cursor()
    cursor.execute("""
                    create table if not exists PURCHASES(
                        item_id integer,
                        cust_id integer,
                        date text);
                    """)
    cursor.execute("""
                    insert into PURCHASES(item_id, cust_id, date) values
                    (1, 1, '301221'),
                    (1, 2, '151121'),
                    (2, 3, '301221');
                    """)
    sqlcon.commit()

    # test comment
    # second test
    # third test

    global purchaseDatabase
    purchaseDatabase = PurchaseDatabase()
    app.run(host="0.0.0.0", port=5002)
