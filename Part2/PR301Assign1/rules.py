class Rules(metaclass=ABCMeta):
	def __init__(self):
		self.rules = { 'id_rule' : "^[A-Z][0-9]{3}$"
					   'gender_rule' : "^(M|F)$"
					   'age_rule' : "^[0-9]{2}$"
					   'sales_rule' : "^[0-9]{3}$"
					   'bmi_rule' : "^(Normal|Overweight|Obesity|Underweight)$"
					   'salary_rule' : "^[0-9]{2,3}$"
					   'birthday_rule' : "^[1-31]-[1-12]-[0-9]{4}$"
					}
		
	def get_attr(self, arg):
		return self.arg