# Copyright 2024 Manuel Calero - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    name = fields.Char(
        string="Description",
    )
    eco = fields.Boolean(
        string="ECO",
    )
    alfinf_trace_ids = fields.Many2one(
        string="Traza",
        comodel_name="alfinf.trace",
    )
    alfinf_detalle = fields.Char(
        string='Detalles',
    )
    alfinf_marca_id = fields.Char(
        string='Marca',
    )
    caja = fields.Char(
        string='Caja',
    )
    palet_id = fields.Char(
        string='Palet',
    )
    fecha_entrada = fields.Date(
        string='Fecha de entrada',
    )
    administrativo = fields.Boolean(
        string='Administrativo',
    )
    updateTime = fields.Datetime(
        string='Fecha modificacion',
    )
