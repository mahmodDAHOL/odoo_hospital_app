from datetime import date

from odoo import api, fields, models


class HospitalPatient(models.Model):
    _inherit = 'mail.thread'
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    
    name = fields.Text(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Data of birth')
    ref = fields.Char(string="Reference")
    age = fields.Integer(string='Age', compute= '_compute_age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender', tracking=True)
    active  = fields.Boolean(string="Active", default=True)
    image  = fields.Image(string="Image")
    parent = fields.Char(string='Parent')
    marital_status = fields.Selection([
        ('married','Married'),
        ('single','Single'),
    ], string="Marital", tracking=True)
    partner_name = fields.Char(string="Parent name")

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        for patient in self:
            if patient.date_of_birth:
                today = date.today()
                patient.age = today.year -patient.date_of_birth.year
            else:
                patient.age = 0