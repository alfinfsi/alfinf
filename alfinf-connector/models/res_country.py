# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class ResCountry(models.Model):
    _inherit = "res.country"


    alfinf_finca_ids= fields.One2many(
        string='Fincas',
        comodel_name='alfinf.finca',
        inverse_name='country_id',
    )

