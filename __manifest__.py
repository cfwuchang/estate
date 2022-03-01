{
    'name': "房地产广告",

    'summary': """
        real estate""",

    'description': """
        real estate
    """,

    'author': "Company",
    'website': "http://oa.xmfuqi.cn/#/pages/list/list",
    'sequence':10,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': '任务',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/test_model_views.xml",
    ],
    # only loaded in demonstration mode
	'application':True,
}