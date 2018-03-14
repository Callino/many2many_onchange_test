# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.osv import osv
import logging
from datetime import date, datetime, timedelta
from openerp import tools
import hashlib
from random import randint
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class ModelA(models.Model):
    _name = 'model.a'

    @api.onchange('model_b_id')
    def onchange_model_b(self):
        self.model_c_ids = [(6, 0, self.model_b_id.model_c_ids.ids)]

    name = fields.Char(string="Name")
    model_b_id = fields.Many2one('model.b', string="Model B")
    model_c_ids = fields.Many2many('model.c', string="Model C")
