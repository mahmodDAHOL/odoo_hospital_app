from odoo import models

class ResGroups(models.Model):
    _inherit = 'res.groups'

    def get_application_groups(self, domain):
        sale_receipts = self.env.ref('account.group_sale_receipts').id
        return super(ResGroups, self).get_application_groups(domain + [('id','!=', sale_receipts)])