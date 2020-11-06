# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FormularioParametrizacion(models.Model):
    _name = 'keralty_module.formulario.param'
    _description = 'Formulario Parametrización'

    nombre_codigo = fields.Char(required=True, string="Nombre o Código")
    casilleros = fields.Float(string="Área de casilleros para funcionarios", required=True, help="Area de casilleros para funcionarios", digits=(8, 2))
    banios_hombres = fields.Float(string="Baños públicos hombres", required=True, help="Baños públicos hombres", digits=(8, 2))
    banios_mujeres = fields.Float(string="Baños públicos mujeres", required=True, help="Baños públicos mujeres", digits=(8, 2))
    banios_hombres_disc = fields.Float(string="Baños públicos hombres en condición de discapacidad.", required=True, help="Baños publícos hombres en condición de discapacidad", digits=(8, 2))
    banios_mujeres_disc = fields.Float(string="Baños públicos mujeres en condición de discapacidad", required=True, help="Baños públicos mujeres en condición de discapacidad", digits=(8, 2))
    cafeteria_empleados = fields.Float(string="Cafeteria empleados", required=True, help="Cafeteria empleados", digits=(8, 2))
    cuarto_aseo = fields.Float(string="Cuarto de aseo (poceta)", required=True, help="Cuarto de aseo (poceta)", digits=(8, 2))
    banios_hombres_emp = fields.Float(string="Baño hombres para empleados", required=True, help="Baño hombres para empleados", digits=(8, 2))
    banios_mujeres_emp = fields.Float(string="Baño mujeres para empleados", required=True, help="Baño mujeres para empleados", digits=(8, 2))
    # Laboratorio
    banios_hombres_lab = fields.Float(string="Baños públicos hombres laboratorio", required=True, help="Baños públicos hombres laboratorio", digits=(8, 2))
    banios_mujeres_lab = fields.Float(string="Baños públicos mujeres laboratorio", required=True, help="Baños públicos mujeres laboratorio", digits=(8, 2))
    banios_hombres_lab_disc = fields.Float(string="Baños públicos hombres en condición de discapacidad laboratorio", required=True, help="Baños públicos hombres en condición de discapacidad laboratorio", digits=(8, 2))
    banios_mujeres_lab_disc = fields.Float(string="Baños públicos mujeres en condición de discapacidad laboratorio", required=True, help="Baños públicos mujeres en condición de discapacidad laboratorio", digits=(8, 2))
    banio_mixto = fields.Float(string="Baño mixto para empleados", required=True, help="Baño mixto para empleados", digits=(8, 2))
    vestier = fields.Float(string="Vestier con casilleros mixto para empleados", required=True, help="Vestier con casilleros mixto para empleados", digits=(8, 2))
    oficina_admon = fields.Float(string="Oficina coordinación adminsitrativa", required=True, help="Oficina coordinación adminsitrativa", digits=(8, 2))

    #     value = fields.Integer()

class FormularioCliente(models.Model):
    _name = 'keralty_module.formulario.cliente'
    _description = 'Formulario Cliente'

    #
    nombre_proyecto = fields.Char(required=True, string="Nombre Proyecto")
    # Ocupación centro médico
    numero_usuarios = fields.Float(string="Número de Usuarios", required=True, help="Número de Usuarios")
    numero_empleados = fields.Float(string="Número de Empleados", required=True, help="Número de Empleados")
    terceros = fields.Float(string="Terceros", required=True, help="Terceros")

    def action_confirmar_proyecto(self):
        print("Confirmar proyecto")
        return True

class FormularioValidacion(models.Model):
    _name = 'keralty_module.formulario.validacion'
    _description = 'Formulario Validacion'

    nombre_tecnico = fields.Char(required=True, string="Nombre Proyecto")
    descripcion = fields.Char(required=True, string="Descripcion")
    formulario_cliente = fields.Many2one(string="Formulario Cliente", comodel_name='keralty_module.formulario.cliente',
                    help="Formulario Cliente asociado para validacion tecnica.")

# hereda de producto y añade campo para relación con Categoría
class ProductProduct(models.Model):
    _inherit = 'product.product'
    categorias_ids = fields.Char(required=True, string="Categorias")
    #categoria_ids = fields.Many2one(string="Categorías", comodel_name='keralty_module.categoria',
    #                                help='Categorías asociadas al producto.')

class Categoria(models.Model):
    _name = 'keralty_module.categoria'
    _description = 'Categoria'

    formulario_cliente = fields.Many2one(string="Formulario Cliente", comodel_name='keralty_module.formulario.cliente',
                    help="Formulario Cliente asociado para validacion tecnica.")
    #productos_asociados = fields.One2many('product.TEMPLATE', 'categoria_ids', 'Productos Asociados')


# class keralty_module(models.Model):
#     _name = 'keralty_module.keralty_module'
#     _description = 'keralty_module.keralty_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Char(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = Char(record.value) / 100
