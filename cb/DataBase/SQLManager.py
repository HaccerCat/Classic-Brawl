# made by S.B#9838
import os
import json
import sqlite3
import datetime
import traceback
class DataBase:
	def __init__(self, path):
		self.connection = sqlite3.connect(path)
		self.cursor = self.connection.cursor()
		try:
			self.cursor.execute(f"CREATE TABLE main (LowID integer, auth text, Data json)")
		except:
			pass
	def error(self, e):
		print("an error has occurred, check sqlite3-manager.logs for more info")
		open("sqlite3-manager.logs", "a").write(f"\nan error has occurred at {datetime.datetime.now()}:\n{str(e)}\n--------------------------------------------------")
	def insert(self, key, data):
		try:
			data = {"DATA": data}
			self.cursor.execute(f"INSERT INTO main (auth, Data) VALUES (?, ?)", (key, json.dumps(data, ensure_ascii=False)))
			self.connection.commit()
		except Exception as e:
			DataBase.error(self, traceback.format_exc())
	def load_data(self, key):
		try:
			self.cursor.execute(f"SELECT * from main where auth=?", (key, ))
			loaded = self.cursor.fetchall()
			return json.loads(loaded[0][2])["DATA"]
		except:
			DataBase.error(self, traceback.format_exc())
	def load_all(self):
		tables = [ ]
		try:
			self.cursor.execute("SELECT * from main")
			data = self.cursor.fetchall()
			for db in data:
				db_data = json.loads(db[2])["DATA"]
				tables.append(db_data)
			return tables
		except:
			DataBase.error(self, traceback.format_exc())
	def update(self, key, item, value):
		try:
			self.cursor.execute(f"SELECT * from main where auth=?", (key, ))
			loaded = self.cursor.fetchall()
			loaded = json.loads(loaded[0][2])
			loaded["DATA"][item] = value
			self.cursor.execute(f"UPDATE main SET Data=? WHERE auth=?", (json.dumps(loaded, ensure_ascii=False), key))
			self.connection.commit()
		except:
			DataBase.error(self, traceback.format_exc())
	def delete(self, key):
		self.cursor.execute(f"DELETE from main where auth = {key}")
		self.connection.commit()
	def close(self):
		self.cursor.close()