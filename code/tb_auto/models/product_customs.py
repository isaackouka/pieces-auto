from odoo import models, fields, api, _


class productCustoms(models.Model):
    _name = 'product.customs'
    _description = 'Product Customs'


    manifacturing_country = fields.Many2one(
        comodel_name='res.country'
    )

    origin_country = fields.Many2one(
        comodel_name='res.country'
    )

    price_preferential = fields.Float()

    tax = fields.Many2many(
        comodel_name='account.tax',
        domain=[('type_tax_use', '=', 'purchase')]
    )

    tva = fields.Many2one(
        comodel_name='account.tax',
        domain=[('type_tax_use', '=', 'purchase')]
    )

    product_id = fields.Many2one(
        comodel_name='product.template'
    )