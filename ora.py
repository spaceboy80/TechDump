	import cx_Oracle
	con = cx_Oracle.connect('username/password@server/dbname')
	print con.version
	cur = con.cursor()
	cur.execute('SELECT * FROM …')
	row = cur.fetchone()
	res = cur.fetchmany(numRows=3)
	cur.prepare('SELECT * FROM dept where deptid = :id')
	cur.execute(None, {'id': 210})
	cur.close()
con.cloe()