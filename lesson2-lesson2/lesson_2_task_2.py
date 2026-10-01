def is_year_leap(year: int) -> bool:
    """Возвращает True, если год високосный, иначе False."""
    return year % 4 == 0

user_input = input("Введите год: ")
year = int(user_input)

result = is_year_leap(year)

print(f"год {year}: {result}")
