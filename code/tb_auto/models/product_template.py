from email.policy import default
import string
from odoo import models, fields, api, _
from odoo.osv import expression


class ProductTemplate(models.Model):

    _inherit = "product.template"

    def _get_buy_route(self):
        buy_route = self.env.ref('tb_auto.route_warehouse0_buy', raise_if_not_found=False)
        if buy_route:
            return buy_route.ids
        return []

    def _default_artec_company_auto(self):
        company = self.env['res.company'].browse(
            self._context.get('allowed_company_ids'))
        if len(company) == 1 and company[0].name not in ['EURL BOUKHENOUFA IMPORT/EXPORT', 'SARL CONFI CHOC', 'SARL TB INGREDIENTS']:
            return True
        else:
            return False

    artec_company_auto = fields.Boolean(
        default=_default_artec_company_auto,
        store=False,
    )

    name = fields.Char(
        string='Product name',
        required=True,
        translate=True,
    )

    artec_has_multi_name = fields.Boolean(
        default=False,
        string='Multi name'
    )

    artec_name_ids = fields.Many2many(
        comodel_name='product.name',
        string='Other names'
    )

    artec_designation = fields.Char(
        compute='_compute_artec_designation',
        string='Designation'
    )

    artec_reference_oe = fields.Many2many(
        comodel_name='product.referenceoe',
        string='Reference OE'
    )

    artec_short_reference = fields.Char(
        compute='_compute_short_reference',
        string='Short Reference'
    )

    artec_reference_mark_ids = fields.One2many(
        'alternative.references',
        'product_id'
    )

    artec_category_ids = fields.Many2many(
        comodel_name='product.family',
        string='Category',
    )

    artec_product_family = fields.Many2one(
        comodel_name='product.category',
        string='Family'
    )

    artec_mark_id = fields.Many2one(
        comodel_name='product.mark',
        string='Mark'
    )

    artec_constructor_ids = fields.Many2many(
        comodel_name='car.mark',
        string='Constructors'
    )

    artec_front_ids = fields.Many2many(
        comodel_name='product.front',
        string='Front'
    )

    artec_side_ids = fields.Many2many(
        comodel_name='product.side',
        string='Side'
    )

    artec_position_ids = fields.Many2many(
        comodel_name='product.position',
        string='Position'
    )

    artec_specification = fields.Many2many(
        comodel_name='product.specifiation',
        string='Specification'
    )

    artec_observation = fields.Char(
        string='Observations'
    )

    artec_compatible_car_ids = fields.Many2many(
        comodel_name='compatible.car',
    )

    artec_hs_code = fields.Char(
        string='HS Code'
    )

    artec_hs_designation = fields.Char(
        string='HS Designation'
    )

    artec_tax_custom = fields.Many2one(
        string='Tax Custom',
        comodel_name='account.tax',
        domain=[('type_tax_use', '=', 'purchase')]
    )

    artec_locally_made = fields.Boolean(
        string='Locally made'
    )

    artec_customs_ids = fields.One2many(
        'product.customs',
        'product_id'
    )

    artec_sale_in_pack = fields.Boolean(
        default=False,
        string='Sale in pack'
    )


    @api.depends('artec_reference_oe')
    def _compute_short_reference(self):
        for record in self:
            if record.artec_reference_oe:
                for ref in record.artec_reference_oe:
                    if (len(ref.name) == 11 and ref.name[5] == '-'):
                        record.artec_short_reference = ref.name[6] + \
                            ref.name[7]
                        break
                    else:
                        record.artec_short_reference = ''
            else:
                record.artec_short_reference = ''

    @api.depends('name', 'artec_compatible_car_ids', 'artec_specification', 'artec_front_ids', 'artec_side_ids', 'artec_position_ids', 'artec_mark_id', 'artec_constructor_ids')
    def _compute_artec_designation(self):
        for record in self:
            list_cars = ''
            designation = ''
            if record.name:
                designation = record.name
            list_cars = '' + '/'.join(['{} {}'.format(
                c.model_id.name,
                '(' + '-'.join(c.generation_ids.mapped('name')) +
                ')' if c.generation_ids else ''
            ) for c in record.artec_compatible_car_ids])
            designation = designation + ' ' + list_cars
            front = '('+'-'.join(record.artec_front_ids.mapped('name')
                                 ) + ')' if record.artec_front_ids else ''
            designation = designation + ' ' + front
            side = '('+'-'.join(record.artec_side_ids.mapped('name')
                                ) + ')' if record.artec_side_ids else ''
            designation = designation + ' ' + side
            position = '('+'-'.join(record.artec_position_ids.mapped('name')
                                    ) + ')' if record.artec_position_ids else ''
            designation = designation + ' ' + position
            specification = '('+'-'.join(record.artec_specification.mapped('name')
                                         ) + ')' if record.artec_specification else ''
            designation = designation + ' ' + specification
            mark = record.artec_mark_id.name if record.artec_mark_id else ''
            designation = designation + ' ' + mark
            constructor = '-'.join(record.artec_constructor_ids.mapped('name')
                                   ) if record.artec_constructor_ids else ''
            designation = designation + ' ' + constructor
            record.artec_designation = designation

    @api.model
    def create(self, vals):
        vals['default_code'] = self.env['ir.sequence'].next_by_code(
            'tba.reference') or _("New")
        return super(ProductTemplate, self).create(vals)


class ProductMark(models.Model):
    _name = 'product.mark'
    _description = 'Product Mark'
    _order = 'name asc'

    name = fields.Char(
        required=True
    )
    image = fields.Image()


class ProductReferenceOE(models.Model):
    _name = 'product.referenceoe'

    name = fields.Char(
        string='Reference OE',
        required=True
    )


class AlternativeReferences(models.Model):
    _name = 'alternative.references'

    mark_id = fields.Many2one(
        comodel_name='product.mark',
        required=True,
    )

    reference = fields.Char(
        string='Reference',
        required=True,
    )

    product_id = fields.Many2one(
        comodel_name='product.template'
    )


class ProductName(models.Model):
    _name = 'product.name'

    name = fields.Char(
        required=True
    )


class ProductSpecification(models.Model):
    _name = 'product.specifiation'

    name = fields.Char(
        required=True
    )
