#-*- coding: utf-8 -*-


from odoo import api, fields, models

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    user_code = fields.Char(string="User ID")
    user_code_autogenerate = fields.Char(string="Code Sequence") 
    
    
        
        
    @api.model
    def create(self, vals):
        print("Hello")
        if not vals.get('user_code_autogenerate'):
            vals['user_code_autogenerate'] = self.env['ir.sequence'].next_by_code('employee.sequence')

        company_id = self.env['res.company'].browse(vals.get('company_id'))
        if company_id:
            company_code = company_id.company_code  # Replace with the correct attribute name
            if vals.get('user_code_autogenerate'):
                vals['user_code'] = f"{company_code}{vals['user_code_autogenerate']}"
            else:
                vals['user_code'] = company_code

        res = super(HrEmployee, self).create(vals)
        return res  
        
        