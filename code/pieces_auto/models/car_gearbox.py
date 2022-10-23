from odoo import models, fields, api

class CarGearbox(models.Model):
    _name = 'car.gearbox'
    _description = 'Car Gearbox'

    name = fields.Char(
        compute='_compute_name'
    )
    type = fields.Selection(selection=[('BVM', 'BVM'),('BVA', 'BVA')])
    number_gears = fields.Integer()

    @api.depends('type','number_gears')
    def _compute_name(self):
        for record in self :
            if record.number_gears and record.type :
                record.name =record.type+' '+str(record.number_gears)+' Vitesses'
            else:
                record.name=''

