from odoo import models, fields, api
from odoo.osv import expression


class ProductTemplate(models.Model):

    _inherit = "product.template"

    mark_id = fields.Many2one(
        comodel_name='mark.auto',
        )
    original_reference = fields.Char()

    comp_ids = fields.Many2many(
        comodel_name='product.comp'
    )


