#-*- coding: utf-8 -*-


from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = "res.company"

    company_code = fields.Char(string="Company Code")
    

    

    
    
    
    
    
