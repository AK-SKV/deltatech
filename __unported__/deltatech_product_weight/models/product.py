# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2015 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    barcode = fields.Char(related=False)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    volume = fields.Float(compute="_compute_volume", store=False) #compute="_compute_volume", inverse="_set_volume", store=False)related="product_tmpl_id.volume"
    weight = fields.Float(compute="_compute_weight", store=False) #compute="_compute_weight", inverse="_set_weight", store=False)related="product_tmpl_id.weight"



    @api.multi
    @api.depends('product_tmpl_id.volume')
    def _compute_volume(self):
        for product in self:
            volume = float(product.product_tmpl_id.volume)
            if volume:
                product.volume = volume

    @api.multi
    @api.depends('product_tmpl_id.weight')
    def _compute_weight(self):
        for product in self:
            weight = float(product.product_tmpl_id.weight)
            if weight:
                product.weight = weight


    """
    @api.one
    def _set_weight(self):
        if self.product_tmpl_id.weight and self.product_tmpl_id.weight != self.weight:
            self.product_tmpl_id.weight = self.weight


    @api.multi
    def _set_volume(self):
        for product in self:
            if product.product_tmpl_id.volume:
                product.product_tmpl_id.volume = product.volume


    """