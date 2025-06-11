from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"


    ref = fields.Char(string="Reference")
    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone Number')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    age_type = fields.Selection([
        ('old', "Old"),
        ('kid', "Kid"),
    ], string="Age Type")