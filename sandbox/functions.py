
def summa(a, b):
    return a + b

result = summa(4, 3)

def save(text):
    f = open("demo.txt", "a")
    f.write(text + "\n")
    f.close()

save(str(summa(4, 3)))
