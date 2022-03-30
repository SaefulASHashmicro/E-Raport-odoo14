# -*- coding: utf-8 -*-
# from odoo import http


# class ERaport(http.Controller):
#     @http.route('/e_raport/e_raport/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/e_raport/e_raport/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('e_raport.listing', {
#             'root': '/e_raport/e_raport',
#             'objects': http.request.env['e_raport.e_raport'].search([]),
#         })

#     @http.route('/e_raport/e_raport/objects/<model("e_raport.e_raport"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('e_raport.object', {
#             'object': obj
#         })
