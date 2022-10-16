from odoo import models, fields, api, _


class productFront(models.Model):
    _name = 'product.front'

    name = fields.Char()

class productsSide(models.Model):
    _name = 'product.side'

    name = fields.Char()

class productPosition(models.Model):
    _name = 'product.position'

    name = fields.Char()