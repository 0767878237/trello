from odoo import models, fields

class TodoGroup(models.Model):
    _name = 'todo.group'
    _description = 'Task Group'

    name = fields.Char('Group Name', required=True)
    task_ids = fields.One2many('todo.task', 'group_id', string='Tasks')
