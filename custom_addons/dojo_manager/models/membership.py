from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class DojoMembership(models.Model):
    _name = 'dojo.membership'
    _description = 'Membership Subscription'

    name = fields.Char(string="Reference", required=True, copy=False, readonly=True, default='New')
    member_id = fields.Many2one('dojo.member', string="Member", required=True)
    
    # NEW: Link to the Plan
    membership_type_id = fields.Many2one('dojo.membership.type', string="Plan")
    
    # These fields are now auto-filled, but can be edited if needed
    price = fields.Float(string="Price")
    duration = fields.Integer(string="Duration (Months)")
    
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date", compute='_compute_end_date', store=True)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expired', 'Expired'),
    ], string="Status", default='draft')

    # 1. LOGIC: Auto-fill Price and Duration when Plan is selected
    @api.onchange('membership_type_id')
    def _onchange_membership_type(self):
        if self.membership_type_id:
            self.price = self.membership_type_id.default_price
            self.duration = self.membership_type_id.default_duration

    # 2. LOGIC: Calculate End Date
    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if record.start_date and record.duration:
                record.end_date = record.start_date + relativedelta(months=record.duration)
            else:
                record.end_date = False