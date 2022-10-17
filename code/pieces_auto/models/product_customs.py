from odoo import models, fields, api, _


class productCustoms(models.Model):
    _name = 'product.customs'
    _description = 'Product Customs'

    hs_code = fields.Char(
        required=True, 
    )
    hs_designation = fields.Char()

    manifacturing_country = fields.Many2one(
        comodel_name='res.country'
    )

    origin_country = fields.Many2one(
        comodel_name='res.country'
    )

    price_preferential = fields.Float()

    custom_taxe = fields.Float()

    tva = fields.Float()

    product_id = fields.Many2one(
        comodel_name='product.template'
    )