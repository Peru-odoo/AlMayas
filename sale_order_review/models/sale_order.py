# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('review', 'Under Review'), ('approve', 'Reviewed'), ('sent',)])
    rev_sale_id = fields.Many2one('sale.order', string="Revision Of", copy=False)
    src_sale_id = fields.Many2one('sale.order', string="Source", copy=False)
    rev_sale_ids = fields.One2many('sale.order', 'rev_sale_id', string="Sale History", copy=False)
    rev_count = fields.Integer(string="Reverse Orders", compute="reversed_order_count", copy=False)
    src_sale_ids = fields.One2many('sale.order', 'src_sale_id', string="Sale History", copy=False)
    org_sale_id = fields.Many2one('sale.order', string="Origin", copy=False, )
    src_count = fields.Integer(string="src Orders", compute="src_order_count", copy=False)
    is_revised = fields.Boolean(string="Is Revised", copy=False)

    # def action_cancel(self):
    #     if self.rev_sale_ids:
    #         raise UserError

    def action_sent_review(self):
        self.state = 'review'

    def action_order_approve(self):
        self.state = 'approve'

    # def action_quotation_send(self):
    #     self.state = 'draft'
    #     return super(SaleOrder, self).action_quotation_send()

    def revise_quotation(self):
        new_quote = self.copy()
        self.is_revised = True

        if self.org_sale_id:
            new_quote.org_sale_id = self.org_sale_id.id
        else:
            new_quote.org_sale_id = self.id
        self.src_sale_id = new_quote.id
        self.rev_sale_id = new_quote.id
        new_quote.rev_sale_ids = new_quote.rev_sale_ids + self.rev_sale_ids
        new_quote.name = new_quote.org_sale_id.name + "/Rev" + str(len(new_quote.rev_sale_ids))
        self.state = 'cancel'
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'views': [(False, 'form')],
            'res_id': new_quote.id,
        }

    @api.depends('rev_sale_ids')
    def reversed_order_count(self):
        self.rev_count = len(self.rev_sale_ids)

    @api.depends('src_sale_ids')
    def src_order_count(self):
        self.src_count = len(self.src_sale_ids)

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        self.state = 'draft'
        return super(SaleOrder, self.with_context(mail_post_autofollow=True)).message_post(**kwargs)
