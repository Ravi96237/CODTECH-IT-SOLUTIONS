# Datasets from Open Trivia DB(https://opentdb.com)
import json
import os
import random

def load_json(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data

def organize_questions(json_data):
    organized_questions = []
    for question_data in json_data['results']:
        options = question_data['incorrect_answers'] + [question_data['correct_answer']]
        random.shuffle(options)

        organized_question = {
            'question': question_data['question'],
            'options': options,
            'answer': question_data['correct_answer']
        }

        organized_questions.append(organized_question)

    return organized_questions

def get_organized_data():
    quiz_db_folder_path = 'quizdb/'

    '''
    {
        "CATEGORY A": [
            {
            "question": "Q1",
            "options": [
                "A",
                "B",
                "C",
                "D"
            ],
            "answer": "A"
            }
        ]
    }
    '''
    organized_data = {}

    for file_name in os.listdir(quiz_db_folder_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(quiz_db_folder_path, file_name)
            json_data = load_json(file_path)

            category = json_data['results'][0]['category']
            organized_data[category] = organize_questions(json_data)
    
    return organized_data

def choose_random_question(organized_data):
    random_category = random.choice(list(organized_data.keys()))
    random_question = random.choice(organized_data[random_category])
    return random_question

def print_options(options):
    for i, option in enumerate(options, start=65):
        print(f"{chr(i)}. {option}")

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (A, B, C, D): ").upper()
        if user_choice in {'A', 'B', 'C', 'D', 'a', 'b', 'c', 'd'}:
            return user_choice
        else:
            print("Invalid input. Please enter A, B, C, or D.")

def main():
    print("Welcome to KBC!")
    qa_data = get_organized_data()

    num_questions = 10 # We can modify this to get the input from the user
    correct_answers = 0

    for _ in range(num_questions):
        random_question = choose_random_question(qa_data)

        print("\nQuestion:", random_question['question'])
        print_options(random_question['options'])

        user_choice = get_user_choice()

        correct_option = chr(random_question['options'].index(random_question['answer']) + 65)  # ASCII code for 'A'

        if user_choice == correct_option:
            correct_answers += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {correct_option}. {random_question['answer']}\n")

    print(f"\nQuiz completed! Your score: {correct_answers}/{num_questions}")

if __name__ == "__main__":
    main()
