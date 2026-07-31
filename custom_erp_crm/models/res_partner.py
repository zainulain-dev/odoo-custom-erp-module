# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_crm_tracking_id = fields.Char(string="CRM Tracking ID")
    x_is_vip_client = fields.Boolean(string="VIP Client", default=False)
