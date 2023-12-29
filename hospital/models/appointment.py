from odoo import fields, models

class HospitalAppointment(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'hospital.appointment'
    _description = 'Hospital appointment'
    _rec_name = 'patient_id'
    
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment time', default=fields.Datetime.now())
    booking_date = fields.Datetime(string='Booking date', default=fields.Date.context_today) 
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very High')], string="Priority"
    )
    state = fields.Selection([
        ('draft','Draft'),
        ('in_consultation','In Consultation'),
        ('done','Done'),
        ('cancel','Cancelled')], string="Status"
    )
    doctor_id = fields.Many2one('res.users', string="Doctor")