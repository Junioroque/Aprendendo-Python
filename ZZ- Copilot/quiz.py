#Crie uma função que rode um quiz pergunta e resposta.
"""
Crie uma lista de questões com 5 perguntas e 4 possíveis respostas.
Cada pergunta deve ter apenas uma resposta correta.
Cada resposta correta deve valer 1 ponto.
Esse quiz será de várias capitais do mundo.
"""
questions = [
    {
        "question": "Qual é a capital da França?",
        "options": ["a) Paris", "b) Londres", "c) Roma", "d) Berlim"],
        "answer": "a"
    },
    {
        "question": "Qual é a capital do Brasil?",
        "options": ["a) Rio de Janeiro", "b) São Paulo", "c) Brasília", "d) Salvador"],
        "answer": "c"
    },
    {
        "question": "Qual é a capital do Japão?",
        "options": ["a) Tóquio", "b) Kyoto", "c) Osaka", "d) Hiroshima"],
        "answer": "a"
    },
    {
        "question": "Qual é a capital da Austrália?",
        "options": ["a) Sydney", "b) Melbourne", "c) Canberra", "d) Brisbane"],
        "answer": "c"
    },
    {
        "question": "Qual é a capital do Canadá?",
        "options": ["a) Toronto", "b) Vancouver", "c) Ottawa", "d) Montreal"],
        "answer": "c"
    }
]

#Escreva uma função que recebe a questão e as exibe uma a uma para o usuário.
#Ela retorna a resposta do usuário e valida se a resposta está é valida ou se ela é um erro.

def show_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Digite a letra da resposta correta: ").lower()
    while answer not in ['a', 'b', 'c', 'd']:
        print("Resposta inválida. Tente novamente.")
        answer = input("Digite a letra da resposta correta: ").lower()
    return answer

#Escreva uma função que recebe a resposta do usuário e a compara com a resposa correta.

def check_answer(question, user_answer):
    return user_answer == question["answer"]

def main():
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Digite a letra da resposta correta: ").lower()
        if answer == q["answer"]:
            score += 1
    print(f"Você acertou {score} de {len(questions)} perguntas.")


if __name__ == "__main__":
    main()