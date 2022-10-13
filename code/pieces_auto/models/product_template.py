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
    reference_oe = fields.Many2many(
        comodel_name='reference.oe'
    )

    short_reference = fields.Char(
        compute='_compute_short_reference'
    )

    comp_ids = fields.Many2many(
        comodel_name='product.comp'
    )

    designation = fields.Char()

    @api.depends('reference_oe')
    def _compute_short_reference(self):
        for record in self:
            if record.reference_oe:
                first_ref = record.reference_oe[0].name
                try:
                    index = first_ref.index('-')
                    record.short_reference = first_ref[index+1]+first_ref[index+2]
                except:
                    record.short_reference=''
            else:
                record.short_reference = ''


class ReferenceOE(models.Model):
    _name = 'reference.oe'

    name = fields.Char(
        string='Reference OE'
    )
