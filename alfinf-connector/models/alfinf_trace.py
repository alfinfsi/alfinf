# Copyright 2024 Alberto Rodriguez - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AlfinfTrace(models.Model):
    _name = "alfinf.trace"

    name = fields.Char(
        string="Nombre"
    )
    res_partner_id = fields.Many2one(
        string="Cliente",
        comodel_name="res.partner"
    )
