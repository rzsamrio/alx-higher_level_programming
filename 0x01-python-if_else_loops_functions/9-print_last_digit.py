def print_last_digit(number):
	if number < 0:
		number = abs(number)
		last = number % 10
		print(f"{last}", end="")
		return last
	else:
		last = number % 10
		print(f"{last}", end="")
