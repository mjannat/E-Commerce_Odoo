# -*- coding: utf-8 -*-

from odoo import models, fields, api

class custom_report(models.Model):
    _inherit = 'sale.order'

    def action_print_delivery_note(self):
        return self.env.ref('sale_report.print_delivery_note_pdf').report_action(self)

