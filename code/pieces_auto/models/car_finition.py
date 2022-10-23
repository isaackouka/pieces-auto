from odoo import models, fields, api

class CarfFinition(models.Model):
    _name = 'car.finition'
    _description = 'finition auto'

    name = fields.Char()
    model_ids = fields.Many2many('car.model')