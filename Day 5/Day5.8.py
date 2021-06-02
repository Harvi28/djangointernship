class publisher:
    def title(self):
        name = "lost girl"
        return name

class book(publisher):
    def page(self):
        number = 230
        return number
class tape(publisher):
    def time(self):
        time = 200
        return time
pub = publisher()
b = book()
t = tape()
print("Name of the book is:",b.title())
print("Pages of the book are:",b.page())
print("Timing for playing:",t.time())