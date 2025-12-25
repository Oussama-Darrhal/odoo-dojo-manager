# -*- coding: utf-8 -*-
# from odoo import http


# class DojoManager(http.Controller):
#     @http.route('/dojo_manager/dojo_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dojo_manager/dojo_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dojo_manager.listing', {
#             'root': '/dojo_manager/dojo_manager',
#             'objects': http.request.env['dojo_manager.dojo_manager'].search([]),
#         })

#     @http.route('/dojo_manager/dojo_manager/objects/<model("dojo_manager.dojo_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dojo_manager.object', {
#             'object': obj
#         })

