from odoo import fields, models


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    
    name = fields.Text(string='Name', required=True, tracking=True)
    active  = fields.Boolean(string="Active", default=True)
