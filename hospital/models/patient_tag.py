from odoo import fields, models


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    
    name = fields.Text(string='Name', required=True, tracking=True)
    active  = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color_2")
    sequence = fields.Integer(string="Sequence")

    _sql_constraints = [
        ('unique_tag_name','unique (name, active)','Name must be unique'),
        ('check_sequence','check (sequence > 0)','Sequence must be non zero positive number.'),
    ]
