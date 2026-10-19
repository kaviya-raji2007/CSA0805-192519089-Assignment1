
def read_number(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError:
            print("Invalid number. Try again.")

farmer_id = input("Enter farmer ID: ").strip()

litres = read_number("Enter litres: ")
fat = read_number("Enter fat percentage: ")
snf = read_number("Enter SNF percentage: ")

if not farmer_id:
    print("Invalid farmer ID")
elif litres <= 0:
    print("Quantity must be positive")
elif not 2.0 <= fat <= 7.0:
    print("Fat must be between 2.0 and 7.0")
else:
    print(f"{'Farmer ID':<15}{'Litres':>10}{'Fat':>10}{'SNF':>10}")
    print(f"{farmer_id:<15}{litres:>10.2f}{fat:>10.2f}{snf:>10.2f}")
