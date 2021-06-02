class scheme:
    def id(self):
        self.sid = int(input("Enter scheme ID:"))
        return self.sid
    def name(self):
        self.snm = input("Enter scheme Name:")
        return self.snm
    def out(self):
        self.sor = input("Enter scheme Outgoing Rate:")
        return self.sor
    def msg(self):
        self.smsgc = input("Enter scheme message charge:")
        return self.smsgc
class customer(scheme):
    def cid(self):
        self.cuid = int(input("Enter Customer ID:"))
        return self.cuid
    def cname(self):
        self.cnm = input("Enter Customer Name:")
        return self.cnm
    def cph(self):
        self.cpn = int(input("Enter Customer Phone number:"))
        return self.cpn
    def display(self):
        print("Scheme ID is:", self.sid)
        print("Scheme name is:", self.snm)
        print("Scheme Outgoing Rate is:", self.sor)
        print("Scheme message charge is:", self.smsgc)
        print("Customer ID is:", self.cuid)
        print("Customer name is:", self.cnm)
        print("Phone number is:", self.cpn)


s = scheme()
c= customer()
c.display()
