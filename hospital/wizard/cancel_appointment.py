import datetime
from odoo import fields, models, api


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
        self.appointment_id.state = "cancel"