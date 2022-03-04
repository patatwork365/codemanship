import unittest

from src.cd import CD
from src.warehouse import Warehouse

class CDWarehouse(unittest.TestCase):

    def test_match_cd_artist(self):
        cd = CD(artist='Foo', title='Bar')
        cd_dict = {cd: 3}

        warehouse = Warehouse(cd_dict)
        self.assertEqual('Match found.', warehouse.search(artist='Foo'))


    def test_match_cd_title(self):
        cd = CD(artist='Foo', title='Bar')
        cd_dict = {cd: 3}

        warehouse = Warehouse(cd_dict)
        self.assertEqual('Match found.', warehouse.search(title='Bar'))


    def test_no_match_cd_artist(self):
        cd = CD(artist='Foo', title='Bar')
        cd_dict = {cd: 3}

        warehouse = Warehouse(cd_dict)
        self.assertEqual('Match not found.', warehouse.search(artist='Baz'))


    def test_no_match_cd_title(self):
        cd = CD(artist='Foo', title='Bar')
        cd_dict = {cd: 3}

        warehouse = Warehouse(cd_dict)
        self.assertEqual('Match not found.', warehouse.search(title='Baz'))
