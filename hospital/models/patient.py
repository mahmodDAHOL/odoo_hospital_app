from odoo import fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    
    name = fields.Text(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')