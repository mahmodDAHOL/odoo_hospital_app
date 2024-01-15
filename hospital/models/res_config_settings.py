from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cancel_days = fields.Integer(string='days', config_parameter='hospital.cancel_days')