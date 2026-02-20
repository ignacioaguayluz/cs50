months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:

                print(f"{year}-{month:02}-{day:02}")
                break

        elif "," in date:
            month_name, day_str, year_str = date.split(" ")

            if month_name in months:
                month = months.index(month_name) + 1

                day = int(day_str.replace(",", ""))
                year = int(year_str)

                if 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
        else:
            continue
    except ValueError:
        pass


