import re

class SimpleCalculator:
	def __init__(self):
		self._history = []
		self._regex = re.compile(r"^\s*(\d+)\s*([\+\-\/\*])\s*(\d+)\s*$")

		self._operators = {
			"+": lambda a, b: a + b,
			"-": lambda a, b: a - b,
			"/": lambda a, b: a / b,
			"*": lambda a, b: a * b
		}

	def evaluate_expression(self, input_expression):
		match = self._regex.match(input_expression)
		if match is None:
			return "Error"
		
		op1, opr, op2 = match.groups()

		if opr == "/" and op2 == 0:
			return "Error"

		result = self._operators[opr](int(op1), int(op2))

		self._history.append((input_expression, result))

		return result

	def get_history(self):
		return self._history.copy()
