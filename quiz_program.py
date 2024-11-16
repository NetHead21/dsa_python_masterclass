# Quiz Data: the questions and their corresponding answer
quiz_data: dict[int, tuple[str, str]] = {
    1: ("What is the capital of France?", "Paris"),
    2: ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    3: ("What is the largest planet in our solar system?", "Jupiter"),
    4: ("What year did World War II end?", "1945"),
    5: ("What is the powerhouse of the cell?", "Mitochondria"),
    6: ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    7: ("What is the chemical symbol for gold?", "Au"),
    8: ("What is the boiling point of water in Celsius?", "100"),
    9: ("What is the currency of Japan?", "Yen"),
    10: ("Who is known as the 'Father of Computer Science'?", "Alan Turing"),
}


def check_answer(correct_answer: str, user_answer: str) -> bool:
    return correct_answer.lower() == user_answer.lower()


def get_score(correct_answers: tuple[str, ...], user_answers: list[str]) -> int:
    return sum(
        1
        for correct, user in zip(correct_answers, user_answers)
        if check_answer(correct, user)
    )


def get_user_answer() -> list[str]:
    return [
        input(f"{idx}: {data[0]}\nEnter your answer: ")
        for idx, data in quiz_data.items()
    ]


def main() -> None:
    total_questions = len(quiz_data)
    correct_answers = tuple(value[1] for value in quiz_data.values())
    user_answers = get_user_answer()
    score = get_score(correct_answers, user_answers)
    percentage = (score / total_questions) * 100

    # Display Results
    print(f"You got {score} out of {total_questions} correct.")
    print(f"Your grade: {percentage:.2f}")


if __name__ == "__main__":
    main()
