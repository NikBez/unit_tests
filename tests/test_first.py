import pytest

from first import get_uniq_names, get_popular_names, get_courses_by_durations


# -------------------------Testing get_uniq_names-------------------------
class TestUnique:
    def test_empty(self):
        mentors = []
        expect = 'Уникальные имена преподавателей: '
        result = get_uniq_names(mentors)
        assert expect == result

    def test_is_string(self):
        mentors = []
        result = get_uniq_names(mentors)
        assert isinstance(result, str)

    def test_only_names(self):
        mentors = [['Никита', 'Вася', 'Иван Петрович']]
        result = get_uniq_names(mentors)
        expect = 'Уникальные имена преподавателей: Вася, Иван, Никита'
        assert expect == result

    def test_not_str(self):
        mentors = [['Никита', 'Вася', 1]]
        with pytest.raises(AttributeError):
            get_uniq_names(mentors)

    def test_sorted(self):
        mentors = [['c', 'b', 'a']]
        result = get_uniq_names(mentors)
        expect = 'Уникальные имена преподавателей: a, b, c'
        assert expect == result


# -----------------------------Testing get_popular_names--------------------------------
class TestPopular:
    def test_empty_popular(self):
        mentors = []
        expect = 'Empty list'
        result = get_popular_names(mentors)
        assert expect == result

    def test_is_string_popular(self):
        mentors = [['Никита', 'Вася', 'Иван Петрович']]
        result = get_popular_names(mentors)
        assert isinstance(result, str)

    def test_not_str(self):
        mentors = [['Никита', 'Вася', 1]]
        with pytest.raises(AttributeError):
            get_popular_names(mentors)


# # -----------------------------Testing get_courses_by_durations--------------------------------
class TestDuration:
    def test_return_expected_str(self):
        courses = ['1', '2']
        durations = [5, 10]
        expect = '1 - 5 месяцев\n2 - 10 месяцев\n'
        result = get_courses_by_durations(courses, durations)
        assert result == expect

    def test_different_count_of_args(self):
        courses = ['1', '2']
        durations = [5]
        expect = '1 - 5 месяцев\n'
        result = get_courses_by_durations(courses, durations)
        assert result == expect

    def test_sorting_by_duration(self):
        courses = ['1', '2', '3', '4', '5']
        durations = [5, 10, 2, 20, 17]
        expect = '3 - 2 месяцев\n1 - 5 месяцев\n2 - 10 месяцев\n5 - 17 месяцев\n4 - 20 месяцев\n'
        result = get_courses_by_durations(courses, durations)
        assert result == expect
