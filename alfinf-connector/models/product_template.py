# Copyright 2024 Manuel Calero - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_format = fields.Boolean(
        string='Formato'
    )
    is_in = fields.Boolean(
        string='Entrada'
    )
    is_out = fields.Boolean(
        string='Salida'
    )


