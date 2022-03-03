# -*- coding: utf-8 -*-
from odoo import http

# class CclStateTax(http.Controller):
#     @http.route('/ccl_state_tax/ccl_state_tax/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ccl_state_tax/ccl_state_tax/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ccl_state_tax.listing', {
#             'root': '/ccl_state_tax/ccl_state_tax',
#             'objects': http.request.env['ccl_state_tax.ccl_state_tax'].search([]),
#         })

#     @http.route('/ccl_state_tax/ccl_state_tax/objects/<model("ccl_state_tax.ccl_state_tax"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ccl_state_tax.object', {
#             'object': obj
#         })