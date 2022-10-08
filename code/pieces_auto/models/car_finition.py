from odoo import models, fields, api

class finition(models.Model):
    _name          = 'finition.auto'
    _description   = 'finition auto'

    name           = fields.Char()
    model_ids      = fields.Many2many('model.auto')