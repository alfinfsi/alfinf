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
    tz_hectarea = fields.Char(
        string="Traza hectarea"
    )
    tz_parcela = fields.Char(
        string="Traza parcela"
    )
    tz_columna = fields.Char(
        string="Traza columna"
    )
    tz_planta = fields.Char(
        string="Traza planta"
    )
    res_partner_id = fields.Many2one(
        string="Cliente",
        comodel_name="res.partner"
    )
    variedad_id = fields.Char(
        string="Variedad"
        #comodel_name="variedad"
    )
    active = fields.Boolean(default=True)
