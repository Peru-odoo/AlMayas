from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    is_omit_move_line = fields.Boolean(string="Omit Move Line",Default=False)
