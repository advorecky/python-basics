# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте
# работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real) - (self.imag * other.imag),
                             (self.imag * other.real) + (self.real * other.imag))

    def __str__(self):
        return f"{self.real + self.imag}"


complex_number01 = ComplexNumber(5, 3j)
complex_number02 = ComplexNumber(2, 6j)
print(complex_number01 + complex_number02)
print(complex_number01 * complex_number02)
