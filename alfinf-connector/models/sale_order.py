# Copyright 2024 Manuel Calero - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    alfinf_avfid = fields.Integer(
        string='Alfinf ID'
    )
