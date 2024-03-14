# Copyright 2024 Manuel Calero - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'


    is_trace = fields.Boolean(
        string='Traza'
    )
    cont_id = fields.Char(
        string='Id contabilidad'
    )
    cl_cif = fields.Char(
        string='CIF'
    )
    idniff = fields.Integer(
        string='ID NIF'
    )
    alfinf_trace_ids = fields.One2many(
        string='Traza',
        comodel_name='alfinf.trace',
        inverse_name='res_partner_id'
    )
