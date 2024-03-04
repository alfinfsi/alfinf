# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfParcela(models.Model):
    _name = 'alfinf.parcela'
    _description = 'Parcelas'
    _rec_name = 'parcela'

    parcela = fields.Char(
        string='Parcela',
    )
    hectareas_producidas = fields.Float(
        string='Hectareas producidas',
    )
    finca_id = fields.Many2one(
        string='Finca',
        comodel_name='alfinf.finca',
        inverse_name='alfinf_parcela_id'
    )
    traza_id = fields.One2many(
        string='Traza',
        comodel_name='alfinf.trace',
        inverse_name='tz_parcela_id'
    )
