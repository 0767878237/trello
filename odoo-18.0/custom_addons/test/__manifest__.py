{
    'name': 'test', # ten hien thi
    'version': '1.0',
    'summary': 'anh tuan',
    'author': 'Le Duc Anh Tuan',
    'category': 'Productivity',
    'depends': ['base', 'website'],
    'license': 'LGPL-3',
    'data': [
       'views/todo_task_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'test/static/src/js/todo_sidebar.js',
            'test/static/src/xml/todo_sidebar.xml',
        ],
    },
    'installable': True,
    'application': True,
}