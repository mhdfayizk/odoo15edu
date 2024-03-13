#-*- coding: utf-8 -*-


from odoo import api, fields, models

class HrDepartment(models.Model):
    _inherit = "hr.department"

    dep_code = fields.Char(string="Department Code")
     
    
    
        
        
    


    
    
    