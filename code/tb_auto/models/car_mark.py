from odoo import models, fields, api

class CarMark(models.Model):
    _name = 'car.mark'
    _description = 'Car Mark'

    name = fields.Char(
        required=True, 
    )
