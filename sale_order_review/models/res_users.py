# -*- coding: utf-8 -*-

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    sign = fields.Image("Signature", max_width=1920, max_height=1920)
