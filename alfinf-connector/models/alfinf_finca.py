# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfFinca(models.Model):
    _name = "alfinf.finca"

    finca = fields.Char(
        string="Finca",
        required=True,
        help="Nombre de la finca",
    )
    hectareas_producidas = fields.Integer(
        string="Hectareas producidas",
    )
