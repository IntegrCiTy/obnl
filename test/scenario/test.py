from scenario.db import *

connect = PostgreSQLConnectionInfo( 
	user = 'postgres', 
	pwd = 'postgres', 
	host = 'localhost', 
	port = '5432', 
	dbname = 'testdb'
	)

cleanup_db( connect )