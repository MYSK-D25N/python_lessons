try:
	v0 = int(input("Начальная скорость (v0, м/с) = "))
	v = int(input("Конечная скорость (v, м/с) = "))
	t = int(input("Время (t, с) = "))
	if t == 0:
		print("Время не может быть равно нулю.")
		raise ValueError("Время не может быть равно нулю.")
except ValueError:
	print("Ошибка ввода данных.")
else:
	def addDistance(acceleration):
		def wrapper():
			print("Ускорение (a) = ", acceleration())
			S = v0 * t + (acceleration() * t**2) / 2
			print("Расстояние (S) = ",S)
		return wrapper

	@addDistance
	def acceleration():
		a = (v - v0) / t
		return a

	print(acceleration())
