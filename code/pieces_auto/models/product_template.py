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

    designation = fields.Char(
    #    compute='_compute_designation',
    )

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

    front_ids = fields.Many2many(
        comodel_name='product.front',
    )
    side_ids = fields.Many2many(
        comodel_name='product.side',
    )
    position_ids = fields.Many2many(
        comodel_name='product.position',
    )
    
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

    # @api.depends('name','comp_ids','specification','front_ids','side_ids','position_ids')
    # def _compute_designation(self):
    #     for record in self:
    #             for car in record.comp_ids:
    #                 cars = car.model_id.name+' '+car.year_start+'-'+car.year_end
    #             record.designation=record.name +' '+ cars +' '+ record.specification

    
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
