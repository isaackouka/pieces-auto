from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError


class CarModel(models.Model):
    _name = 'car.model'
    _description = 'Car Model'

    mark_id = fields.Many2one(
        comodel_name='car.mark',
        required=True,
    )
    name = fields.Char(
        required=True,
    )
    engine_ids = fields.Many2many(
        comodel_name='car.engine',
        required=True,
    )
    gearbox_ids = fields.Many2many(
        comodel_name='car.gearbox',
        required=True,
    )
    finition_ids = fields.Many2many(
        comodel_name='car.finition',
    )
    generation_ids = fields.Many2many(
        comodel_name='model.generation'
    )

    tractions_ids = fields.Many2many(
        comodel_name='model.traction'
    )

    
class ModelGeneration(models.Model):
    _name = 'model.generation'
    _description = 'Model generation'

    name = fields.Char(
        compute='_compute_name',
    )

    generation = fields.Integer(
        required=True, 
    )

    year_start = fields.Selection([(str(y), str(y))
                                  for y in range(1970, (datetime.now().year)+1)],
                                  required=True,
                                  )
    year_end = fields.Selection([(str(y), str(y))
                                for y in range(1970, (datetime.now().year)+1)])

    @api.depends('generation')
    def _compute_name(self):
        for record in self:
            if record.generation:
                record.name = str(record.generation)
            else:
                record.name = ''


class ModelTracion(models.Model):
    _name = 'model.traction'
    _description = 'Model Traction'

    name = fields.Char()
