courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
     "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
     "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

durations = [14, 20, 12, 20]


def get_uniq_names(mentors):
    all_list = []
    for m in mentors:
        all_list += m
    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')[0]
        all_names_list.append(name)
    unique_names = sorted(list(set(all_names_list)))
    return f'Уникальные имена преподавателей: {", ".join(unique_names)}'


def get_popular_names(mentors):
    all_list = []
    for m in mentors:
        all_list += m
    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')[0]
        all_names_list.append(name)
    unique_names = list(set(all_names_list))

    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])
    if not popular:
        return 'Empty list'

    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[0:3]
    to_print = ''
    for i in range(3):
        to_print += f'{top_3[i][0]}: {top_3[i][1]} раз(а), '

    populars_str = to_print.rstrip(', ')
    return populars_str


def get_courses_by_durations(courses, durations):
    courses_list = []
    for course, duration in zip(courses, durations):
        course_dict = {"title": course, "duration": duration}
        courses_list.append(course_dict)
    courses_list = sorted(courses_list, key=lambda x: x['duration'])
    result = ''
    for course in courses_list:
        result += f'{course["title"]} - {course["duration"]} месяцев\n'
    return result

uniq_names = get_uniq_names(mentors)
popular_names = get_popular_names(mentors)
courses_by_duration = get_courses_by_durations(courses, durations)
print(courses_by_duration)
