def get_color(num):
    # Define the grid numbers and corresponding colors
    grid_number = list(range(1, 37))
    grid_color = ['green', 'red', 'blue', 'orange', 'gray', 'green', 'green', 'gray', 'orange', 'blue', 'red', 'green',
                  'red', 'blue', 'orange', 'gray', 'green', 'red', 'red', 'green', 'gray', 'orange', 'blue', 'red',
                  'blue', 'orange', 'gray', 'green', 'red', 'blue', 'blue', 'red', 'green', 'gray', 'orange', 'blue']

    # Create a dictionary mapping grid numbers to colors
    grid = {grid_number[i]: grid_color[i] for i in range(36)}

    return grid.get(num)


def color_guessing(total_rounds):
    won_rounds = 0
    previous_victories = set()
    warnings = 0
    round_number = 1

    print("Welcome to the Grid Color Guessing Game!")

    while round_number <= total_rounds:
        user_input = input(f"Enter two grid numbers for Round {round_number}: ")

        # Check if the input contains exactly two numbers
        if not user_input.replace(" ", "").isdigit() or user_input.count(" ") != 1:
            print("Invalid input. Please enter two numbers separated by a space.")
            round_number += 1
            continue

        num1, num2 = map(int, user_input.split())

        # Validate input range
        if num1 < 1 or num1 > 36 or num2 < 1 or num2 > 36:
            print("Invalid numbers. Please enter numbers between 1 and 36.")
            round_number += 1
            continue

        # Check for repeated numbers
        if (num1, num2) in previous_victories or (num2, num1) in previous_victories:
            warnings += 1
            print(f"WARNING {warnings}: You already used these numbers!")
            if warnings >= 4:
                print("WARNING 4: END OF PROGRAM")
                return
        else:
            # Check if they have the same color
            color1 = get_color(num1)
            color2 = get_color(num2)

            if color1 == color2:
                print(f"{num1} and {num2} have the same color ({color1}) => Round {round_number}")
                previous_victories.add((num1, num2))
                won_rounds += 1
            else:
                print(f"{num1} and {num2} do not have the same color ({color1} vs {color2}) => Round {round_number}")

        round_number += 1  # Always increment round number

    # Final check
    if won_rounds >= 3:
        print("Congratulations! You won the game!")
    else:
        print("Game Over! You did not win enough rounds.")


# Run the game with 5 rounds
color_guessing(5)
