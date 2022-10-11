from odoo import models, fields, api
from odoo.osv import expression


class ProductTemplate(models.Model):

    _inherit = "product.template"

    name = fields.Char(
        string='Product name',
        required=True, 
        translate=True,
    )

    mark_id = fields.Many2one(
        comodel_name='mark.auto',
        )
    reference_oe = fields.Char()

    short_reference = fields.Char()

    comp_ids = fields.Many2many(
        comodel_name='product.comp'        
    )


    designation = fields.Char()





