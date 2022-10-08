from odoo import models, fields, api

class ProductTemplate(models.Model):

    _inherit = "product.template"

    mark_id = fields.Many2one(
        comodel_name='mark.auto',
        )
    old_reference = fields.Char()

    comp_ids = fields.Many2many(
        comodel_name='product.comp'
    )


