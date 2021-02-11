import MySQLdb.cursors
from flask import (Flask, request, render_template)
mysql = MySQLdb.Connection(user="aheisleycook",passwd="A7147084155o!",port=3306, host="localhost")
my  =  mysql.cursor()
def Load_Sql(filename):
    with open(filename + ".sql", "r") as  sql:
        query = sql.readline()
        for cmd in query:
            my.execute(cmd)


Load_Sql("query")