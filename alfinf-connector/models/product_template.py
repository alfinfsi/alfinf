# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


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
    ft_grnvase = fields.Float(
        string="Kilos Formato"
    )
    euro_coste_envase = fields.Integer(
        string="Coste por envase"
    )
    piezas = fields.Integer(
        string="Piezas"
    )
    gr_pieza = fields.Float(
        string="gr piezas",
        compute='_compute_gr_piezas'
    )
    categoria = fields.Integer(
        string="Categoria",
        default=1,
        domain=[
            ('>=', 0)
        ]
    )
    unidades = fields.Integer(
        string="Unidades",
        domain=[
            ('>=', 1)
        ]
    )
    peso_entrada = fields.Float(
        string="Peso entrada",
        digits=(16, 2)
    )
    peso_salida = fields.Float(
        string="Peso salida",
        digits=(16, 2)
    )
    coste_formato = fields.Float(
        string="Coste formato",
        digits=(16, 2)
    )
    kg_plastico = fields.Float(
        string="Kilos de plastico no reciclados"
    )

    # Campos calculados

    @api.depends('ft_kgFormato', 'piezas')
    def _compute_gr_piezas(self):
        for product in self:
            if product.piezas != 0:
                product.gr_pieza = product.ft_kgFormato / product.piezas
            else:
                product.gr_pieza = 0
