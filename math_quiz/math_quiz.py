import random


def random_integer_generator(min_int, biggest_int):
    """
    Generates a random integer number within the range of smallest_int and biggest_int and returns the generated number.
    Including smallest_int but excluding bigger_int

    min_int: Minimal integer value for random integer generation
    type min_int: int
    biggest_int: biggest integer number for the int generation excluding biggest_int
    type biggest_int: int
    """
    try:
        random_num = random.randint(min_int, biggest_int)
        return random_num
    except TypeError:
        print( "One or both of your entered number/s is/are not integer/s")


def sign_generator():

    # Randomly selects and returns one of the array elements (Operator)

    return random.choice(['+', '-', '*'])


def math_operation(number1, number2, operator):

    """
    performs some math operations such as addition, subtraction, and multiplication

    number1: Given first number
    type number1: float, int
    number2: Given second number
    type number2: float, int
    operator: mathematical operator
    type operator: string
    problem: Mathematical problem
    type problem: string
    """

    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problem, answer


def math_quiz():
    """
    Small math quiz program which generates randomly two numbers with random
    operation and tests the user. When the user answers correctly his score increases otherwise the game
    finishes and shows the score of the user

    score: Number of correctly answered questions
    type score: int
    total_questions: Number of total questions
    type total_questions:
    """

    score = 0
    total_questions = 3  #3.14159265359
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = random_integer_generator(1, 10)
        number2 = random_integer_generator(1, 5)
        operator = sign_generator()
        problem, answer = math_operation(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
        print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
