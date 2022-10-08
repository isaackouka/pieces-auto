from odoo import models, fields, api

class mark(models.Model):
    _name          = 'mark.car.auto'
    _description   = 'mark car auto'

    name           = fields.Char()
