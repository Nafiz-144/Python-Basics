from Question import Question

question_prompts = [
    "what color are apples?\n(a)red\n(b)purple\n(c)blzck\n\n",
    "what color are Bananas?\n(a)teal\n(b)megenta\n(c)Yellow\n\n",
    "what color are Strawberries?\n(a)Yellow\n(b)red\n(c)black\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got"+str(score)+"/"+str(len(questions)) + "correct")


run_test(questions)
