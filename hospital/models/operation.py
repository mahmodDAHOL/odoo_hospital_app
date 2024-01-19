from odoo import api, fields, models

class HospitalOperation(models.Model):
    _name = "hospital.operation"
    _description = "Hospital Operation"
    _log_acccess = False # don't add WHO fields to the table
    
    doctor_id = fields.Many2one('res.users', string='Doctor')
    operation_name = fields.Char(string='Name')
    reference_record = fields.Reference(selection=[('hospital.patient','Patient'),
                                                   ('hospital.appointment','Appointment')], string="Record")

    @api.model
    def name_create(self, name):
        """allow user to create doctor from its many to one field in oppointment form"""
        return self.create({'operation_name': name}).name_get()[0]