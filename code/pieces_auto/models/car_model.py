from odoo import models, fields, api
from datetime import datetime

class model(models.Model):
    _name          = 'model.auto'
    _description   = 'model auto'

    mark_id = fields.Many2one('mark.car.auto')
    name = fields.Char()
    engine_ids = fields.Many2many("engine.auto")
    gearbox_ids = fields.Many2many("gearbox.auto")
    finition_ids = fields.Many2many("finition.auto")
    year_start = fields.Selection([(str(y), str(y)) for y in range(1970, (datetime.now().year)+1)])
    year_end = fields.Selection([(str(y), str(y)) for y in range(1970, (datetime.now().year)+1)])