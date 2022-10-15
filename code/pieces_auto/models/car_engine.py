from odoo import models, fields, api


class engine(models.Model):
    _name = 'engine.auto'
    _description = 'engine auto'

    name = fields.Char(
        compute='_compute_name'
    )
    cylindre = fields.Char()
    type = fields.Char()
    energie = fields.Selection(
        selection=[('ess', 'Essence'),
                   ('dsl', 'Diesel'),
                   ('gpl', 'GPL')]
    )
    vales = fields.Integer()
    powerful = fields.Integer()

    model_ids = fields.Many2many('model.auto')

    @api.depends('cylindre', 'type', 'powerful')
    def _compute_name(self):
        for record in self:
            if record.cylindre and record.type and record.powerful:
                record.name = record.cylindre+' ' + \
                    record.type+' '+str(record.powerful)+'ch'
            else:
                record.name = ''
