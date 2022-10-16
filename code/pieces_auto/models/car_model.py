from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError


class model(models.Model):
    _name = 'model.auto'
    _description = 'model auto'

    mark_id = fields.Many2one(
        comodel_name='mark.car.auto',
    )
    name = fields.Char(
        required=True,
    )
    engine_ids = fields.Many2many(
        comodel_name='engine.auto',
        required=True,
    )
    gearbox_ids = fields.Many2many(
        comodel_name='gearbox.auto',
        required=True,
    )
    finition_ids = fields.Many2many(
        comodel_name='finition.auto',
    )
    year_start = fields.Selection([(str(y), str(y))
                                  for y in range(1970, (datetime.now().year)+1)],
                                  required=True,
                                  )
    year_end = fields.Selection([(str(y), str(y))
                                for y in range(1970, (datetime.now().year)+1)])

    @api.constrains('year_end')
    def check_year(self):
        for record in self:
            if int(record.year_end) < int(record.year_start):
                raise ValidationError(_("Invalid Year End"))
