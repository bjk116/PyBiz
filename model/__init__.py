import mysql.connector
from mysql.connector import errorcode

class db():
	"""
		db: connect to a MySQL database
		Arguments:
			user: username for SQL db
			password: password for SQL db
			host: host address for db
			database: name of database
		Returns:
			self.db: connection to the database 
	"""

	cnx = None
	cursor = None

	def __init__(self, user = "", password = "", host = "", database = ""):
		"""

		"""
		try:
			print("at")
			cnx = mysql.connector.connect(user='brian',password='admin', host='127.0.0.1', database='production')
			print("connected")
			# Return a cursor object
			self.cnx = cnx
			print("no issue connecting")
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
				return None
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
				return None
			else:
				print(err)
				return None
		# We don't want to close the connection if nothing is wrong
		# else:
		# 	self.cnx.close()

	def executeQuery(self, query):
		self.cursor = self.cnx.cursor()
		self.cursor.execute(query)
		
		data = []
		for item in self.cursor:
			data.append(item)

		return data

	def close(self):
		self.cursor.close()
		self.cnx.close()



	def updateQuery(self, query):
		# table, columns = [], values = [], whereClause = None
		# if len(columns) != len(values):
		# 	print "we got an error, not same amount of columns and values passed into the function"
		# 	return
		# else:
		# 	setStatement = ""
		# 	for idx, value in columns:
		# 		setStatement += "%s = %s," % ()



		# query = "UPDATE %s SET %s WHERE %s;"%(table, ','.join(columns), '"'+'", "'.join(values)+'"', whereClause)
		print(query)
		self.cursor = self.cnx.cursor()
		self.cursor.execute(query)
		
		self.cnx.commit()
		self.cursor.close()

	def selectAllFromTable(self, table, limit = 1000):
		query = "SELECT * FROM " + table + " LIMIT " + str(limit) +";"
		print(query)

		self.cursor = self.cnx.cursor()
		self.cursor.execute(query)

		data = []
		for item in self.cursor:
			data.append(item)

		self.cursor.close()

		return data

	def getColumnsFromTable(self, table, columns = [], Limit = 1000):

		#They didn't provide columns, let's just return every column
		if len(columns) == 0:
			return self.selectAllFromTable(table)
		elif len(columns) == 1:
			query = "SELECT %s FROM %s" %(columns[0], table)
		else:
			pass

	def insertIntoTable(self, table, columns = [], values = []):
		"""
		Wrapper function used to insert values into a database table
		"""
		query = "INSERT INTO %s (%s) VALUES (%s)"%(table, ','.join(columns), '"'+'", "'.join(values)+'"')
		self.cursor = self.cnx.cursor()
		self.cursor.execute(query)
		print("id of inserted entry: " + str(self.cursor.lastrowid))
		self.cnx.commit()
		self.cursor.close()

	# def selectAllWithWhereFilter(self, tableName = None, whereFilter = "1 = 1"):
	# 	if tableName is None:
	# 		return "No table"
	# 	else:
	# 		query = "SELECT * FROM %s WHERE %s" % (tableName, whereFilter)
	# 		self.cursor = self.cnx.cursor()
	# 		self.cursor.execute(query)

	# def runQuery(self, tableName = None, columns = "*", whereClause = None, orderBy = None, groupBy = None, having = None):
	# 	"""
	# 	runQuery: this will be made to replace all other functions eventually
	# 	runQuery: allows running simple wherefilter clause arguments
	# 	Args:

	# 	Returns:
	# 		data
	# 	"""
	# 	pass