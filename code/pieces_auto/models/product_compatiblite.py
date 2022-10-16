from datetime import datetime
from odoo import models, fields, api, _


class productCompatibility(models.Model):
    _name = 'product.comp'
    _description = 'Product Comp'

    model_id = fields.Many2one(
        comodel_name='model.auto'
    )

    engine_ids = fields.Many2one(
        comodel_name='engine.auto'
    )

    energie = fields.Selection(
        selection=[('ess', 'Essence'),
                   ('dsl', 'Diesel'),
                   ('gpl', 'GPL')]
    )

    gearbox_ids = fields.Many2one(
        comodel_name='gearbox.auto'
    )

    year_start = fields.Selection([(str(y), str(y))
                                for y in range(1970, (datetime.now().year)+1)])
    year_end = fields.Selection([(str(y), str(y))
                                for y in range(1970, (datetime.now().year)+1)])

    finition_ids = fields.Many2many(
        comodel_name='finition.auto'
    )

    @api.onchange('model_id')
    def _onchange_model_id(self):
        attrs = {'domain': {
            'engine_ids': []
        },
        }
        if self.model_id:
            engine_ids = self.model_id.mapped('engine_ids.id')
            attrs['domain']['engine_ids'].append(
                ('id', 'in', engine_ids))

        return attrs
