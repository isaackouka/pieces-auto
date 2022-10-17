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
       compute='_compute_designation',
    )

    reference_oe = fields.Many2many(
        comodel_name='reference.oe'
    )

    short_reference = fields.Char(
        compute='_compute_short_reference'
    )

    category_ids = fields.Many2many(
        comodel_name='product.category'
    )

    product_family = fields.Many2one(
        comodel_name='product.family'
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
        comodel_name='product.comp',
    )

    customs_ids = fields.One2many(
        'product.customs',
        'product_id'
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

    @api.depends('name','comp_ids','specification','front_ids','side_ids','position_ids')
    def _compute_designation(self):
        for record in self:
            list_cars = ''
            designation = record.name
            if record.comp_ids:
                for car in record.comp_ids:
                    if car.model_id:
                        list_cars = car.model_id.name
                    if car.year_start:
                        list_cars = list_cars +' '+car.year_start
                    if car.year_end:
                        if car.year_start != car.year_end:
                            list_cars = list_cars +'-'+car.year_end
                    if car != record.comp_ids[-1]:
                        list_cars = list_cars +' _'

                    designation = designation +' '+ list_cars
            if record.specification:
                designation = designation +' '+record.specification
            if record.front_ids:
                designation = designation +' '+record.front_ids.name
            if record.side_ids:
                designation = designation +' '+record.side_ids.name
            if record.position_ids:
                designation = designation +' '+record.position_ids.name
            
            record.designation = designation
                            
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
