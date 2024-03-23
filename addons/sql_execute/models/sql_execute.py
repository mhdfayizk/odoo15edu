from odoo import models, fields, api

class ExecuteSQL(models.Model):
    _name = 'sql.execute'
    _description = 'Execute SQL'

    query = fields.Char(string='SQL Query')

    def execute_query(self):
        self.env.cr.execute(self.query)
        return True
