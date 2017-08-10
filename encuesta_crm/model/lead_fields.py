#-*- coding: utf-8 -*-
from odoo import api, fields, models

class Lead_fields(models.Model):

    _inherit='crm.lead'

    x_cmt_calif = fields.Boolean(string="Calificacion", readonly=True)
    x_cmt_certificacion = fields.Boolean(string="¿Es cliente activo?")
    x_cmt_fasedeproyecto = fields.Selection([(1,'Planeación'),(2,'Cotización'),(3,'Ejecución')], string="¿En quéfase se encuentra su proyecto")
    x_cmt_interested = fields.Integer(string="Interesado", readonly=True, compute="_get_interested")
    x_cmt_productoleinteresa = fields.Many2one('x_cmt_productoleinteresa', string="¿Qué producto o servicio le interesa")
    x_cmt_productosprodoalm = fields.Many2one('x_cmt_productosquproduceoalm', string="¿Cuáles son los productos que produce y/o almacena principalmente?")
    x_cmt_projecttype = fields.Selection([(4,'Obra nueva'),(3,'Ampliación'),(2,'Remodelación'),(1,'Mantenimiento')], string="Tipo de Proyecto")
    x_cmt_quali = fields.Integer(string="Interés", compute="_get_calif", readonly=True)
    x_cmt_quienhizolallamada = fields.Selection([(1,'Outbound'),(1,'Inbound')], string="¿Quién hizo la llamada?")

    @api.one
    @api.depends('x_cmt_certificacion', 'x_cmt_fasedeproyecto', 'x_cmt_projecttype')
    def _get_calif(self):
        for record in self:
            record['x_cmt_calif'] = self.x_cmt_certificacion + self.x_cmt_fasedeproyecto + self.x_cmt_projecttype
    def _get_interested(self):
        for record in self:
            x_fase = self.x_cmt_fasedeproyecto
            if x_fase == 3:
                x_fase = 1
            elif x_fase == 2:
                x_fase = 1
            else:
                x_fase = 0
            x_certification = self.x_cmt_certificacion
            x_projecttype = self.x_cmt_projecttype
            if x_projecttype == 4:
                x_projecttype = 1
            elif x_projecttype == 3:
                x_projecttype = 1
            elif x_projecttype == 2:
                x_projecttype = 1
            else:
                x_projecttype = 0
            record['x_cmt_interested'] = x_fase + x_certification + x_projecttype
