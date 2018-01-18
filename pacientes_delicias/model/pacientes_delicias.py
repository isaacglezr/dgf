from odoo import api, fields, models

class Pacientes_delicias(models.Model):
    _name='pacientes.delicias'
    
    x_paciente = fields.Many2one('res_partner', string='Paciente')
    x_FechaEntrada = fields.Datetime(string='Fecha de Ingeso')
    x_FechaSalida = fields.Datetime(string='Fecha de Alta')
    x_Expediente = fields.Char(string='Expediente')
    x_Doctor = fields.Many2one('res_partner', string='Doctor')
    x_MediMaterial= fields.Many2many('product_product', string='Medicamento/Material')
    
    #Habitacion
    x_Habitacion = fields.Boolean(string='Requiere Habitacion')
    x_NumHabitacion = fields.Many2one(string='Numero de Habitacion')
    
    #Quirofano
    x_Quirofano = fields.Boolean(string='Quirofano')
    x_NumQuirofano = fields.Many2one(string='Sala de Quirofano')
