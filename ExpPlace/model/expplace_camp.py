from odoo import api, fields, models

class Expplace(models.Model):
    _inherit = 'account.invoice'
    
    x_Expedicion = fields.Char(string="Lugar de Expedicion", compute='_cambio_lugar')
    
    @api.one
    @api.depends('user_id.name')
    def _cambio_lugar(self):
        for record in self:
            Matriz = ['UNIMEGAS JUAREZ']
            Sucursal = ['UNIMEGAS CHIHUAHUA']
            
            lugar = self.user_id.name
            if lugar in Matriz:
                record['x_Expedicion'] = 'MATRIZ JUÁREZ'
            elif lugar in Sucursal:
                record['x_Expedicion'] = 'SUCURSAL CHIHUAHUA'