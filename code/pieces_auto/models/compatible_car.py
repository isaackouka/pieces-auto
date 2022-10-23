from datetime import datetime
from odoo import models, fields, api, _


class CompatibleCar(models.Model):
    _name = 'compatible.car'
    _description = 'Compatible Car'

    model_id = fields.Many2one(
        comodel_name='car.model',
        required=True, 
    )

    generation_ids = fields.Many2many(
        comodel_name='model.generation',
    )

    engine_ids = fields.Many2one(
        comodel_name='car.engine'
    )

    energie = fields.Selection(
        selection=[('ess', 'Essence'),
                   ('dsl', 'Diesel'),
                   ('gpl', 'GPL')]
    )

    gearbox_ids = fields.Many2one(
        comodel_name='car.gearbox'
    )

    finition_ids = fields.Many2many(
        comodel_name='car.finition'
    )

    @api.onchange('model_id')
    def _onchange_model_id(self):
        attrs = {'domain': {
            'engine_ids': [],
            'gearbox_ids': [],
            'generation_ids': [],
        }}
        if self.model_id:
            engine_ids = self.model_id.mapped('engine_ids.id')

            attrs['domain']['engine_ids'].append(
                ('id', 'in', engine_ids))

            gearbox_ids = self.model_id.mapped('gearbox_ids.id')
            attrs['domain']['gearbox_ids'].append(
                ('id', 'in', gearbox_ids))
            
            generation_ids = self.model_id.mapped('generation_ids.id')
            attrs['domain']['generation_ids'].append(
                ('id', 'in', generation_ids))

            self.engine_ids = [(5, False, False)]
            self.gearbox_ids = [(5, False, False)]
            self.generation_ids = [(5, False, False)]

        return attrs
