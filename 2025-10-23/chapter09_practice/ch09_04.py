class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, amount):
        self.salary += amount
        print(f"{self.name}의 연봉이 {self.salary}으로 증가되었습니다.")

Kim = Employee("Kim", 5000)
lee = Employee("lee", 6000)

print(f"{Kim.name}의 연봉은 {Kim.salary}입니다.")
print(f"{lee.name}의 연봉은 {lee.salary}입니다.")

Kim.raise_salary(2000)
lee.raise_salary(2000)