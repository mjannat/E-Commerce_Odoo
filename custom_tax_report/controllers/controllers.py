# -*- coding: utf-8 -*-
# from odoo import http


# class CustomTaxReport(http.Controller):
#     @http.route('/custom_tax_report/custom_tax_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_tax_report/custom_tax_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_tax_report.listing', {
#             'root': '/custom_tax_report/custom_tax_report',
#             'objects': http.request.env['custom_tax_report.custom_tax_report'].search([]),
#         })

#     @http.route('/custom_tax_report/custom_tax_report/objects/<model("custom_tax_report.custom_tax_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_tax_report.object', {
#             'object': obj
#         })
