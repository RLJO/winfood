from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    amount_credit_limit = fields.Monetary('Credit Limit')

class SaleOrder(models.Model):
    _inherit = "sale.order"

    credit_approve = fields.Boolean('Approved', default=False)
    def action_confirm(self):

        if self.partner_id and \
                self.partner_id.amount_credit_limit != 0 and not self._context.get('skip_credit_check'):
            sum = 0
            value = self.env['sale.order'].search([('partner_id', '=', self.partner_id.id)])
            for rec in value:
                sum += rec.amount_total

            amount_due =self.amount_total
            if (amount_due > self.partner_id.amount_credit_limit or sum >  self.partner_id.amount_credit_limit) and not self.credit_approve:
                return {
                    'name': _('Warning'),
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    'res_model': 'warning.warning',
                    'target': 'new',
                    'context': {},
                }
        return super(SaleOrder, self).action_confirm()
