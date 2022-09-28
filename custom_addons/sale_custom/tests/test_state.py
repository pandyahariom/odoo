# -*- coding: utf-8 -*-
from odoo.tests import common
import datetime


class TestModelSaleOrder(common.TransactionCase):
    def test_state_field(self):
        # 10:Deco Addict,
        record = self.env["sale.order"].create(
            {
                "partner_id": 10,
                "pricelist_id": 1,
                "date_order": datetime.datetime.now(),
            }
        )
        # record.some_action()
        self.assertEqual(record.state, "draft")
