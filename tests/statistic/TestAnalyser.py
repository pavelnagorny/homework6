'''
Created on 13 april 2013

@author: vl
'''
import unittest
from statistic.analyser import Analyser


class TestAnalyser(unittest.TestCase):

    def setUp(self):
        import os
        self.__filename = os.path.join(os.path.dirname(__file__),'site.test.log')
        self.__logdata = list()
        self.__logdata.append(["172.0.0.1", "google.com", "ua"])
        self.__logdata.append(["172.0.0.2", "google.com", "en"])
        self.__logdata.append(["172.0.0.2", "google.com/", "en"])
        self.__logdata.append(["172.0.0.1", "google.com/index/", "ru"])
        self.createFile()
        
        self.__uniquevisitors = ["172.0.0.1","172.0.0.2"]
        self.__countries_googlecom = ["ua","en"]
        self.__allvisitors = [2,3]
        self.__homepagevisitorscount = 3
        self.__uniqitemscount = (2,3,3,)
        
        self.__resbycountries = {"ua":1, "en":1, "ru":1}
        self.__resbyvisitors = {"172.0.0.1":2, "172.0.0.2":1}
        
        self.__analyser = Analyser(self.__filename)
        self.__analyser.load_file()

    def tearDown(self):
        import os
        os.remove(self.__filename)

    def createFile(self):
        f = open(self.__filename,'w')
        for r in self.__logdata:
            f.write("\t".join(r))
            f.write("\n")
        f.close()        
        
    def testResourceCountries(self):
        countries = self.__analyser.resource_countries("google.com");
        countries.sort()
        self.__countries_googlecom.sort()
        self.assertEqual(countries, self.__countries_googlecom)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
