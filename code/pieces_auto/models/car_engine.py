from odoo import models, fields, api

class engine(models.Model):
    _name          = 'engine.auto'
    _description   = 'engine auto'

    name           = fields.Char()
    model_ids      = fields.Many2many('model.auto')
