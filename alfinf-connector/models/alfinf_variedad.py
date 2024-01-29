# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfVariedad(models.Model):
    _name= "alfinf.variedad"
    _rec_name = "nombre"

    nombre= fields.Char(
        string="nombre"
    )

    familia_id = fields.Many2one(
        'alfinf.family',  # Modelo que contiene el nombre de la familia
        string='familia',
        required=True,
        ondelete='restrict',
    )
