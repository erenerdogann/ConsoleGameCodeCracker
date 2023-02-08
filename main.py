import random

DIGITS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
TRIES = 10
CODE_LENGHT = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGHT):
        digit = random.choice(DIGITS)
        code.append(digit)

    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGHT:
            print(f"You Must Guess {CODE_LENGHT} Colors.")
            continue

        for digit in guess:
            if digit not in DIGITS:
                print(f"Invalid Digit: {digit}. Try Again!")
                break

        else:
            break

    return guess

def check_code(guess, real_code):
    digit_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for digit in real_code:
        if digit not in digit_counts:
            digit_counts[digit] = 0
        digit_counts[digit] += 1

    for guess_digit, real_digit in zip(guess, real_code):
        if guess_digit == real_digit:
            correct_pos += 1
            digit_counts[guess_digit] -= 1

    for guess_digit, real_digit in zip(guess, real_code):
        if guess_digit in digit_counts and digit_counts[guess_digit] > 0:
            incorrect_pos += 1
            digit_counts[guess_digit] -= 1

    return correct_pos, incorrect_pos

def game():
    print("~ Code Cracker ~")
    print(f"You have {TRIES} tries to guess the code...")
    print("Code is consist of digits and they need to be entered SPACE SEPARATED!")

    code = generate_code()
    for attemps in range(1, TRIES+1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGHT:
            print(f"You Guessed The Code in {attemps} attemps!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print("You Ran Out of Tries, The Code Was: ", *code)

if __name__ == "__main__":
    game()