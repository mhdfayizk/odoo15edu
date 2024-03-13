#-*- coding: utf-8 -*-


from odoo import api, fields, models

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    user_code = fields.Char(string="User ID"readonly="1")
    user_code_autogenerate = fields.Char(string="Code Sequence") 
    
    
        
        
    @api.model
    def create(self, vals):
        print("Hello")
        if not vals.get('user_code_autogenerate'):
            vals['user_code_autogenerate'] = self.env['ir.sequence'].next_by_code('employee.sequence')
    
        company_id = self.env['res.company'].browse(vals.get('company_id'))
        department_id = self.env['hr.department'].browse(vals.get('department_id'))
        if company_id:
            company_code = company_id.company_code
        if department_id:
            department_code = department_id.dep_code  
            if vals.get('user_code_autogenerate'):
                vals['user_code'] = f"{company_code}{department_code}{vals['user_code_autogenerate']}"
            else:
                vals['user_code'] = company_code
    
        res = super(HrEmployee, self).create(vals)
        return res  
        
    
    def write(self, vals):
        company_code=''
        department_code=''
        if 'company_id' in vals:
            new_company_id = self.env['res.company'].browse(vals.get('company_id'))
            company_code = new_company_id.company_code
            
        if 'department_id' in vals:
            new_department_id = self.env['hr.department'].browse(vals.get('department_id'))
            department_code = new_department_id.dep_code    
            
            if self.user_code_autogenerate:
                new_user_code = f"{company_code}{department_code}{self.user_code_autogenerate}"
                vals['user_code'] = new_user_code
    
        return super(HrEmployee, self).write(vals)


    
    
    