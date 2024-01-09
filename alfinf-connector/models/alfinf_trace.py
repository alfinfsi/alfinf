# Copyright 2024 Alberto Rodriguez - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AlfinfTrace(models.Model):
    _name = "alfinf.trace"
    _inherit = ["mail.thread"]

    name = fields.Char(
        string="Nombre",
        tracking=True
    )
    res_partner_id = fields.Many2one(
        string="Cliente",
        comodel_name="res.partner"
    )
    active = fields.Boolean(default=True)
