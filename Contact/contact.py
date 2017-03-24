import os


def clear():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    elif os.name in ('linux', 'osx', 'posix'):
        os.system("clear")
    else:
        print("\n" * 120)


class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name : ", self.name)
        print("Phone-Number : ", self.phone_number)
        print("E-mail : ", self.e_mail)
        print("Address : ", self.addr)
        print("-" * 60)


def set_contact():
    name = input("Name : ")
    phone_number = input("Phone Number : ")
    e_mail = input("E-Mail : ")
    addr = input("Address : ")

    contact = Contact(name, phone_number, e_mail, addr)
    return contact


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]


def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + "\n")
        f.write(contact.phone_number + "\n")
        f.write(contact.e_mail + "\n")
        f.write(contact.addr + "\n")
    f.close()


def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = int(len(lines) / 4)

    for i in range(num):
        name = lines[4 * i].rstrip("\n")
        phone = lines[4 * i + 1].rstrip("\n")
        email = lines[4 * i + 2].rstrip("\n")
        addr = lines[4 * i + 3].rstrip("\n")

        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    
    f.close()




'''
   int()를 할 수 없는경우 버그가 남
'''


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연학처 삭제")
    print("4. 종     료")
    menu = input("메뉴선택 : ")
    return int(menu)


def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 4:
            store_contact(contact_list)
            break
        elif menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("삭제 할 이름은 : ")
            delete_contact(contact_list, name)
        else:
            pass


if __name__ == "__main__":
    run()
