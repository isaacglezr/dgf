from odoo import api, fields, models

class CodeUse_field(models.Model):
    _inherit = 'account.invoice'
    
    x_UseCode = fields.Char(string="Codigo Uso", compute='_cambio_code')
    
    @api.one
    @api.depends('l10n_mx_edi_usage')
    def _cambio_code(self):
        for record in self:
            if (self.l10n_mx_edi_usage == 'G01'):
                record['x_UseCode'] = 'G01'
            elif (self.l10n_mx_edi_usage == 'G02'):
                record['x_UseCode'] = 'G02'
            elif (self.l10n_mx_edi_usage == 'G03'):
                record['x_UseCode'] = 'G03'
            elif (self.l10n_mx_edi_usage == 'I01'):
                record['x_UseCode'] = 'I01'
            elif (self.l10n_mx_edi_usage == 'I02'):
                record['x_UseCode'] = 'I02'
            elif (self.l10n_mx_edi_usage == 'I03'):
                record['x_UseCode'] = 'I03'
            elif (self.l10n_mx_edi_usage == 'I04'):
                record['x_UseCode'] = 'I04'
            elif (self.l10n_mx_edi_usage == 'I05'):
                record['x_UseCode'] = 'I05'
            elif (self.l10n_mx_edi_usage == 'I06'):
                record['x_UseCode'] = 'I06'
            elif (self.l10n_mx_edi_usage == 'I07'):
                record['x_UseCode'] = 'I07'
            elif (self.l10n_mx_edi_usage == 'I08'):
                record['x_UseCode'] = 'I08'
            elif (self.l10n_mx_edi_usage == 'D01'):
                record['x_UseCode'] = 'D01'
            elif (self.l10n_mx_edi_usage == 'D02'):
                record['x_UseCode'] = 'D02'
            elif (self.l10n_mx_edi_usage == 'D03'):
                record['x_UseCode'] = 'D03'
            elif (self.l10n_mx_edi_usage == 'D04'):
                record['x_UseCode'] = 'D04'
            elif (self.l10n_mx_edi_usage == 'D05'):
                record['x_UseCode'] = 'D05'
            elif (self.l10n_mx_edi_usage == 'D06'):
                record['x_UseCode'] = 'D06'
            elif (self.l10n_mx_edi_usage == 'D07'):
                record['x_UseCode'] = 'D01'
            elif (self.l10n_mx_edi_usage == 'D08'):
                record['x_UseCode'] = 'D08'
            elif (self.l10n_mx_edi_usage == 'D09'):
                record['x_UseCode'] = 'D09'
            elif (self.l10n_mx_edi_usage == 'D010'):
                record['x_UseCode'] = 'D010'
            elif (self.l10n_mx_edi_usage == 'P01'):
                record['x_UseCode'] = 'P01'
            else:
                record['x_UseCode'] = 'Sin Asignar'