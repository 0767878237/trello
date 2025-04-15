/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class TodoSidebar extends Component {
    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        this.groups = useState({ list: [] });

        onWillStart(async () => {
            const groupData = await this.orm.searchRead("todo.group", [], ["name"]);
            this.groups.list = groupData;
        });
    }

    openGroup(groupId) {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Tasks by Group",
            res_model: "todo.task",
            view_mode: "tree,form",
            domain: [["group_id", "=", groupId]],
        });
    }
}

TodoSidebar.template = "todo_app.TodoSidebar";

registry.category("actions").add("todo_sidebar_action", TodoSidebar);
