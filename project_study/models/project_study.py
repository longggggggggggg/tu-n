# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, tools, _
class ProjectStudy(models.Model):
    _name = 'project.study'
    REE = [('todo', 'TODO'),
           ('in-progress', 'IN-PROGRESS'),
           ('review', 'REVIEW'),
           ('done', 'DONE')]
    name = fields.Char(string="name")
    date = fields.Date(string="Date")
    dateLine = fields.Many2one('res.users', String='dateLine')
    description = fields.Html(String='description')
    status = fields.Selection(selection=REE, string='status', default='todo')
    note = fields.Text(String='Note')

    assign_to = fields.Many2one('res.users', String="Assign To", default=lambda self: self.env.user)
    user_ids = fields.One2many("study1", "err", string="dateLine")

class api(models.Model):
    _name = "study1"
    name = fields.Char(string="study1")
    err = fields.Many2one('project.study', string='user')