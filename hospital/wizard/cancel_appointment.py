import datetime
from odoo import fields, models, api


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'
    
    @api.model
    def default_get(self, fields_list):
        res = super(CancelAppointmentWizard, self).default_get(fields_list)
        res['cancel_date'] = datetime.date.today()
        return res

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    reason = fields.Text(string="Reason")
    cancel_date = fields.Text(string="Cancellation Date")
    
    def cancel_action(self):
        self.appointment_id.state = "cancel"