from odoo import models

class PortalMixing(models.AbstractModel):
    _inherit = 'portal.mixin'

    def set_action_from_portal(self, suffix=None, report_type=None, download=None, query_string=None, anchor=None):
        self.ensure_one()
        order_id = int(self.access_url.replace("/my/orders/", ""))
        order = self.env['sale.order'].search([('id', '=', order_id)])
        order.action_customerIfo()

    def account_action_from_portal(self, suffix=None, report_type=None, download=None, query_string=None, anchor=None):
        self.ensure_one()
        invoice_id = int(self.access_url.replace("/my/invoices/", ""))
        order = self.env['account.move'].search([('id', '=', invoice_id)])
        order.action_customerIfo()