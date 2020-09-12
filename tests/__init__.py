# This file is part of party_lastname module.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
try:
    from trytond.modules.party_lastname.tests.test_party_lastname import (
        suite)
except ImportError:
    from .test_party_lastname import (suite)

__all__ = ['suite']
