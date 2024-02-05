# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfRecinto(models.Model):
    _name = "alfinf.recinto"
    _description = "Recinto"
    _rec_name = "recinto"

    recinto = fields.Char(
        string="Recinto",
    )
    hectareas_producidas = fields.Integer(
        string="Hectareas producidas",
    )
