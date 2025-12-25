from odoo import models, fields

class DojoMember(models.Model):
    _name = 'dojo.member'
    _description = 'Dojo Member'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Full Name", required=True, tracking=True)
    image = fields.Binary(string="Photo")
    belt_level = fields.Selection([
        ('white', 'White Belt'),
        ('yellow', 'Yellow Belt'),
        ('green', 'Green Belt'),
        ('blue', 'Blue Belt'),
        ('brown', 'Brown Belt'),
        ('black', 'Black Belt'),
    ], string="Belt Level", default='white', tracking=True)
    birth_date = fields.Date(string="Date of Birth")
    membership_ids = fields.One2many('dojo.membership', 'member_id', string="Subscriptions")