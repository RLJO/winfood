from odoo import fields,models,api,_
# from odoo.tools.func import default

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    check_options = fields.Selection([
        ('oversea', 'Oversea PO'),
        ('local', 'Local PO')], string="PO Type",default="local" )

    approve_state = fields.Selection([('draft','Draft'),('approve', 'Approve')], string="State", default='draft',tracking=True )

    def action_approve(self):
        for rec in self:
            rec.approve_state = 'approve'