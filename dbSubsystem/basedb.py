import mysql.connector
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--sqlpass', dest='sqlpass', type=str, help='SQL Password')
args = parser.parse_args()

class BaseDB:
     def __init__(self):
          self.db = mysql.connector.connect(
                         host="localhost",
                         user="root",
                         password=args.sqlpass
                    )
          self.cursor = self.db.cursor()
          self.cursor.execute("create database IF NOT EXISTS gol_db")
          self.cursor.execute('USE gol_db;')
          self.cursor.execute("create table IF NOT EXISTS games (name varchar(70), game varchar(56));")
          self.db.commit()
          print('DB Subsystem initialised...')

     def executesql(self, s):
          try:
               self.cursor.execute('USE gol_db;')
               self.cursor.execute(s)
               res=self.cursor.fetchall()
               self.db.commit()
               return res
          except Exception as e:
               print('BaseDBSubsystem had an error.')
               print(e)