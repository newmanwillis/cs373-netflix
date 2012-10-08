'''
Created on Sep 23, 2012

@author: Administrator
'''
#!/usr/bin/env python

# -------------------------------
# projects/Netflix/TestNetflix.py
# Copyright (C) 2012
# Thomas Preli & Newman Willis
# -------------------------------

"""
To test the program:
    % python TestNetflix.py >& TestNetflix.py.out
    % chmod ugo+x TestNetflix.py
    % TestNetflix.py >& TestNetflix.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Netflix import CreateCache, PredictRating, Netflix, getUsers, getMovies 

# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :

    # ----
    # CreateCache
    # ----
    
    def test_CreateCache_1(self):
        CreateCache('zUserTest1.txt','zMovieTest1.txt')
        testUsers = getUsers()
        prototypeMovies = getMovies()
        testMovies = [0] * 2
        testMovies[0] = prototypeMovies[0]
        testMovies[1] = prototypeMovies[1]
        actualUsers = {'1' : 5.0, '2': 3.0}
        actualMovies = [5.0, 1.0]
        self.assert_(testUsers == actualUsers)
        self.assert_(testMovies == actualMovies)
        
    def test_CreateCache_2(self):
        CreateCache('zUserTest2.txt','zMovieTest2.txt')
        testUsers = getUsers()
        prototypeMovies = getMovies()
        testMovies = [0] * 4
        testMovies[0] = prototypeMovies[0]
        testMovies[1] = prototypeMovies[1]
        testMovies[2] = prototypeMovies[2]
        testMovies[3] = prototypeMovies[3]
        actualUsers = {'1' : 5.0, '10034': 4.1546, '2': 3.0, '8901267': 3.787}
        actualMovies = [3.777, 2.5, 4.187976, 3.9823]
        self.assert_(testUsers == actualUsers)
        self.assert_(testMovies == actualMovies)
        
    def test_CreateCache_3(self):
        CreateCache('zUserTest3.txt','zMovieTest3.txt')
        testUsers = getUsers()
        prototypeMovies = getMovies()
        testMovies = [0] * 4
        testMovies[0] = prototypeMovies[0]
        testMovies[1] = prototypeMovies[1]
        testMovies[2] = prototypeMovies[2]
        testMovies[3] = prototypeMovies[3]
        actualUsers = {'1' : 5.0, '10034': 4.1546, '2': 3.0, '8901267': 3.787}
        actualMovies = [3.777, 2.5, 4.187976, 3.9823]
        self.assert_(testUsers == actualUsers)
        self.assert_(testMovies == actualMovies)

    # ----
    # PredictRating
    # ----
            
    def test_PredictRating_1(self):
        userRating = 3.15
        movieRating = 3.65
        testRating = 0.0
        testRating = PredictRating(userRating, movieRating)
        actualRating = 3.4;
        self.assert_(testRating == actualRating)
       
    # ----
    # Netflix
    # ----        
    ''' 
    def test_Netflix_1(self):
        
        b = Netflix()
        
    '''
    
# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."