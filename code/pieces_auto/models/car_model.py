from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import ValidationError

SELECTION = []

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
    
    # year_end = fields.Selection(
    #     selection='years_selection'
    # )

    # @api.onchange('year_start')
    # def years_selection(self):
    #     for record in self:
    #         year_list = []
    #         for y in range(int(record._fields['year_start'].selection), datetime.now().year + 10):
    #             year_list.append((str(y), str(y)))
    #         return year_list


    @api.constrains('year_end')
    def check_year(self):
        for record in self:
            if int(record.year_end) < int(record.year_start):
                raise ValidationError(_("Invalid Year End"))

    # @api.onchange('year_start')
    # def _onchange_year_start(self):
    #     for record in self:
            
    #         global SELECTION
    #         SELECTION = []
    #         if record.year_start:
    #             for year in range(int(record.year_start), datetime.now().year + 1):
    #                 SELECTION.append((str(year), str(year)))
    #         record._fields['year_end'].selection = dict(SELECTION)
    #         attrs = {'selection': {'year_end': SELECTION}}
    #         return {'1': '2'}
        
