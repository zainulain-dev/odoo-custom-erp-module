# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_custom_notes = fields.Text(string="Custom Internal Notes")
    x_total_weight = fields.Float(
        string="Total Weight",
        compute='_compute_total_weight',
        store=True,
        help="Total weight computed at 10.0 per order line."
    )

    @api.depends('order_line')
    def _compute_total_weight(self):
        for order in self:
            order.x_total_weight = len(order.order_line) * 10.0
