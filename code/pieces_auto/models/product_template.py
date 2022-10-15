from odoo import models, fields, api, _
from odoo.osv import expression


class ProductTemplate(models.Model):

    _inherit = "product.template"

    name = fields.Char(
        string='Product name',
        required=True,
        translate=True,
    )

    has_multi_name = fields.Boolean(
        default=False,
        string='Multi name'
    )

    name_ids = fields.Many2many(
        comodel_name='name.product',
        string='Other names'
    )

    designation = fields.Char()

    reference_oe = fields.Many2many(
        comodel_name='reference.oe'
    )

    short_reference = fields.Char(
        compute='_compute_short_reference'
    )

    mark_id = fields.Many2one(
        comodel_name='mark.auto',
    )

    constructor_ids = fields.Many2many(
        comodel_name='mark.car.auto',
    )

    front = fields.Char()
    side = fields.Char()
    pisition = fields.Char()
    specification = fields.Char()
    
    comp_ids = fields.Many2many(
        comodel_name='product.comp'
    )

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
    
    @api.model
    def create(self, vals):
        vals['default_code'] = self.env['ir.sequence'].next_by_code('tba.reference') or _("New")
        return super(ProductTemplate,self).create(vals)


class ReferenceOE(models.Model):
    _name = 'reference.oe'

    name = fields.Char(
        string='Reference OE'
    )

class NameProduct(models.Model):
    _name = 'name.product'

    name = fields.Char()
