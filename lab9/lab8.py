clients = [
    {"id": 1, "name": "Иванов", "contact": "+78005553535"},
    {"id": 2, "name": "Смирнова", "contact": "+79876543210"}
]

rooms = [
    {"id": 101, "category": "Стандарт", "price": 3000, "status": "Свободен"},
    {"id": 102, "category": "Люкс", "price": 5000, "status": "Занят"}
]

bookings = [
    {"id": 1, "client_id": 1, "room_id": 101, "check_in": "2024-12-01", "check_out": "2024-12-05", "status": "Подтверждено"},
    {"id": 2, "client_id": 2, "room_id": 102, "check_in": "2024-12-03", "check_out": "2024-12-10", "status": "Подтверждено"}
]

services = [
    {"id": 1, "name": "Завтрак", "price": 500},
    {"id": 2, "name": "Стирка одежды", "price": 1500}
]

ordered_services = [
    {"id": 1, "booking_id": 1, "service_id": 1, "quantity": 1},
    {"id": 2, "booking_id": 2, "service_id": 2, "quantity": 2}
]

def add_client():
    client_id = int(input("Введите ID клиента: "))
    name = input("Введите имя клиента: ")
    contact = input("Введите телефон клиента: ")
    clients.append({"id": client_id, "name": name, "contact": contact})
    print("Клиент добавлен.")

def add_room():
    room_id = int(input("Введите ID номера: "))
    category = input("Введите категорию номера: ")
    price = float(input("Введите цену за номер: "))
    status = input("Введите статус номера (Свободен/Занят): ")
    rooms.append({"id": room_id, "category": category, "price": price, "status": status})
    print("Номер добавлен.")

def add_booking():
    booking_id = int(input("Введите ID бронирования: "))
    client_id = int(input("Введите ID клиента: "))
    room_id = int(input("Введите ID номера: "))
    check_in = input("Введите дату заезда (ГГГГ-ММ-ДД): ")
    check_out = input("Введите дату выезда (ГГГГ-ММ-ДД): ")
    status = input("Введите статус бронирования (Подтверждено/Ожидает): ")
    bookings.append({"id": booking_id, "client_id": client_id, "room_id": room_id, "check_in": check_in, "check_out": check_out, "status": status})
    print("Бронирование добавлено.")

def add_service():
    service_id = int(input("Введите ID услуги: "))
    name = input("Введите название услуги: ")
    price = float(input("Введите цену услуги: "))
    services.append({"id": service_id, "name": name, "price": price})
    print("Услуга добавлена.")

def add_ordered_service():
    order_id = int(input("Введите ID заказа: "))
    booking_id = int(input("Введите ID бронирования: "))
    service_id = int(input("Введите ID услуги: "))
    quantity = int(input("Введите количество: "))
    ordered_services.append({"id": order_id, "booking_id": booking_id, "service_id": service_id, "quantity": quantity})
    print("Заказ услуги добавлен.")

def delete_field(table, field_id):
    for field in table:
        if field["id"] == field_id:
            table.remove(field)
            print(f"Запись с ID {field_id} удалена.")
            return
    print(f"Запись с ID {field_id} не найдена.")

def update_field(table, field_id):
    for field in table:
        if field["id"] == field_id:
            print(f"Текущая запись: {field}")
            for key in field.keys():
                if key != "id":
                    new_value = input(f"Введите новое значение для {key} (оставьте пустым для пропуска): ")
                    if new_value:
                        field[key] = int(new_value) if isinstance(field[key], int) else float(new_value) if isinstance(field[key], float) else new_value
            print("Запись обновлена.")
            return
    print(f"Запись с ID {field_id} не найдена.")

def generate_report():
    print("\nОтчет по клиентам:")
    for client in clients:
        print(f"Клиент: {client['name']} ({client['contact']})")
        client_bookings = [b for b in bookings if b['client_id'] == client['id']]
        for booking in client_bookings:
            room = next(r for r in rooms if r['id'] == booking['room_id'])
            print(f"  - Номер: {room['category']} (ID: {room['id']}, статус: {booking['status']})")
            client_services = [o for o in ordered_services if o['booking_id'] == booking['id']]
            for order in client_services:
                service = next(s for s in services if s['id'] == order['service_id'])
                print(f"  - Услуга: {service['name']} x {order['quantity']}")
    input("\nНажмите любую кнопку для продолжения.")

