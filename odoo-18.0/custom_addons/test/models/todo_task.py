from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Trello Task'

    name = fields.Char(string='Module Name', required=True)
    description = fields.Char(string="Technical Name", required=True)
    author = fields.Char(string="Author", required=True)
    website = fields.Char(string="Website", required=True)
    due_date = fields.Date(string='Due Date')
    done = fields.Boolean(string="Done", default=False)

    group_id = fields.Many2one('todo.group', string="Group")
