class employee:
    def parentm(self):
        name="Harvi"
        designation="manager"
        print("name:",name," designation:",designation)
class salaryinfo(employee):
    def childm(self):
        salary=100
        print("salary:",salary)

c = salaryinfo()
c.childm()
c.parentm()