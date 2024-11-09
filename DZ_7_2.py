
def custom_write(file_name,strings):
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        number_bytes = file.tell()
        file.write(str(number_bytes) + '-'  + string + '\n')
    file.close()

    file = open(file_name, 'r', encoding='utf-8')
    counter_line = 0
    string_position = {}

    for line in file.read().splitlines():
        counter_line += 1
        key = (counter_line, int(line.split("-")[0]))
        value = line.split("-")[1]
        string_position[key] = value
    file.close()

    return string_position

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result =custom_write('text.txt', info)

    for elem in result.items():
        print(elem)

