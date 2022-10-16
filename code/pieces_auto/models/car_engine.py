from odoo import models, fields, api


class engine(models.Model):
    _name = 'engine.auto'
    _description = 'engine auto'

    name = fields.Char(
        compute='_compute_name',
    )
    cylindre = fields.Char(
        required=True,
    )
    type = fields.Char(
        required=True,
    )
    energie = fields.Selection(
        selection=[('ess', 'Essence'),
                   ('dsl', 'Diesel'),
                   ('gpl', 'GPL')],
        required=True,
    )
    vales = fields.Integer(
        required=True,
    )
    powerful = fields.Integer(
        required=True,
    )

    model_ids = fields.Many2many(
        comodel_name='model.auto'
    )

    @api.depends('cylindre', 'type', 'powerful')
    def _compute_name(self):
        for record in self:
            if record.cylindre and record.type and record.powerful:
                record.name = record.cylindre+' ' + \
                    record.type+' '+str(record.powerful)+'ch'
            else:
                record.name = ''
