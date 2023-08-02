DATABASE = {
    'Сергей': 'Павлодар',
    'Айбек': 'Атырау',
    'Дамир': 'Астана',
    'Рустем': 'Алматы',
    'Максим': 'Кокшетау',
    'Амир': 'Алматы',
    'Азат': 'Уральск',
    'Руслан': 'Астана'
}

def process_tomiris(query):
    if query =='сколько у меня друзей?':
        count = len(DATABASE)
        return 'У вас ' + str(count) + ' друзей'
    elif query == 'кто все мои друзья?':
        counter = ''
        for i in DATABASE:
            counter = counter +str(i) + ' '
        return 'Твои друзья ' +str(counter)
    elif query == 'где все мои друзья?':
        counter = ''
        for i in DATABASE.values():
            counter = counter +str(i) + ' '
        return 'Твои друзья в городах: ' +str(counter)
    else:
        return 'Неизвестный запрос'

print(process_tomiris('Какая сейчас погода?'))
print(process_tomiris('где все мои друзья?'))
print(process_tomiris('кто все мои друзья?'))
print(process_tomiris('сколько у меня друзей?'))