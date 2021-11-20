'''
ФИО,пол,группа,семейное положение(холост/женат/свободна/замужем),рост,физкульт.группа(общая/спорт/спец)
Данные в строке разделяются запятыми. Может быть пропущена информация о семейном положении.
'''


def basket_team_test(string):
    keys = ['fio', 'sex', 'group', 'rel', 'height', 'phiz']
    person = dict(zip(keys, string.split(',')))

    if not person.get('rel'):
        person['rel'] = 'пропуск'

    if (person.get('sex') == 'муж' and int(person.get('height')) >= 180) or \
            (person.get('sex') == 'жен' and int(person.get('height')) >= 175):
        if person.get('phiz') in ['спорт', 'общая']:
            return f'{person.get("fio")},{person.get("height")},{person.get("rel")}'

    return f'{person.get("fio")},не подходит,{person.get("rel")}'


if __name__ == '__main__':
    #print(basket_team_test(input()))
    assert basket_team_test("Магомедова А.М.,жен,ПС-32,,175,спорт") == 'Магомедова А.М.,175,пропуск'
    assert basket_team_test("Иванов И.Н.,муж,ПС-21,женат,187,общая") == 'Иванов И.Н.,187,женат'
