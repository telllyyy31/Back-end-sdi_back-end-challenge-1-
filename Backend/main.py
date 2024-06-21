class CarRental:
    def __init__(self):
        self.car_options = [
            {'size': 'Small', 'capacity': 5, 'cost': 5000},
            {'size': 'Medium', 'capacity': 10, 'cost': 8000},
            {'size': 'Large', 'capacity': 15, 'cost': 12000}
        ]

    def find_min_cost(self, seats):
        # This function will find the minimum cost for the given number of seats
        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]
            if n <= 0:
                return 0, []
            min_cost = float('inf')
            best_combination = []
            for option in self.car_options:
                cost, combination = dp(n - option['capacity'])
                cost += option['cost']
                if cost < min_cost:
                    min_cost = cost
                    best_combination = combination + [option]
            memo[n] = (min_cost, best_combination)
            return memo[n]

        return dp(seats)

    def print_result(self, seats):
        min_cost, combination = self.find_min_cost(seats)
        print("Car combination:")
        for car in combination:
            print(f"{car['size']} ({car['capacity']} seats) - {car['cost']} PHP")
        print(f"Total = {min_cost} PHP")

if __name__ == "__main__":
    seats = int(input("Please input number (seat): "))
    car_rental = CarRental()
    car_rental.print_result(seats)
