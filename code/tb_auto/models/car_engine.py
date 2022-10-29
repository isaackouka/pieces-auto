from odoo import models, fields, api

class CarEngine(models.Model):
    _name = 'car.engine'
    _description = 'Car Engine'

    name = fields.Char(
        compute='_compute_name',
    )
    cylindre = fields.Char(
        required=True,
    )
    type = fields.Many2one(
        comodel_name='engine.type',
        required=True,
    )
    energie = fields.Selection(
        selection=[('ess', 'Essence'),
                   ('dsl', 'Diesel'),
                   ('gpl', 'GPL')],
        required=True,
    )
    valves = fields.Integer(
        required=True,
    )
    powerful = fields.Integer(
        required=True,
    )

    model_ids = fields.Many2many(
        comodel_name='car.model'
    )

    @api.depends('cylindre', 'type', 'powerful')
    def _compute_name(self):
        for record in self:
            if record.cylindre and record.type and record.powerful:
                record.name = record.cylindre+' ' + \
                    record.type.name+' '+str(record.powerful)+'ch'
            else:
                record.name = ''


class EngineType(models.Model):
    _name = 'engine.type'
    
    name = fields.Char()
