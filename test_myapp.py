# -*- coding: utf-8 -*-

import unittest
import myapp
from unittest import mock
from myapp import app
from flask_mysqldb import MySQL

#Documentation: https://docs.python.org/3/library/unittest.html

class TestMyApp(unittest.TestCase):
    
    #setUpClass is ran once before all the tests
    @classmethod
    def setUpClass(cls):
        pass
    
    #tearDownClass is ran once after all the tests
    @classmethod
    def tearDownClass(cls):
        pass
    
    #setUp is ran before every single test
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        self.test = app.test_client(self)
        #self.mysql = MySQL(app)
    
    #tearDown is ran after every single test 
    def tearDown(self):
        pass
    
    #Basic test to make sure pages available normally by direct path
    #return a 200 status
    def test_1_200(self):
        response = self.test.get("/")
        print("\nHome page available from 127.0.0.1:5000/: {}".format(response.status_code))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Election News", response.data)

        login = self.test.get("/login")
        print("Login page available from 127.0.0.1:5000/login: {}".format(login.status_code))
        self.assertEqual(login.status_code, 200)
        self.assertIn(b"Login to Elect-me", login.data)

        sign_up = self.test.get("/sign-up")
        print("Sign-up page available from 127.0.0.1:5000/sign-up: {}".format(sign_up.status_code))
        self.assertEqual(sign_up.status_code, 200)
        self.assertIn(b"Create Account", sign_up.data)

        forgot_p = self.test.get("/forgotpassword")
        print("Forgot Password page available from 127.0.0.1:5000/forgotpassword: {}".format(forgot_p.status_code))
        self.assertEqual(forgot_p.status_code, 200)
        self.assertIn(b"What is your Voter ID", forgot_p.data)

        forgot_id = self.test.get("/forgotvoterid")
        print("Forgot VoterID page available from 127.0.0.1:5000/forgotvoterid: {}".format(forgot_id.status_code))
        self.assertEqual(forgot_id.status_code, 200)
        self.assertIn(b"What is your Email", forgot_id.data)

    def test_2_signup(self):
        email = "test@gmail.com"
        print("Testing Sign-up Post")
        response = self.test.post("/sign-up", data=dict(age="18", fname="testf", lname="testl",
                                                        email=email, addy="test",
                                                        zip="test", id1="test", id2="test",
                                                        id1type="test", id2type="test",
                                                        s1="test", s2="test", s3="test", pword="testpass123"))
        #conn = self.mysql.connector.connect(user='root', password='Fundamentals09!', host='localhost', database='vote_info')
        #cur = conn.cursor
        #cur = self.mysql.connection.cursor
        #query_string="SELECT first_name FROM users WHERE email=%s"
        #cur.execute(query_string,[email])
        #results = cur.fetchall()
        #self.assertEqual(results.length(), 1)
        
        
        
        
        
    #HELPER FUNCTIONS
        
    #signup takes all the inputs for signing up a new user and sends the post request
    def signup(self, age, fname, lname, email, addy, zip, id1, id2):
        return self.test.post('/sign-up', data=dict(age=age, fname=fname, lname=lname,
                                                    email=email, addy=addy, zip=zip, 
                                                    id1=id1, id2=id2))
        
        
if __name__ == '__main__':
    unittest.main()
