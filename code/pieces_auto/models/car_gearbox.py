from odoo import models, fields, api

class gearbox(models.Model):
    _name = 'gearbox.auto'
    _description = 'gearbox auto'

    name = fields.Char(
        compute='_compute_name'
    )
    type = fields.Selection(selection=[('bvm', 'BVM'),('bva', 'BVA')])
    number_gears = fields.Integer()

    @api.depends('type','number_gears')
    def _compute_name(self):
        for record in self :
            if record.number_gears and record.type :
                record.name =record.type+' '+str(record.number_gears)+' Vitesses'
            else:
                record.name=''

