from email.contentmanager import raw_data_manager
import string, random
from odoo import fields, api, models
from random import randint, randrange

class ResPartner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one('winfood.city', string="City" , domain="[('state_id', '=', state_id)]")
    township_id = fields.Many2one('winfood.township', string="TownShip", domain="[('city_id', '=', city_id)]")
    phone = fields.Char(required=True)
    gene_password = fields.Char(string="Password",readonly=True)

    @api.model
    def create(self, vals):
        result = super(ResPartner, self).create(vals)
        
        phone = vals.get('phone')
        gene_password = None
        if phone:
            # auto Generate Password
            gene_password = randint(10**(6-1), (10**6)-1)
            
            name = vals.get('name')
            result.write({'gene_password':gene_password})
            portal_user = self.env['res.users'].create({
                'name': name,
                'login': phone,
                'password': gene_password,
                'partner_id': result.id,
                'groups_id': [(6, 0, [self.env.ref('base.group_portal').id])],
            })
        return result

class City(models.Model):
    _name = 'winfood.city'
    _description = "City Name"
    name = fields.Char(string="City", required=True)
    state_id = fields.Many2one('res.country.state', string='State')

class TownShip(models.Model):
    _name = 'winfood.township'
    _description = "TownShip Name"
    name = fields.Char(string="TownShip", required=True)
    city_id = fields.Many2one('winfood.city', string="City", required=True)


