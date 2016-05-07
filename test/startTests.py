'''
Created on Nov 7, 2015

@author: marius
'''
from test.domain.entities import suite_entities
from test.domain.validator import suite_validator
from test.controller.controller import suite_controller
from test.repository.file_repository import suite_file_repository
from test.repository.inmem_repository import suite_inmem_repository
from test.utils.sorting_algorithms import suite_utils
from unittest.suite import TestSuite
import unittest
class TestApp():
    
    @staticmethod
    def run():
        all_suites = [suite_entities(), 
                      suite_validator(), 
                      suite_controller(), 
                      suite_file_repository(),
                      suite_inmem_repository(),
                      suite_utils()]
        ts = TestSuite(all_suites)
        unittest.TextTestRunner(verbosity=2).run(ts)