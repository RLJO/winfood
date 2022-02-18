from odoo import api, models, fields, _

class StockPickingInherit(models.Model):
	_inherit = 'stock.picking'
	
	def get_inventory_user(self):
		result = False
		user_id = self.env.uid
		user = self.env['res.users'].browse(user_id)
		# print(user,'current user show-----------------')
		is_inventory_user_id = False
		group_inventory_user_id = \
			self.env['ir.model.data'].get_object_reference('stock', 'group_stock_user')[1]

		group_manager_id = \
			self.env['ir.model.data'].get_object_reference('stock', 'group_stock_manager')[1]

		if group_inventory_user_id and not group_manager_id in [g.id for g in user.groups_id]:
			print ('group_inventory_user_id',group_inventory_user_id)
			is_inventory_user_id = True

		if is_inventory_user_id:
			result=True
		self.get_user = result

	get_user =fields.Boolean(compute='get_inventory_user',string='Get User')
