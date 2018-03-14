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


class ModelB(models.Model):
    _name = 'model.b'

    name = fields.Char(string="Name")
    model_c_ids = fields.Many2many('model.c', string="Model C")
