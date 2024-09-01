#import 
import mysql.connector
import unittest


#mysql setup


#simple way to test connection
#cur = db.cursor()
#query_string = "SELECT * FROM election WHERE election_title = '%s'"%("0001")
#cur.execute(query_string)
#results = cur.fetchall()
#print(results)

# unit test with db
class TestDb(unittest.TestCase):
    connection = None
    def setUp(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Fundamentals09!',
            database='vote_info'
        )
    
    def tearDown(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def test_connection(self):
        self.assertTrue(self.connection.is_connected())

if __name__ == '__main__':
    unittest.main()