# Copyright 2024 Alberto Rodriguez - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models


class AlfinfTrace(models.Model):
    _name = 'alfinf.trace'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Traza',
        tracking=True
    )
    tz_hectarea = fields.Char(
        string='Traza hectarea'
    )
    campania = fields.Char(
        string ='Camapaña'
    )
    id_sector=fields.Integer(
        string ='sector'
    )
    eco = fields.Boolean(
        string='Eco'
    )
    ggn = fields.Char(
        string='GGN'
    )
    tz_parcela = fields.Char(
        string='Traza parcela'
    )
    tz_columna = fields.Char(
        string='Traza columna'
    )
    tz_planta = fields.Char(
        string='Traza planta'
    )
    replante = fields.Char(
        string='Repelente'
    )
    res_partner_id = fields.Many2one(
        string='Cliente',
        comodel_name='res.partner'
    )
    variedad_id = fields.Many2one(
        string='Variedad',
        comodel_name='alfinf.variedad'
    )
    vivero_id = fields.Char(
        string = 'Vivero'
    )
    active = fields.Boolean(
        default=True
    )
