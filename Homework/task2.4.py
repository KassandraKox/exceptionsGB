# Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку. 
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя.

def get_required_message():
    print('Введите текст: ')
    while True:
        try:
            text = input()
            if text in ('', ' '):
                print("Пустые строки вводить нельзя!")
                #break
            else:
                print('text принят')
        except ValueError:
            print("Пустые строки вводить нельзя!")
            break
get_required_message()

