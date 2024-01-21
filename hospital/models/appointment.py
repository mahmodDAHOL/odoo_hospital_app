from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'hospital.appointment'
    _description = 'Hospital appointment'
    _rec_name = 'ref'
    _order = 'id desc'
    
    patient_id = fields.Many2one('hospital.patient', string='Patient', ondelete='cascade')
    ref = fields.Char(string="Reference", readonly=True)
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
        ('cancel','Cancelled')], string="Status",
        default='draft', tracking=True
    )
    doctor_id = fields.Many2one('res.users', string="Doctor")
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.line', 'appointment_id', string='Pharmacy')
    hide_sales_price = fields.Boolean(string="Hide sales price")
    operation = fields.Many2one('hospital.operation', string="Operation")
    progress = fields.Integer(string="Progress", compute="_compute_progress")
    duration = fields.Float(string="Duration")

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    amount_total = fields.Float(string="Total", compute="_compute_amount_total",
                                    currency_field='company_currency_id')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).create(vals)

    def unlink(self):
        if self.state != 'draft':
            raise ValidationError("You can delete appointment only in draft state.")
        return super(HospitalAppointment, self).unlink()
        
    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).write(vals)
        
    def action_in_consultation(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = "in_consultation"
    
    def action_done(self):
        for rec in self:
            rec.state = "done"
        return {
            'effect': {
                'fadeout','slow',
                'message','Done',
                'type','rainbow_man'
            }
        }
    
    def action_cancel(self):
        action = self.env.ref('hospital.cancel_appointment_action').read()[0]
        return action

    def action_draft(self):
        for rec in self:
            rec.state = "draft"
            
    @api.depends('state')
    def _compute_progress(self):
        for rec in self:
            if rec.state == 'draft':
                progress = 25
            elif rec.state == 'in_consultation':
                progress = 50
            elif rec.state == 'done':
                progress = 100
            else:
                progress = 0
            rec.progress = progress
 
    @api.depends('pharmacy_line_ids.price_subtotal')
    def _compute_amount_total(self):
        for appointment in self:
            total = 0
            for rec in appointment.pharmacy_line_ids:
                total += rec.price_subtotal
            appointment.amount_total = total

class AppointmentPharmacyLine(models.Model):
    _name = 'appointment.pharmacy.line'
    _description = "Appointment Pharmacy Line"

    product_id = fields.Many2one('product.product', required=True)
    price = fields.Float(string="Price", related='product_id.list_price')
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")

    company_currency_id = fields.Many2one('res.currency', related='appointment_id.currency_id')
    price_subtotal = fields.Monetary(string="Subtotal", compute="_compute_price_subtotal",
                                     currency_field='company_currency_id')

    @api.depends('price', 'qty')
    def _compute_price_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.price * rec.qty