# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_tax_report(models.Model):
    _inherit = 'sale.order'

    def action_print_delivery_note(self):
        return self.env.ref('sale_report.tax_print_delivery_note_pdf').report_action(self)
