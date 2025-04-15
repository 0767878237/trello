{
    'name': 'Task Management',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Manage tasks with sidebar filtering',
    'description': """
Task Management System
=====================
This module provides a task management interface with:
- Left sidebar for categories/groups
- Right panel for filtered tasks
- Automatic grouping functionality
""",
    'author': 'Anh Tuan',
    'website': 'https://www.yourwebsite.com',
    'depends': ['base', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/task_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'task_management/static/src/scss/task_management.scss',
            'task_management/static/src/js/task_management.js',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