def view_clients():
    print("\nКлиенты:")
    for client in clients:
        print(client)
    input("\nНажмите любую кнопку для продолжения.")

def view_rooms():
    print("\nНомера:")
    for room in rooms:
        print(room)
    input("\nНажмите любую кнопку для продолжения.")

def view_bookings():
    print("\nБронирования:")
    for booking in bookings:
        print(booking)
    input("\nНажмите любую кнопку для продолжения.")

def view_services():
    print("\nУслуги:")
    for service in services:
        print(service)
    input("\nНажмите любую кнопку для продолжения.")

def view_ordered_services():
    print("\nЗаказанные услуги:")
    for order in ordered_services:
        print(order)
    input("\nНажмите любую кнопку для продолжения.")

def validate_data():
    # Проверка клиентов
    client_ids = {client["id"] for client in clients}
    for booking in bookings:
        if booking["client_id"] not in client_ids:
            return False, f"Некорректный клиент в бронировании {booking['id']}"

    # Проверка номеров
    room_ids = {room["id"] for room in rooms}
    for booking in bookings:
        if booking["room_id"] not in room_ids:
            return False, f"Некорректный номер в бронировании {booking['id']}"

    # Проверка услуг
    service_ids = {service["id"] for service in services}
    for order in ordered_services:
        if order["service_id"] not in service_ids:
            return False, f"Некорректная услуга в заказе {order['id']}"

    return True, "Данные корректны"

def main():
    while True:
        print("\nМеню:")
        print("1. Проверить данные")
        print("2. Добавить клиента")
        print("3. Добавить номер")
        print("4. Добавить бронирование")
        print("5. Добавить услугу")
        print("6. Добавить заказ услуги")
        print("7. Удалить запись")
        print("8. Изменить запись")
        print("9. Просмотреть клиентов")
        print("10. Просмотреть номера")
        print("11. Просмотреть бронирования")
        print("12. Просмотреть услуги")
        print("13. Просмотреть заказанные услуги")
        print("14. Сформировать отчет")
        print("15. Выйти")

        choice = input("\nВведите номер операции: ")
        if choice == "1":
            is_valid, message = validate_data()
            print(message)
        elif choice == "2":
            view_clients()
            add_client()
        elif choice == "3":
            view_rooms()
            add_room()
        elif choice == "4":
            view_bookings()
            add_booking()
        elif choice == "5":
            view_services()
            add_service()
        elif choice == "6":
            view_ordered_services()
            add_ordered_service()
        elif choice == "7":
            table_choice = input("Выберите таблицу (clients/rooms/bookings/services/ordered_services): ")
            field_id = int(input("Введите ID записи для удаления: "))
            if table_choice == "clients":
                delete_field(clients, field_id)
            elif table_choice == "rooms":
                delete_field(rooms, field_id)
            elif table_choice == "bookings":
                delete_field(bookings, field_id)
            elif table_choice == "services":
                delete_field(services, field_id)
            elif table_choice == "ordered_services":
                delete_field(ordered_services, field_id)
            else:
                print("Нет такой таблицы.")
        elif choice == "8":
            table_choice = input("Выберите таблицу (clients/rooms/bookings/services/ordered_services): ")
            field_id = int(input("Введите ID записи для изменения: "))
            if table_choice == "clients":
                update_field(clients, field_id)
            elif table_choice == "rooms":
                update_field(rooms, field_id)
            elif table_choice == "bookings":
                update_field(bookings, field_id)
            elif table_choice == "services":
                update_field(services, field_id)
            elif table_choice == "ordered_services":
                update_field(ordered_services, field_id)
            else:
                print("Нет такой таблицы.")
        elif choice == "9":
            view_clients()
        elif choice == "10":
            view_rooms()
        elif choice == "11":
            view_bookings()
        elif choice == "12":
            view_services()
        elif choice == "13":
            view_ordered_services()
        elif choice == "14":
            generate_report()
        elif choice == "15":
            print("Выход из программы")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()