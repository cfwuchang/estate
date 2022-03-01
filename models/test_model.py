from odoo import models,fields

class EstateProperty(models.Model):
    _name = "test.model"
    _description='房地产广告'
    
    name = fields.Char(string='名称')
    description = fields.Text(string='类型')
    postcode = fields.Text(string='编码')
    date_availability = fields.Date(string='截至日期')
    expected_price = fields.Float(string='预期价格')
    selling_price = fields.Float(string='卖价')
    bedrooms = fields.Integer(string='房间数')
    living_area = fields.Integer(string='房间面积')
    facades = fields.Integer(string='墙壁数')
    garage = fields.Boolean(string='车库')
    garden = fields.Boolean(string='院子')
    garden_area = fields.Integer(string='绿化区')
    garden_orientation = fields.Selection([('North','北'),
    ("South","南"),("East","东"),("West","西")],string='面向花园')

    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())