from odoo import api, fields, models, _

class Task(models.Model):
    _name = 'task.task'
    _description = 'Task'
    _order = 'priority desc, sequence, id desc'

    name = fields.Char('Task Name', required=True)
    description = fields.Text('Description')
    sequence = fields.Integer('Sequence', default=10)
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Urgent')
    ], default='1', string='Priority')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='draft', string='Status')
    deadline = fields.Date('Deadline')
    group_id = fields.Many2one('task.group', string='Group')
    user_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('task.tag', string='Tags')
    color = fields.Integer('Color Index')
    active = fields.Boolean(default=True)

    def action_in_progress(self):
        self.write({'state': 'in_progress'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})