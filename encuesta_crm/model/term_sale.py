#-*- coding:utf-8 -*-
from odoo import models, fields

class Certifi(models.Model):

    _inherit='sale.order'

    x_condiciones_pago = fields.Boolean(string="Condiciones de Pago")
    x_tipo_condicion = fields.Selection([(1,'30% anticipo/70% según condiciones'),(2,'40% anticipo/60% según condiciones'),(3,'50% anticipo/50% según condiciones'),(4,'60% anticipo/40% según condiciones')], string="Tipo de Condición")

