#-*- coding: utf-8 -*-


from odoo import api, fields, models

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    user_code = fields.Char(string="Employee ID")
    user_code_autogenerate = fields.Char(string="Code Sequence") 
    
    
        
    
    # @api.model
    # def create(self, vals):
    #     company_id = self.env['res.company'].browse(vals.get('company_id'))
    #
    #     sequence_id = self.env['ir.sequence'].search([('code', '=', 'employee.sequence')], limit=1)
    #     if not sequence_id:
    #         sequence_id = self.env['ir.sequence'].create({
    #             'name': 'Employee Sequence',
    #             'code': 'employee.sequence',
    #             'padding': 3,
    #         })
    #
    #     vals['user_code_autogenerate'] = sequence_id.next_by_id()
    #
    #     user_code = ''
    #
    #     company_code = getattr(company_id, 'company_code', None)
    #     if company_code:
    #         user_code += str(company_code)
    #
    #
    #     if vals.get('user_code_autogenerate'):
    #         user_code += vals['user_code_autogenerate']    
    #
    #     vals['user_code'] = user_code
    #
    #     res = super(HrEmployee, self).create(vals)
    #     return res
  
  
    @api.model
    def create(self, vals):
        company_id = self.env['res.company'].browse(vals.get('company_id'))
        sequence_code = 'employee.sequence.%s' % company_id.id
        sequence_id = self.env['ir.sequence'].search([('code', '=', sequence_code)], limit=1)

        if not sequence_id:
            sequence_id = self.env['ir.sequence'].create({
                'name': 'Employee Sequence for %s' % company_id.name,
                'code': sequence_code,
                'padding': 3,
            })

        vals['user_code_autogenerate'] = sequence_id.next_by_id()
        user_code = ''
        company_code = getattr(company_id, 'company_code', None)

        if company_code:
            user_code += str(company_code)

        if vals.get('user_code_autogenerate'):
            user_code += vals['user_code_autogenerate']

        vals['user_code'] = user_code

        res = super(HrEmployee, self).create(vals)
        return res
  
  
    # def write(self, vals):
    #     for rec in self:
    #         if 'user_code_autogenerate' in vals:
    #             user_code_autogenerate = vals['user_code_autogenerate']
    #         else:
    #             user_code_autogenerate = rec.user_code_autogenerate
    #
    #         company_id = rec.company_id if 'company_id' not in vals else self.env['res.company'].browse(vals.get('company_id'))
    #
    #
    #         user_code = ''
    #
    #         company_code = getattr(company_id, 'company_code', None)
    #         if company_code:
    #             user_code += str(company_code)
    #
    #
    #
    #         user_code += str(user_code_autogenerate)
    #
    #         vals['user_code'] = user_code
    #
    #     return super(HrEmployee, self).write(vals)
    
    
    