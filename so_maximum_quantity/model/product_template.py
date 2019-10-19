# -*- coding: utf-8 -*-

from odoo import api,fields,models,_

class ProductTemplate(models.Model):
    _inherit="product.template"

    is_maximum = fields.Boolean(
        string="Is Product Limited",
        help="Check this field if this product has a maximum limit.")

    maximum_order_quantity = fields.Float(
    	string='Maximum Order Quantity',
    	help="This field display maximum ordereds qunatity.")

