# -*- coding: utf-8 -*-
from odoo import http

# class ScaffoldProject(http.Controller):
#     @http.route('/scaffold_project/scaffold_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scaffold_project/scaffold_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scaffold_project.listing', {
#             'root': '/scaffold_project/scaffold_project',
#             'objects': http.request.env['scaffold_project.scaffold_project'].search([]),
#         })

#     @http.route('/scaffold_project/scaffold_project/objects/<model("scaffold_project.scaffold_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scaffold_project.object', {
#             'object': obj
#         })