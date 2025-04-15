from odoo import api, fields, models, _

class TaskGroup(models.Model):
    _name = 'task.group'
    _description = 'Task Group'
    _order = 'sequence, name'

    name = fields.Char('Group Name', required=True)
    sequence = fields.Integer('Sequence', default=10)
    active = fields.Boolean(default=True)
    color = fields.Integer('Color Index')
    task_count = fields.Integer(compute='_compute_task_count', string='Task Count')
    task_ids = fields.One2many('task.task', 'group_id', string='Tasks')

    @api.depends('task_ids')
    def _compute_task_count(self):
        for group in self:
            group.task_count = len(group.task_ids)

    def action_view_tasks(self):
        self.ensure_one()
        return {
            'name': _('Tasks'),
            'res_model': 'task.task',
            'view_mode': 'tree,form',
            'domain': [('group_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'context': {'default_group_id': self.id}
        }
