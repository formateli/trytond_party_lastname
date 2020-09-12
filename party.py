# This file is part of party_lastname module.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval

__all__ = ['Party']


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    last_name = fields.Char('Last name', select=True,
        states={
            'readonly': ~Eval('active', True),
        }, depends=['active'])

    def get_full_name(self, name):
        res = super(Party, self).get_full_name(name)
        if self.last_name:
            res += ' ' + self.last_name
        return res

    def get_rec_name(self, name):
        res = super(Party, self).get_rec_name(name)
        if self.last_name:
            res += ' ' + self.last_name
        return res

    @classmethod
    def search_rec_name(cls, name, clause):
        res = super(Party, cls).search_rec_name(name, clause)
        res.append(
            ('last_name',) + tuple(clause[1:])
            )
        return res
