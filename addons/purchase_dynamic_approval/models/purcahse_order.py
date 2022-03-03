from odoo import _, models, fields, api

class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    approver_ids = fields.Many2many('res.users', 'po_approver_rel', string='Approvers')
    acknowledger_ids = fields.Many2many('res.users', 'po_acknowledger_rel', string='Acknowledgers')

    def set_approval_process(self):
        for line in self.order_line:
            if line.account_analytic_id:
                approval = self.env['purchase.order.approval'].search([('analytic_account_id', '=', line.account_analytic_id.id)])
                self.write({'approver_ids': approval.get_approvers()})
                self.write({'acknowledger_ids': approval.get_acknowledgers()})

    @api.model
    def create(self, values):
        result = super(PurchaseOrder, self).create(values)
        return result


class PurchaseApproverLine(models.Model):

    _name = 'purchase.approval.line'
    _description = 'Purchase Approval Line'

    name = fields.Char(string='Description')
    approver_id = fields.Many2one('res.users', string='Approver')
    minimum_amount = fields.Float(string='Minimum Amount')
    miximum_amount = fields.Float(string='Miximum Amount')
    approval_id = fields.Many2one('purchase.order.approval', string="Approve ID")


class PurchaseAcknowledgeLine(models.Model):

    _name = 'purchase.acknowledge.line'
    _description = 'Purchase Acknowledge Line'

    name = fields.Char(string='Level')
    acknowledger_id = fields.Many2one('res.users', string='Acknowledger')
    approval_id = fields.Many2one('purchase.order.approval', string="Approve ID")

class PurchaseOrderApproval(models.Model):

    _name = 'purchase.order.approval'
    _description = 'Purchase Order Approval'

    _rec_name = 'name'
    _order = 'id ASC'

    name = fields.Char(string='Name',required=True,default=lambda self: _('New'),copy=False)
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account')
    company_id = fields.Many2one('res.company', string='Company')
    department_id = fields.Many2one('hr.department', string='Department')
    approval_line_ids = fields.One2many('purchase.approval.line', 'approval_id', string='Approve Users')
    acknowledge_line_ids = fields.One2many('purchase.acknowledge.line', 'approval_id', string='Acknowledge Users')

    @api.onchange('department_id')
    def onchange_department_id(self):
        if self.department_id:
            self.analytic_account_id = self.department_id.analytic_account_id.id
            self.company_id = self.env.user.company_id.id

    def get_approvers(self):
        context = self._context
        approver_ids = []
        for line in self.approval_line_ids:
            approver_ids.append(line.approver_id.id)
        return approver_ids

    def get_acknowledgers(self):
        context = self._context
        acknowledger_ids = []
        for line in self.acknowledge_line_ids:
            acknowledger_ids.append(line.acknowledger_id.id)
        return acknowledger_ids

