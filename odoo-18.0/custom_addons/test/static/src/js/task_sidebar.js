odoo.define('intern_devs_task_sidebar.sidebar', function (require) {
    'use strict';

    const KanbanController = require('web.KanbanController');

    KanbanController.include({
        start: function () {
            this._super.apply(this, arguments);
            this._bindSidebarEvents();
        },

        _bindSidebarEvents: function () {
            const self = this;
            $('.o_task_sidebar .sidebar-item').on('click', function () {
                const filter = $(this).data('filter');
                // Example: filter by domain
                let domain = [];
                if (filter === 'My Tasks') {
                    domain = [['user_id', '=', self.getSession().uid]];
                } else if (filter === 'Today') {
                    const today = moment().format('YYYY-MM-DD');
                    domain = [['date_deadline', '=', today]];
                }
                self.model.load({ domain: domain });
            });
        },
    });
});
