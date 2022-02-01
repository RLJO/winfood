from odoo import fields,api,_,models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one('winfood.city',string="City")
    township_name = fields.Many2one('winfood.township',string="Township",domain="[('city_id', '=', city_id)]")

    @api.model
    def get_values(self):
        res = super(ResPartner, self).get_values()

        params = self.env['ir.config_parameter'].sudo()
        partner = params.get_param('partner', default=False)
        res.update(
            partner=int(partner),
        )
        return res

    def set_values(self):
        super(ResPartner, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("partner", self.partner.id)

class City(models.Model):
    _name = 'winfood.city'
    _description = "City Name"
    name = fields.Char(string="City",required=True)

class TownShip(models.Model):
    _name = 'winfood.township'
    _description = "TownShip Name"
    name = fields.Char(string="TownShip",required=True)
    city_id = fields.Many2one('winfood.city', string="City", required=True)