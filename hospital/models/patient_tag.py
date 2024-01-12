from odoo import api, fields, models


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    
    name = fields.Text(string='Name', required=True, tracking=True)
    active  = fields.Boolean(string="Active", default=True, copy=False)
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color_2")
    sequence = fields.Integer(string="Sequence")
    
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = f"{self.name} (copy)"
        default['sequence'] = 10
        return super(PatientTag, self).copy(default)

    _sql_constraints = [
        ('unique_tag_name','unique (name, active)','Name must be unique'),
        ('check_sequence','check (sequence > 0)','Sequence must be non zero positive number.'),
    ]
