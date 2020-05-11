# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool


class PartyLastnameTestCase(ModuleTestCase):
    'Test Party Last name module'
    module = 'party_lastname'

    @with_transaction()
    def test_party_lastname(self):
        pool = Pool()
        Party = pool.get('party.party')

        party, = Party.create([{
                    'name': 'Just Name',
                    }])
        self.assertEqual(party.name, 'Just Name')
        self.assertEqual(party.last_name, None)
        self.assertEqual(party.full_name, 'Just Name')
        self.assertEqual(party.rec_name, 'Just Name')

        party_ln, = Party.create([{
                    'name': 'With',
                    'last_name': 'Last Name',
                    }])
        self.assertEqual(party_ln.name, 'With')
        self.assertEqual(party_ln.last_name, 'Last Name')
        self.assertEqual(party_ln.full_name, 'With Last Name')
        self.assertEqual(party_ln.rec_name, 'With Last Name')


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartyLastnameTestCase))
    return suite
