#-*- coding: utf-8 -*-


from odoo import api, fields, models

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    user_code = fields.Char(string="User ID")
    user_code_autogenerate = fields.Char(string="Code Sequence") 
    
    
        
    
    @api.model
    def create(self, vals):
        company_id = self.env['res.company'].browse(vals.get('company_id'))
        department_id = self.env['hr.department'].browse(vals.get('department_id'))
    
        sequence_id = self.env['ir.sequence'].search([('code', '=', 'employee.sequence')], limit=1)
        if not sequence_id:
            sequence_id = self.env['ir.sequence'].create({
                'name': 'Employee Sequence',
                'code': 'employee.sequence',
                'padding': 3,
            })
    
        vals['user_code_autogenerate'] = sequence_id.next_by_id()
    
        user_code = ''
    
        company_code = getattr(company_id, 'company_code', None)
        if company_code:
            user_code += str(company_code)
    
        if vals.get('user_code_autogenerate'):
            user_code += vals['user_code_autogenerate']
    
        department_code = getattr(department_id, 'dep_code', None)
        if department_code:
            user_code += str(department_code)
    
        vals['user_code'] = user_code
    
        res = super(HrEmployee, self).create(vals)
        return res
  
  
  
  
  
    def write(self, vals):
        for rec in self:
            if 'user_code_autogenerate' in vals:
                user_code_autogenerate = vals['user_code_autogenerate']
            else:
                user_code_autogenerate = rec.user_code_autogenerate
    
            company_id = rec.company_id if 'company_id' not in vals else self.env['res.company'].browse(vals.get('company_id'))
            department_id = rec.department_id if 'department_id' not in vals else self.env['hr.department'].browse(vals.get('department_id'))
    
            user_code = ''
            
            company_code = getattr(company_id, 'company_code', None)
            if company_code:
                user_code += str(company_code)
    
            department_code = getattr(department_id, 'dep_code', None)
            if department_code:
                user_code += str(department_code)
    
            user_code += str(user_code_autogenerate)
    
            vals['user_code'] = user_code
    
        return super(HrEmployee, self).write(vals)
    
    
    