class employee:
    # special methods/ magic methods / dunder methods
    def __init__(self):
        print("Constructor initiated")
        print(id(self))
        self.id = 123
        self.dept = "XYZ"
        self.salary = 50000
        print("Constructor called")
        

    def travel(self, destination):
        print(f"the employee is traveling to {destination}")

    def print_some(self):
            return "Welcome coder!!!"
sam = employee()
print(id(sam))
# print(sam.salary)
# sam.travel("Kerala")