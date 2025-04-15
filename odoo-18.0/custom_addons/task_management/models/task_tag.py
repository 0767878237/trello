from odoo import api, fields, models, _

class TaskTag(models.Model):
    _name = 'task.tag'
    _description = 'Task Tag'

    name = fields.Char('Name', required=True)
    color = fields.Integer('Color Index')