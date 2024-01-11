# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_format = fields.Boolean(
        string='Formato'
    )

    #campos de la tabla formato
    is_in = fields.Boolean(
        string='Formato de entrada'
    )
    is_out = fields.Boolean(
        string='Formato de salida'
    )
    granel = fields.Boolean(
        string="Granel"
    )
    ft_kgFormato = fields.Float(
        string="Kilos",
        digits=(16, 2)
    )
    denominacion = fields.Char(
        string="Denominacion"
    )
    ft_grnvase = fields.Integer(
        string="Peso del envase"
    )
    euro_coste_envase = fields.Integer(
        string="Coste por envase"
    )
