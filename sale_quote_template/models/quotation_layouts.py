# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LayoutLayout(models.Model):
    _name = 'layout.layout'
    _description = "Layouts"

    name = fields.Char(string="Name")


class QuoteLayout(models.Model):
    _name = 'quote.layout'
    _description = 'Quotation Layouts'

    name = fields.Char(string="Content Name")
    layout_id = fields.Many2one('layout.layout')
    content = fields.Html(string='Content')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    layout_id = fields.Many2one('layout.layout')
    quote_layout_ids = fields.One2many('sale.order.line.layouts', 'order_id', string="Layouts")

    @api.onchange('layout_id')
    def onchange_layout_values(self):
        report_lines = [(5, 0, 0)]
        layouts = self.env['quote.layout'].search([('layout_id', '=', self.layout_id.id)])
        if layouts:
            for vals in layouts:
                data = {
                    'layout_id': self.layout_id.id,
                    'quote_layout_id': vals.id,
                    'content': vals.content
                }
                report_lines.append((0, 0, data))
        self.quote_layout_ids = report_lines


class SaleOrderLineLayouts(models.Model):
    _name = 'sale.order.line.layouts'

    order_id = fields.Many2one('sale.order', string="Sale Order")
    layout_id = fields.Many2one('layout.layout')
    quote_layout_id = fields.Many2one('quote.layout', string="Content Name")
    content = fields.Html(string="Content")

    @api.onchange('quote_layout_id')
    def change_quote_layout_id(self):
        if self.quote_layout_id:
            self.content = self.quote_layout_id.content
