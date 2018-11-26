import sqlite3

conn = sqlite3.connect('laundry.db')
curs = conn.cursor()

towel=0
name=input()
enr_no=0
#name1, enr_no1=str, str
#cloth, cloth1 = str, str
#c=int
#n=int
#tot=int


def retStr(x):
    return str(x)

def insertdry(name, enr_no, cloth):
    curs.execute("INSERT INTO dryclean_data(name, enrollment_no, clothes) VALUES(?,?,?)", (tuple(list(map(retStr, [name, enr_no, cloth ])))))
    
def deldry():
    curs.execute("DELETE FROM laundary_data WHERE enrollment_no =?", (enr_no))

def insertlaundry(name, room_no, enr_no, noc, bedsheet, shirt, tshirt, towel, lower, shorts, jackets, sweatshirts, curtains, jeans, pillow_cover, kurta):
    curs.execute("INSERT INTO laundary_data(name, room_no, enrollment_no, no_of_clothes, shirt, tshirt, jeans, lowers, jackets, sweetshirts, shorts, kurta, curtains, bedsheets, pillow_covers) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(tuple(list(map(retStr, [name, room_no, enr_no, noc,shirt, tshirt, jeans, lower, jackets, sweatshirts, shorts, kurta, curtains,bedsheet, pillow_cover])))))
    
    
def dellaundry(enr_no):
    curs.execute("DELETE FROM laundary_data WHERE enrollment_no =?", (enr_no))
    conn.commit()
    

def ddi():
    print("Name: ")
    name = input()
    print("Enrollment number: ")
    enr_no = input()
    print("Cloth: ")
    cloth = input()
    insertdry(name, enr_no, cloth)
    print("Done.")
    conn.commit()
    conn.close()
    

def dpu():
    print("Name: ")
    name1 = input()
    print("Enrollment number: ")
    enr_no1 = input()
    print("Cloth: ")
    cloth1 = input()
    deldry(name1, enr_no1, cloth1)
    

def lpu():
    print("Enter Name: ")
    name1 = input()
    print("Enter Enrollment nummber: ")
    enr_no1 = input()
    dellaundry()
    print("Done.")

def ldi():
    print("Enter Name: ")
    name = input()
    print("Enter Room Number: ")
    room_no = int(input())
    print("Enter Enrollment Number: ")
    enr_no = input()
    print("Enter Number of clothes")
    noc=int(input())
    while(noc>10):
        print("More than 10 cloths are not allowed, Renter: ")
        noc=int(input())
    tot=noc+1
    while(tot!=noc and noc>0):
        print("Enter number of Shirt(s)")
        shirt = int(input())
        print("Enter number of T-shirt(s)")
        tshirt = int(input())
        print("Enter number of Jean(s)")
        jeans = int(input())
        print("Enter number of Lower(s)")
        lower = int(input())
        print("Enter number of Jacket(s)")
        jackets = int(input())
        print("Enter number of Sweatshirt(s)")
        sweatshirts = int(input())
        print("Enter number of Short(s)")
        shorts = int(input())
        print("Enter number of Kurta(s)")
        kurta = int(input())
        print("Enter number of Curtain(s)")
        curtains = int(input())
        print("Enter number of bedsheet(s)")
        bedsheet = int(input())
        print("Enter number of Pillow Cover(s)")
        pillow_cover = int(input())
        tot=bedsheet+shirt+tshirt+jeans+lower+jackets+sweatshirts+shorts+kurta+curtains+bedsheet+pillow_cover
    insertlaundry(name, room_no, enr_no, noc, bedsheet, shirt, tshirt, towel, lower, shorts, jackets, sweatshirts, curtains, jeans, pillow_cover, kurta)
    print("Done.")
    conn.commit()
    conn.close()
        
def menu():
    print("""1. Laundry Drop-In
2. Laundry Pick-Up
3. Dry Clean Drop-In
4. Dry Clean Pick-Up
5. Exit""")
    c=6
    while(c>5):
        c=int(input())
        if c==1: ldi()
        elif c==2: lpu()
        elif c==3: ddi()
        elif c==4: dpi()
        elif c==5: exit()
        else:
            print("Invalid! enter again: ")

    
menu()
