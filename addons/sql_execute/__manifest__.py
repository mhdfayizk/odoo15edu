# -*- coding: utf-8 -*-


{
	'name': "SQL Queries Execute",
	'version': "15.0.0.1",
	'category': "Tools",
    'license':'OPL-1',
	'summary': "Module for sql query execution",
	'description': """
		
			Module for sql query execution. 
		
			

	""",
	'author': "Christy",
    'depends': ['base'],
	'data': [
	        'security/ir.model.access.csv',
			'views/sql_execute_view.xml',
			],
	'demo': [],
	'installable': True,
	'auto_install': False,
	'application': True,
	
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
