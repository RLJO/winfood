from odoo import fields, api, models, _
from random import randint
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one('winfood.city', string="City")
    township_name = fields.Many2one('winfood.township', string="TownShip", domain="[('city_id', '=', city_id)]")
    phone = fields.Char(required=True)
    gene_password = fields.Char(string="Password", readonly=True)

    @api.model
    def create(self, vals):
        name = vals.get('name')
        phone = vals.get('phone')
        # menu_id = self._context.get('params').get('menu_id') if self._context.get('params') else None
        result = super(ResPartner, self).create(vals)
        if self._context.get('default_customer_rank') and phone:
            gene_password = randint(10 ** (6 - 1), (10 ** 6) - 1)
            result.write({'gene_password': gene_password})
            self.env['res.users'].create({
                'name': name,
                'login': phone,
                'password': str(gene_password),
                'partner_id': result.id,
                'groups_id': [(6, 0, [self.env.ref('base.group_portal').id])],
            })                
        else:
            pass
        return result

    # def write(self, vals):
    #     phone = vals.get('phone')
    #     record_id = self.env['res.partner'].browse(self.id)
    #     user_ids = self.env['res.users'].search([('partner_id','=',self.id)])
    #     result = super(ResPartner, self).write(vals)
    #     if phone:
    #         gene_password = randint(10 ** (6 - 1), (10 ** 6) - 1)
    #         record_id.write({'gene_password': gene_password})
    #         user_ids.write({
    #             'name': self.name,
    #             'login': phone,
    #             'password': str(gene_password),
    #         })
    #     return result

class City(models.Model):
    _name = 'winfood.city'
    _description = "City Name"
    name = fields.Char(string="City", required=True)

class TownShip(models.Model):
    _name = 'winfood.township'
    _description = "TownShip Name"
    name = fields.Char(string="TownShip", required=True)
    city_id = fields.Many2one('winfood.city', string="City", required=True)

