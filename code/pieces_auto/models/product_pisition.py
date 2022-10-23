from odoo import models, fields, api, _


class productFront(models.Model):
    _name = 'product.front'

    name = fields.Char(
        required=True
    )

class productsSide(models.Model):
    _name = 'product.side'

    name = fields.Char(
        required=True
    )

class productPosition(models.Model):
    _name = 'product.position'

    name = fields.Char(
        required=True
    )