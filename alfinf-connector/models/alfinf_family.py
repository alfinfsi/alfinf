# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models


class AlfinfFamily(models.Model):
    _name = 'alfinf.family'
    _description = 'Familia'
    _rec_name = 'familia'   #En las relaciones, este es el campo que se muestra

    familia = fields.Char(
        string='Familia',
        tracking=True
    )
    cod_intrastat = fields.Char(
        string='id_intrastat',
    )
    cgn = fields.Char(
        string='CGN'
    )
