from datetime import date

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from dateutil import relativedelta

class HospitalPatient(models.Model):
    _inherit = 'mail.thread'
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    
    name = fields.Text(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Data of birth')
    ref = fields.Char(string="Reference")
    age = fields.Integer(string='Age', compute= '_compute_age', inverse='_inverse_compute_age',
                         search='_search_age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender', tracking=True)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    active  = fields.Boolean(string="Active", default=True)
    image  = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tags")
    appointment_count = fields.Integer(string='Appointment Count', compute= '_compute_appointment_count', store=True)
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointment')
    parent = fields.Char(string='Parent')
    marital_status = fields.Selection([
        ('married','Married'),
        ('single','Single'),
    ], string="Marital", tracking=True)
    partner_name = fields.Char(string="Partner name")
    is_birthday = fields.Boolean(string="Birthday ?", compute="_compute_is_birthday")

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    api.ondelete(at_uninstall=False)
    def check_appointments(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError("You cannot delete a patient with appointments.")

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

    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)
            
    def _search_age(self, operator, value):
        """Allow to search by age"""
        date_of_birth = date.today() - relativedelta.relativedelta(years=value)
        start_of_year = date_of_birth.replace(day=1, month=1)
        end_of_year = date_of_birth.replace(day=31, month=12)
        return [('date_of_birth', '>=', start_of_year), ('date_of_birth', '<=', end_of_year)]

    @api.depends('date_of_birth')
    def _compute_is_birthday(self):
        for rec in self:
            is_birthday = False
            if rec.date_of_birth:
                today = date.today()
                if today.day == rec.date_of_birth.day and today.month == rec.date_of_birth.month:
                    is_birthday = True
            rec.is_birthday = is_birthday