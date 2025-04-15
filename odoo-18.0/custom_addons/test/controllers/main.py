from odoo import http
from odoo.http import request

class TodoController(http.Controller):

    @http.route('/my/tasks', type='http', auth='user', website=True)
    def show_tasks(self):
        groups = request.env['todo.group'].sudo().search([])
        return request.render('your_module.todo_task_sidebar_page', {
            'groups': groups
        })