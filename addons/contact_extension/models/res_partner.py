import string, random
from odoo import fields, api, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one('winfood.city', string="City")
    township_name = fields.Many2one('winfood.township', string="TownShip", domain="[('city_id', '=', city_id)]")
    phone = fields.Char(required=True)
    gene_password = fields.Char(string="Password",readonly=True)

    @api.model
    def create(self, vals):
        name = vals.get('name')
        phone = vals.get('phone')
        if phone:
            characters = list(string.digits)
            password = []
            for i in range(8):
                password.append(random.choice(characters))
            random.shuffle(password)
            listToStr = ' '.join([str(elem) for elem in password])
            gene_password = listToStr
        result = super(ResPartner, self).create(vals)
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

class TownShip(models.Model):
    _name = 'winfood.township'
    _description = "TownShip Name"
    name = fields.Char(string="TownShip", required=True)
    city_id = fields.Many2one('winfood.city', string="City", required=True)


