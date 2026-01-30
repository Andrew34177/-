class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def show_info(self):
        print(f"Сотрудник: {self.name}, Должность: {self.position}")
if __name__ == "__main__":
    emp = Employee("Андрей", "Разработчик")
    emp.show_info()