from odoo import api, models, fields, _

class MRPBOMInherit(models.Model):
	_inherit = 'mrp.bom'

	product_qty = fields.Float(
        'Quantity', default=1.0,
        digits='Product Unit of Measure', required=True)