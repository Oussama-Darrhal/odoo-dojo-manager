from odoo import models, fields

class DojoMembershipType(models.Model):
    _name = 'dojo.membership.type'
    _description = 'Membership Plan'

    name = fields.Char(string="Plan Name", required=True)
    default_price = fields.Float(string="Price")
    default_duration = fields.Integer(string="Duration (Months)", default=1)