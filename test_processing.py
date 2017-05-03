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

from processing import get_commits, read_file, countpathlines, countgradle, countmodify, countdelete, countadd, countR

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.txt')
        
        
    def test_countpathlines(self):
        plines = countpathlines()
        self.assertEqual(3011,plines)
        
    def test_countgradle(self):
        gradle = countgradle()
        self.assertEqual(100,gradle)
        
    def test_countmodify(self):
        modify = countmodify()
        self.assertEqual(1186,modify)
        
    def test_countdelete(self):
        delete = countdelete()
        self.assertEqual(767,delete)

    def test_countadd(self):
        add = countadd()
        self.assertEqual(1056,add)
        
    def test_r(self):
        r = countR()
        self.assertEqual(2,r)
        
        
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])

if __name__ == '__main__':
    unittest.main()
