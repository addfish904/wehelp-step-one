def book(consultants, hour, duration, criteria):
    available_consultants = []
    for consultant in consultants:
        bookings = consultant.get("bookings", [])
        is_available = all(
            (hour + duration <= start or hour >= end)
            for start, end in bookings
        )
        if is_available:
            available_consultants.append(consultant)

    if criteria == "price":
        available_consultants.sort(key=lambda c: c["price"])
    elif criteria == "rate":
        available_consultants.sort(key=lambda c: c["rate"], reverse=True)

    if available_consultants:
        selected = available_consultants[0]
        print(selected["name"])
        if "bookings" not in selected:
            selected["bookings"] = []
        selected["bookings"].append((hour, hour + duration))
    else:
        print("No Service")

consultants = [
    {"name": "John", "rate": 4.5, "price": 1000, "bookings": []},
    {"name": "Bob", "rate": 3, "price": 1200, "bookings": []},
    {"name": "Jenny", "rate": 3.8, "price": 800, "bookings": []},
]

book(consultants, 15, 1, "price")  # 輸出 Jenny
book(consultants, 11, 2, "price")  # 輸出 Jenny
book(consultants, 10, 2, "price")  # 輸出 John
book(consultants, 20, 2, "rate")  # 輸出 John
book(consultants, 11, 1, "rate")  # 輸出 Bob
book(consultants, 11, 2, "rate")  # 輸出 No Service
book(consultants, 14, 3, "price")  # 輸出 John
