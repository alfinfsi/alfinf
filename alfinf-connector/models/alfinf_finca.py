# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfFinca(models.Model):
    _name = 'alfinf.finca'
    _rec_name = 'nombre'

    nombre = fields.Char(
        string='Finca',
        required=True,
        help='Nombre de la finca',
    )
    hectareas_producidas = fields.Integer(
        string='Hectareas producidas',
    )
    municipio = fields.Char(
        string='Municipio'
    )
    poligono = fields.Char(
        string="poligono"
    )
    country_id = fields.Many2one(
        string='Pais',
        comodel_name='res.country',
        inverse_name='alfinf_finca_id'
    )
    provincia_id = fields.Many2one(
        string='Provincia',
        comodel_name='res.country.state',
        inverse_name='alfinf_finca_id'
    )
