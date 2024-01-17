import datetime
from dateutil import relativedelta
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'
    
    @api.model
    def default_get(self, fields_list):
        res = super(CancelAppointmentWizard, self).default_get(fields_list)
        res['cancel_date'] = datetime.date.today()
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment", domain=[('state', '=', 'draft')])
    reason = fields.Text(string="Reason")
    cancel_date = fields.Text(string="Cancellation Date")
    
    def cancel_action(self):
        cancel_day = self.env['ir.config_parameter'].get_param('hospital.cancel_day')
        allowed_date = self.appointment_id.booking_date.date - relativedelta.relativedelta(days=int(cancel_day))
        if allowed_date < datetime.date.today():
            raise ValidationError("Sorry cancellation is not allowed for this booking.")
        self.appointment_id.state = "cancel"