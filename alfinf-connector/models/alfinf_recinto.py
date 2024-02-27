# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfRecinto(models.Model):
    _name = 'alfinf.recinto'
    _description = 'Recinto'
    _rec_name = 'recinto'

    recinto = fields.Char(
        string='Recinto',
    )
    hectareas_producidas = fields.Float(
        string='Hectareas producidas',
    )
    finca_id = fields.Many2one(
        string='Finca',
        comodel_name='alfinf.finca',
        inverse_name='alfinf_recinto_id'
    )
    traza_id = fields.One2many(
        string='Traza',
        comodel_name='alfinf.trace',
        inverse_name='tz_recinto_id'
    )
