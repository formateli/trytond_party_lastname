# This file is part of party_lastname module.
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

        parties = Party.search([('rec_name', 'like', '%Just%')])
        self.assertEqual(len(parties), 1)
        self.assertEqual(parties[0].name, party.name)
        parties = Party.search([('rec_name', 'like', '%Last%')])
        self.assertEqual(len(parties), 1)
        self.assertEqual(parties[0].name, party_ln.name)
        parties = Party.search([('rec_name', 'like', '%Name%')])
        self.assertEqual(len(parties), 2)


del ModuleTestCase
