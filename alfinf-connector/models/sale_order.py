# Copyright 2024 Manuel Calero - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    alfinf_avfid = fields.Integer(
        string='Alfinf ID'
    )
    transportista_id = fields.Many2one(
        string='transportista',
        comodel_name='res.partner',
        inverse_name='id'
    )
    consignataria_id = fields.Char(
        string='Consignatario'
    )
    matricula_camion = fields.Char(
        string='Matricula camión'
    )
    matricula_remolque = fields.Char(
        string='Matricula remolque'
    )
    temperatura_carga = fields.Float(
        string='Temperatura carga'
    )
    ch_cargado= fields.Boolean(
        string='Cargado'
    )
    ch_revisado= fields.Boolean(
        string='Revisado'
    )
    ch_diferencia= fields.Boolean(
        string='Diferencia'
    )
