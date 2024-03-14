# -*- coding: utf-8 -*-


{
	'name': "Sky Secretary Odoo Customisations",
	'version': "15.0.0.2",
	'category': "Human Resources/Employees",
    'license':'OPL-1',
	'summary': "This Module provides customisations for different modules",
	'description': """
		
			This Module provides customisations for different modules. 
		
			

	""",
	'author': "Sky Secretary",
	"website" : "https://skysecretary.com/",
    'depends': ['hr'],
	'data': [
		    'data/employee_code_sequence.xml',
			'views/hr_employee_view.xml',
			'views/res_company_view.xml',
			'views/hr_department_view.xml',
			],
	'demo': [],
	'installable': True,
	'auto_install': False,
	'application': True,
	
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
