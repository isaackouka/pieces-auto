from odoo import models, fields, api

class model(models.Model):
    _name          = 'model.auto'
    _description   = 'model auto'

    mark_id        = fields.Many2one('mark.car.auto')
    name           = fields.Char()
    engine_ids     = fields.Many2many("engine.auto")
    finition_ids   = fields.Many2many("finition.auto")
    year1          = fields.Integer()
    year2          = fields.Integer()