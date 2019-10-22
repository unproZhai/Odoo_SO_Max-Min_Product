# -*- coding: utf-8 -*-

from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Raise the warning "Maximum order quantity of the product <Name> is <Quantity Value>." 
    # if the order quantity is more than the 'Maximum Order Quantity' of the Product.
    @api.one
    @api.constrains('order_line')
    def check_constraint_quantity(self):
        for record in self:
            if record.order_line:
                for line in record.order_line:
                    product_id = line.product_id.id 
                    product = self.env['product.product'].browse(product_id)
                    if product.is_maximum:
                        maximum_order_qty = product.maximum_order_quantity 
                        if line.product_uom_qty > maximum_order_qty: 
                            raise ValidationError(_('Maximum order quantity of the product' +line.name+' is ' +str(maximum_order_qty)))  
