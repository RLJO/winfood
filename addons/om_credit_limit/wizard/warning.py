from odoo import models, fields, _


class RaiseWarning(models.TransientModel):
    _name = "warning.warning"
    _description = "Warning"

    def action_confirm(self):
        order = self.env['sale.order'].browse(self._context.get('active_id'))
        if order.exists():
            return order.with_context(skip_credit_check=True).action_confirm()

    def action_approve_credit_limit(self):
        order = self.env['sale.order'].browse(self._context.get('active_id'))
        if order.exists():
            order.credit_approve = True

#
# class RaiseWarning(models.TransientModel):
#     _name = "warning.warning"
#     _description = "Warning"
#
#     def action_confirm(self):
#         invoice = self.env['account.move'].browse(self._context.get('active_id'))
#         if invoice.exists():
#             return invoice.with_context(skip_credit_check=True).action_post()
