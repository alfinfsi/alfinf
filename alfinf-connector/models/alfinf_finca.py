# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models, api

class AlfinfFinca(models.Model):
    _name = 'alfinf.finca'
    _rec_name = 'nombre'
    _sql_constraints = [
        #('alfinf_finca_nombre_uniq', 'unique(nombre)', 'Ya existe'),
    ]


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
    parcela_ids = fields.One2many(
        string='parcela',
        comodel_name='alfinf.parcela',
        inverse_name='finca_id'
    )
    trace_ids = fields.Many2one(
        string='Traza',
        comodel_name='alfinf.trace',
        inverse_name='tz_parcela_id'
    )

    #   Eliminar constraint
    #   @api.onchange('provincia_id')
    #   def onchange_country_id(self):
    #       self.env.cr.execute("ALTER TABLE alfinf_finca DROP CONSTRAINT alfinf_finca_nombre_uniq;")
