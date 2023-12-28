from odoo import fields, models

class HospitalAppointment(models.Model):
    _inherit = 'mail.thread'
    _name = 'hospital.appointment'
    _description = 'Hospital appointment'
    
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment time', default=fields.Datetime.now())
    booking_date = fields.Datetime(string='Booking date', default=fields.Date.context_today) 