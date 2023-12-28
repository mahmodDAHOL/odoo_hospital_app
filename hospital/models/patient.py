from odoo import fields, models

class HospitalPatient(models.Model):
    _inherit = 'mail.thread'
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    
    name = fields.Text(string='Name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender', tracking=True)
    active  = fields.Boolean(string="Active", default=True)