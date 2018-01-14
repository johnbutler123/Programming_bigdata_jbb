####See script processing.py which contains the functions used for testing as used for populating the class constructor
###The key critical check is the number of comment = 422 - Thii matches the number of rows in all the relevant csv files
## process_changes(6a,7,8,9,10,11,12,13,14,15).csv

##Also thoroughly tested the changes with path references, Modify =  1186, Delete = 767 and Add = 1056 - all tested correctly
##These values were independently checked on the source file. and are also contained in "report" worksheet in workbook "7-8-9-AddDeletesModsByAuthor"
##They are also consistent with those values in "report" worksheet in workbook "7-8-9-AddDeletesModsByAuthor" 

##Also ran test for total pathlines - produced result of 3011.  
##Surprisingly this is two higher than the sum of Add, Delete and Modify ie 1056 + 767 + 1186 = 3009 
## Discovered that the unaccounted for 2 items relate to path "R" - see test below
## This brought home to me the importance of unit testing - however, because the value of 2 is so small as a proportion of 2011 I chose to ignore

import unittest

changes_file = 'changes_python.txt'
data = [line.strip() for line in open(changes_file, 'r')]
sep = 72*'-'

#from processing import get_commits, read_file, countpathlines, countgradle, countmodify, countdelete, countadd, countR
from process_changes_class import Commit

class TestCommits(unittest.TestCase):

    # def setUp(self):
        # self.data = read_file('changes_python.txt')
        
        
    def test_countpathlines(self):
        self.commits = Commit()
        self.assertEqual(3011, self.commits.countpathlines())

        
    def test_countgradle(self):
        self.commits = Commit()    
        self.assertEqual(100,self.commits.countgradle())
        
    def test_countmodify(self):
        self.commits = Commit()
        self.assertEqual(1186,self.commits.countmodify())        
        
    def test_countdelete(self):
        self.commits = Commit()    
        self.assertEqual(767,self.commits.countdelete())

    def test_countadd(self):
        self.commits = Commit()   
        self.assertEqual(1056,self.commits.countadd())
        
    def test_r(self):
        self.commits = Commit()       
        self.assertEqual(2,self.commits.countR())

    def test_countauthor(self):
        self.commits = Commit()   
        self.assertEqual(10,self.commits.countauthor())

    def test_get_commits(self):
        self.commits = Commit()   
        self.assertEqual(422,self.commits.get_commits(data))         
        


if __name__ == '__main__':
    unittest.main()
