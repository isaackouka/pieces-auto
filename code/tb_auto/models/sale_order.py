from dataclasses import field
from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare, float_round

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    artec_number_of_package = fields.Integer(
        string='Number packages'
    )

    artec_sale_in_pack = fields.Boolean(
        related='product_id.artec_sale_in_pack'
    )

    @api.onchange('product_id')
    def _artec_check_sale_in_package(self):
        for record in self:
            print('')
            if record.product_id.product_tmpl_id.artec_sale_in_pack == True:
                record.product_uom_qty = 0
                return {
                    'warning': {
                        'title': _('Warning'),
                        'message': _(
                            "This product must be sale in packages",
                        ),
                    },
                }
                

    @api.onchange('artec_number_of_package')
    def _onchange_artec_number_of_package(self):
        for record in self:
            qty_pack = record.product_packaging.qty
            record.product_uom_qty = record.artec_number_of_package * qty_pack

    @api.onchange('product_packaging')
    def _artec_onchange_product_packaging(self):
        for record in self:
            record.artec_number_of_package = 0


    def _check_package(self):
        default_uom = self.product_id.uom_id
        pack = self.product_packaging
        qty = self.product_uom_qty
        q = default_uom._compute_quantity(pack.qty, self.product_uom)


        if (
            qty
            and q
            and float_compare(
                qty / q, float_round(qty / q, precision_rounding=1.0), precision_rounding=0.001
            )
            != 0
        ):
            newqty = qty - (qty % q) + q
            return {
                'warning': {
                    'title': _('Warning'),
                    'message': _(
                        "This product is packaged by %(pack_size).2f %(pack_name)s. You should sell %(quantity).2f %(unit)s.",
                        pack_size=pack.qty,
                        pack_name=default_uom.name,
                        quantity=newqty,
                        unit=self.product_uom.name
                    ),
                },
            }
        return {}