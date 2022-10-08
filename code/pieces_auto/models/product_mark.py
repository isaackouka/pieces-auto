from odoo import models, fields, api

class mark(models.Model):
    _name = 'mark.auto'
    _description = 'pieces_auto mark'
    _order = 'name asc'

    name = fields.Char()
    image = fields.Image() 
