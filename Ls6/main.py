import random


def read_file(file_name):
    with open(file_name, 'rt') as file_contents:
        file_content = file_contents.readlines()
        print(f"Всего игр сыграно:{len(file_content)}")
        max_point = 0
        for player in file_content:
            data = player.rstrip().split('  ')
            if max_point <= int(data[1]):
                max_point = int(data[1])
        print(f"Максимальный рекорд: {max_point}")

def add_to_file(file_name):
    with open(file_name, 'a') as file_contents:
        file_contents.write(f"{name_player}  {points}\n")

if __name__ == '__main__':

    print("Введите Ваше имя")
    name_player = input()
    points = 0
    with open("words.txt", 'r') as f:
        for line in f:
            true_word = line.rstrip()
            str_var = list(true_word)
            random.shuffle(str_var)
            code_word = ''.join(str_var)
            print(f"Угадайте слово: {code_word}")
            answear = input()
            if answear == true_word:
                print("Верно! Вы получаете 10 очков.")
                points += 10
            else:
                print(f"Неверно! Верный ответ – {true_word}.")

    add_to_file('top.txt')
    read_file('top.txt')

