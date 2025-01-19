function book(consultants, hour, duration, criteria) {
    //篩選符合時間條件的顧問
    const availableConsultants = consultants.filter(consultant => {
        const bookings = consultant.bookings || [];
        return bookings.every(([start, end]) => {
            const newStart = hour;
            const newEnd = hour + duration;
            return newEnd <= start || newStart >= end; // 時間不重疊
        });
    });

    //根據標準（price和rate）排序
    if (criteria === "price") {
        availableConsultants.sort((a, b) => a.price - b.price);
    } else if (criteria === "rate") {
        availableConsultants.sort((a, b) => b.rate - a.rate);
    }

    //判斷結果
    if (availableConsultants.length > 0) {
        const selected = availableConsultants[0];
        console.log(selected.name);

        if (!selected.bookings) {
            selected.bookings = [];
        }
        selected.bookings.push([hour, hour + duration]);
    } else {
        console.log("No Service");
    }
}

const consultants = [
    { name: "John", rate: 4.5, price: 1000, bookings: [] },
    { name: "Bob", rate: 3, price: 1200, bookings: [] },
    { name: "Jenny", rate: 3.8, price: 800, bookings: [] },
];

book(consultants, 15, 1, "price"); // 輸出 Jenny
book(consultants, 11, 2, "price"); // 輸出 Jenny
book(consultants, 10, 2, "price"); // 輸出 John
book(consultants, 20, 2, "rate"); // 輸出 John
book(consultants, 11, 1, "rate"); // 輸出 Bob
book(consultants, 11, 2, "rate"); // 輸出 No Service
book(consultants, 14, 3, "price"); // 輸出 John