#-*- coding: utf-8 -*-

from odoo import api, fields, models

class Encuestas(models.Model):

    _inherit='res.partner'

    x_aquenivelvendeagente = fields.Selection([(1,'Local'),(2,'Regional')], string="¿Cual es su territorio?")
    x_cmt_aqueniveldistribuye = fields.Selection([(1,'Regional'),(1,'Nacional'),(1,'Exporta')], string="¿A que nivel distribuye?")
    x_cmt_calificaciondelprospecto = fields.Char(string="Calificacion del Prospecto")
    x_cmt_cargo = fields.Selection([(1,'Compras'),(1,'Mantenimiento'),(1,'Investigación y Desarrollo'),(2,'Ingeniería de Proyectos'),(2,'Líder de Proyecto'),(2,'Dueño')], string="Cargo de la Empresa")
    x_cmt_certifi = fields.Many2one('x_cmt_certifi', string="Cuenta con alguna certificacion o tiene alguna en proceso?")
    x_cmt_clientesproyectista = fields.Selection([(1,'HORECA, ej. Hotel, Rest. Cafetería'),(2,'Clientes Institucionales, ej. Walmart'),(3,'Productores, ej. Quesos Excelsior'),(4,'Plantas de procesos & Rastros, ej. Swan'),(5,'Otro')], string="¿A qué tipo de clientes atiende principalmente?")
    x_cmt_comoseenterodenosotros = fields.Selection([(1,'Web'),(1,'Referido'),(1,'Prospección'),(2,'Evento')], string="¿Como se entero de nosotros?")
    x_cmt_compitepor = fields.Selection([(1,'Precio'),(1,'Calidad')], string="Compite por:")
    x_cmt_cualessuactividadprincipal = fields.Selection([(10,'Usuario final'),(30,'Proyectista'),(20,'Profesional Técnico'),(40,'Contratista'),(60,'Distribuidor'),(70,'Fabricante'),(80,'Agente de Negocios')], string="Actividad o Giro Principal")
    x_cmt_cualessuterritorio = fields.Selection([(1,'Nacional'),(1,'Regional')], string="¿Cual es su territorio?")
    x_cmt_cualmarcadepanel = fields.Char(string="¿Cual marca de panel?")
    x_cmt_cuenta_con_bodegas_o_sucursales = fields.Boolean(string="Cuenta con sucursales o bodegas?")
    x_cmt_cuentaconcertificacion = fields.Selection([(3,'TIF'),(1,'Otra'),(1,'Ninguna')], string="¿Con que certificacion cuenta?")
    x_cmt_cuentaconpersonal = fields.Selection([(10,'Si, hasta 5'),(20,'Si, mas de 5'),(1,'No')], string="¿Cuenta con personal propio para instalaciones (cuántos)?")
    x_cmt_cuentaconpersonalproftec = fields.Selection([(10,'No'),(20,'De 1 a 3'),(30,'Más de 3')], string="¿Cuenta con personal propio para instalaciones?")
    x_cmt_distribuyealgo = fields.Selection([(1,'Equipos de Refrigeración'),(1,'Puertas Frigoríficas'),(1,'Panel')], string="¿Distribuye otras cosas tales como?")
    x_cmt_distribuyepanel = fields.Boolean(string="¿Es distribuidor de algún tipo de panel?")
    x_cmt_esdistribuidordepanel = fields.Selection([(1,'Ninguno'),(1,'Ternium'),(1,'Metenco'),(1,'Unypanel'),(1,'Otro')], string="¿Es distribuidor directo de algún tipo de panel?")
    x_cmt_instalacionesfabriles = fields.Boolean(string="¿Cuenta con instalaciones fabriles?")
    x_cmt_instalauidmismo = fields.Selection([(10,'Si'),(10,'No')], string="¿Instala Usted mismo sus proyectos?")
    x_cmt_medioseentero = fields.Selection([(1,'Web/Buscador'),(2,'Call Center'),(3,'Referido'),(4,'Mailing/Social Media'),(5,'Evento'),(6,'Otro')], string="Medio por el cual se enteró de nosotros")
    x_cmt_nivelvendesuproducto = fields.Selection([(1,'Regional'),(1,'Nacional'),(1,'Exporta')], string="¿A qué nivel vende sus productos?")
    x_cmt_otroclienteproyectista = fields.Char(string="Otro cliente")
    x_cmt_otromedio = fields.Char(string="Otro medio por el cual se enteró de nosotros")
    x_cmt_productosquealmacena = fields.Selection([(20,'Cárnicos'),(0,'Lácteos'),(0,'Frutas y Vegetales'),(0,'Planta en Proceso'),(0,'Otros')], string="¿Cuál o cuáles son los productos que produce y/o Almacena principalmente?")
    x_cmt_productosqueproduce = fields.Selection([(20,'Cárnicos'),(0,'Lácteos'),(0,'Frutas y Vegetales'),(0,'Planta en Proceso'),(0,'Otros')], string="Productos que produce y/o almacena")
    x_cmt_productosquproduceoalm = fields.Many2one('x_cmt_productosquproduceoalm', string="Productos que produce y/o almacena principalmente")
    x_cmt_productosymarcasquerepresenta = fields.Text(string="Productos y/o marcas que representa")
    x_cmt_queprdosrvleinteresa = fields.Selection([(1,'Accesorios cuartos fríos'),(1,'Puertas'),(1,'Cables calefactores'),(1,'Equipos de Control/Monitoreo'),(1,'Equipo de Refrigeración'),(1,'Asesoría Técnica'),(1,'Proyecto')], string="¿Qué producto o servicio le interesa?")
    x_cmt_quetipodebienes_otros = fields.Char(string="¿Qué otros bienes?")
    x_cmt_seespecializaenalimentaria = fields.Boolean(string="¿Se especializa solo en proyectos para la industria alimentaria?")
    x_cmt_solovendeotmbninstala = fields.Selection([(60,'Sólo vende'),(10,'Vende e Instala')], string="¿Sólo vende o también instala?")
    x_cmt_subcontrata = fields.Boolean(string="Subcontrata")
    x_cmt_tambienconstruye = fields.Selection([(30,'Sólo proyecta'),(10,'Proyecta y construye')], string="¿Su empresa solo es proyectista o también construye?")
    x_cmt_tienecertificacion2 = fields.Selection([(0,'Si'),(0,'No'),(0,'TIF')], string="¿Cuenta con alguna certificación o tiene alguna en proceso?")
    x_cmt_tienepaginaweb = fields.Boolean(string="Cuenta con página web")
    x_cmt_tienepersonaldeventas	= fields.Selection([(1,'0'),(2,'1 a 3'),(3,'4 a 10'),(4,'Más de 10')], string="¿Tiene personal propio dedicado a ventas?")
    x_cmt_tieneproyecto	= fields.Boolean(string="¿Tiene algún proyecto en este momento?")
    x_cmt_tipodeclientesatiende	= fields.Selection([(1,'HORECA'),(1,'Clientes Institucionales'),(1,'Productores'),(1,'Plastas de Procesos y Rastros')], string="¿A qué tipo de clientes atiende principalmente?")
    x_cmt_tipodedistribuidor = fields.Selection([(1,'Directo'),(1,'Distribuidores')], string="¿Cuál es su tipo de canal de distribución?")
    x_cmt_tipodeproyecto = fields.Selection([(3,'Obra nueva'),(3,'Ampliación'),(2,'Remodelación'),(1,'Mantenimiento')], string="¿Qué tipo de proyecto?")
    x_contr_cuentacnpersonal = fields.Selection([(1,'No'),(2,'de 1 a 5'),(3,'Más de 5'),(4,'Subcontrata')], string="¿Cuenta con personal propio para instalaciones?")
    x_contr_distripanel = fields.Boolean(string="¿Es distribuidor directo de algún tipo de panel?")
    x_contr_esdistdepanel = fields.Text(string="¿Qué marca de panel?")
    x_contr_esdistrideotras = fields.Boolean(string="¿Es distribuidor directo de otras cosas tales como: equipo de refrigeración, puertas, equipos de control?")
    x_contr_marcasdeotras = fields.Text(string="¿Qué marcas?")
    x_cumple = fields.Date(string="Cumpleaños")
    x_distpanel = fields.Text(string="¿De qué marca es distribuidor?")
    x_estadoslistas = fields.Selection([(1,'Aguascalientes'),(2,'Baja California Norte'),(3,'Baja California Sur'),(4,'Campeche'),(5,'Coahuila'),(6,'Colima'),(7,'Chiapas'),(8,'Chihuahua'),(9,'Distrito Federal'),(10,'Durango'),(11,'Guanajuato'),(12,'Guerrero'),(13,'Hidalgo'),(14,'Jalisco'),(15,'México'),(16,'Michoacán'),(17,'Morelos'),(18,'Nayarit'),(19,'Nuevo León'),(20,'Oaxaca'),(21,'Puebla'),(22,'Querétaro'),(23,'Quintana Roo'),(24,'San Luis Potosí'),(25,'Sinaloa'),(26,'Sonora'),(27,'Tabasco'),(28,'Tamaulipas'),(29,'Tlaxcala'),(30,'Veracruz'),(31,'Yucatán'),(32,'Zacatecas')], string="Estado en el que vende")
    x_giroprincipal = fields.Selection([(20,'Usuario final'),(30,'Proyectista'),(40,'Profesional Técnico'),(50,'Contratista'),(60,'Distribuidor'),(70,'Fabricante'),(80,'Agente de Negocios')], string="Actividad o Giro Principal de la Empresa")
    x_term_pago = fields.Many2one('account.payment_term_id', string="Terminos de Pago")
    x_sitioWebVerificado = fields.Boolean(string="Sitio Web Verificado")
    x_tiposdebienesque = fields.Many2one('x_tiposdebienesque', string="¿Qué tipo de bienes produce")
    x_tipoDeCliente = fields.Selection([(1,'Platino'),(1,'Oro'),(1,'Plata')], string="Calificación del Cliente:")
    x_tipodeclientesatiende = fields.Many2one('x_tipodeclientesatiende', string="¿A qué tipo de clientes atiende principalmente?")
    x_perfilconfirmado = fields.Text(string="Perfil Confirmado", compute='_fijar_perfil_cliente')
    x_region = fields.Char(string="Region", compute='_cambio_region')


    @api.one
    @api.depends('state_id.code')
    def _cambio_region(self):
        print " * ************************ Depurando codigo **********************"
	for record in self:
	    centrosur = ['PUE', 'TLA', 'HID', 'OAX', 'VER']
	    centro = ['GRO', 'MOR', 'DIF', 'MEX']
	    sureste = ['CAM', 'CHP', 'ROO', 'TAB', 'YUC']
	    bajio = ['GUA', 'JAL', 'MIC', 'QUE', 'SLP', 'AGU', 'COL', 'NAY', 'ZAC']
	    norte = ['COA', 'NLE', 'TAM']
	    noreste = ['SIN', 'DUR', 'CHH', 'SON']
	    bc = ['BCS', 'BCN']
	    estado = self.state_id.code
	    if estado in centrosur:
	        print " Centro - sur **********************"
	        record['x_region'] = 'Centro-Sur'
	    elif estado in centro:
	    	print " Centro ********************************"
	        record['x_region'] = 'Centro'
	    elif estado in sureste:
	    	print " Sureste **************************"
	        record['x_region'] = 'Sureste'
	    elif estado in bajio:
	    	print " Bajio **********************************"
	        record['x_region'] = 'Bajio'
	    elif estado in norte:
	    	print " Norte *******************************************"
	        record['x_region'] = 'Norte'
	    elif estado in noreste:
	    	print " Noreste *******************************************"
	        record['x_region'] = 'Noreste'
	    elif estado in bc:
	    	print " Baja calidfornia *******************************************"
	        record['x_region'] = 'Baja California'

