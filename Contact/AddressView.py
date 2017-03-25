import Address


def show_menu():
    print("-" * 10, "주소록", "-" * 10)
    print("1. 입력")
    print("2. 출력")
    print("3. 삭제")
    print("4. 종료")

    try:
        selected_num = input("번호를 선택 하세요 : ")
        return selected_num
    except:
        return show_menu()


def save_person(addr):
    name = input("이름 : ")
    phone_number = input("전화번호 : ")
    address = input("주소 : ")

    addr.save(name, phone_number, address)


def print_address(address):
    print("\n" * 2)
    for person in address.findAll():
        print("이름 : ", person.name)
        print("전화번호 : ", person.phone_number)
        print("주소 : ", person.address)
        print("-" * 60)
    print("\n")


def main():
    address = Address.Address()
    while True:
        selected_num = show_menu()

        if selected_num == "4":
            break
        elif selected_num == "1":
            save_person(address)
        elif selected_num == "2":
            print_address(address)


if __name__ == "__main__":
    main()
