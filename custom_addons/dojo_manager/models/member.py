from odoo import models, fields, api

class DojoMember(models.Model):
    _name = 'dojo.member'
    _description = 'Dojo Member'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True, tracking=True)
    image = fields.Image(string="Photo")
    birth_date = fields.Date(string="Date of Birth")
    belt_level = fields.Selection([
        ('white', 'White'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('brown', 'Brown'),
        ('black', 'Black'),
    ], string="Belt Rank", default='white', tracking=True)
    
    membership_ids = fields.One2many('dojo.membership', 'member_id', string="Memberships")
    membership_count = fields.Integer(string="Membership Count", compute='_compute_membership_count')

    @api.depends('membership_ids')
    def _compute_membership_count(self):
        for record in self:
            record.membership_count = len(record.membership_ids)

    def action_view_memberships(self):
        return {
            'name': 'Memberships',
            'type': 'ir.actions.act_window',
            'res_model': 'dojo.membership',
            'view_mode': 'tree,form',
            'domain': [('member_id', '=', self.id)],
            'context': {'default_member_id': self.id},
        }

    # FIX: Pointing to the ACTION, not the TEMPLATE
    def action_open_certificate(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': '/report/html/dojo_manager.action_report_membership_card/%s' % self.id,
            'target': 'new',
        }