##################################################################################################################################################################################
    @api.one
    @api.depends('x_cmt_cualessuactividadprincipal',
		 'x_cmt_tambienconstruye',
		 'x_cmt_cuentaconpersonalproftec',
		 'x_cmt_subcontrata', 
		 'x_cmt_solovendeotmbninstala', 
		 'x_cmt_productosquproduceoalm', 
		 'x_cmt_distribuyepanel',
		 'x_contr_distripanel', 
		 'x_contr_cuentacnpersonal', 
		 'x_cmt_instalacionesfabriles',
		 'x_cmt_certifi',
		 'x_cmt_cuenta_con_bodegas_o_sucursales')
    def _fijar_perfil_cliente(self):
	for record in self:
	# Proyectista
	    if (self.x_cmt_cualessuactividadprincipal == 30):
	        if (self.x_cmt_tambienconstruye == 30):
	            record['x_perfilconfirmado'] = "Proyectista"
	        elif (self.x_cmt_tambienconstruye == 10):
	            record['x_perfilconfirmado'] = "Contratista"
	        else:
	            record['x_perfilconfirmado'] = "Ninguno"
	# Profesional Tecnico
	    elif (self.x_cmt_cualessuactividadprincipal == 20):
	        if (self.x_cmt_cuentaconpersonalproftec == 30 and self.x_cmt_distribuyepanel == False or self.x_cmt_cuentaconpersonalproftec == 20 and self.x_cmt_distribuyepanel == False or self.x_cmt_cuentaconpersonalproftec == 10 and self.x_cmt_distribuyepanel == False):
	                record['x_perfilconfirmado'] = "Profesional Tecnico"
	        elif (self.x_cmt_cuentaconpersonalproftec == 30 and self.x_cmt_distribuyepanel == True):
	                record['x_perfilconfirmado'] = "Contratista"
	        else:
	            record['x_perfilconfirmado'] = "Ninguno"
	# Contratista
	    elif (self.x_cmt_cualessuactividadprincipal == 40):
	        if (self.x_contr_cuentacnpersonal == 3):
	            if (self.x_contr_distripanel == True):
	                record['x_perfilconfirmado'] = "Contratista"
	            else:
	                record['x_perfilconfirmado'] = "Profesional Tecnico"    
	        else:
	            record['x_perfilconfirmado'] = "Profesional Tecnico"
	# Distribuidor
	    elif (self.x_cmt_cualessuactividadprincipal == 60):
	        if (self.x_cmt_solovendeotmbninstala == 60 and self.x_cmt_cuenta_con_bodegas_o_sucursales==True or self.x_cmt_solovendeotmbninstala == 10 and self.x_cmt_cuenta_con_bodegas_o_sucursales==True):
	            record['x_perfilconfirmado'] = "Distribuidor"
	        elif (self.x_cmt_solovendeotmbninstala == 10 or self.x_cmt_solovendeotmbninstala == 60):
	            record['x_perfilconfirmado'] = "Contratista"
	        else:
	            record['x_perfilconfirmado'] = "Ninguno"
	# Fabricante
	    elif (self.x_cmt_cualessuactividadprincipal == 70):
	            if (self.x_cmt_instalacionesfabriles == True):
	                record['x_perfilconfirmado'] = "Fabricante"
	            else:
	                record['x_perfilconfirmado'] = "Pendiente"
	#Usuario Final
	    elif (self.x_cmt_cualessuactividadprincipal == 10):
	        if(self.x_cmt_productosquproduceoalm.name == "Ninguno"):
	            record['x_perfilconfirmado'] = "Ninguno"
	        else:
	            record['x_perfilconfirmado'] = "Usuario Final"
	    else:
	        record['x_perfilconfirmado'] = "Ninguno"






