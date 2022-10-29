from email.policy import default
from numpy import product
from odoo import models, fields, api, _
from odoo.osv import expression


class ProductTemplate(models.Model):

    _inherit = "product.packaging"
    _order = 'id'

    def _default_product(self):
        return self.env.context.get('active_id')

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        check_company=True,
        default=_default_product
    )

    contain_packages = fields.Boolean(
        default=False
    )

    package = fields.Many2one(
        comodel_name='product.packaging',
        domain="[('product_id','=', product_id)]"
    )

    number_package = fields.Integer()

    @api.onchange('number_package')
    def set_qty(self):
        for record in self:
            record.qty = record.package.qty * record.number_package
