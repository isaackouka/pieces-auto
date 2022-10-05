from odoo import models, fields, api

class mark(models.Model):
    _name          = 'pieces_auto.mark'
    _description   = 'pieces_auto.mark'

    name           = fields.Char()
