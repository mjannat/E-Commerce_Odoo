# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ccl_state_tax(models.Model):

    _description = 'Add State Tax'
    _inherit = 'res.country.state'

    tax = fields.Float()
