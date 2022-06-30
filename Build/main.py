from new_student_lesson_builder import NewStudentLessonBuilder
from old_student_lesson_builder import OldStudentLessonBuilder
from lesson_director import LessonDirector
from lesson import Lesson

if __name__ == '__main__':
  lesson_builder = NewStudentLessonBuilder()
  lesson_director = LessonDirector(lesson_builder)
  lesson_director.make()

  lesson: Lesson = lesson_builder.get_result()
  print(f"Novo estudantes: {lesson.name} - {lesson.price} - {lesson.discounted_price}")

  lesson_builder = OldStudentLessonBuilder()
  lesson_director = LessonDirector(lesson_builder)
  lesson_director.make()

  lesson: Lesson = lesson_builder.get_result()
  print(f"Estudante antigo: {lesson.name} - {lesson.price} - {lesson.discounted_price}")
  # resultado: Inteligência Artificial - Iniciante a Avançado em 10 Minutos. - 49,99 - 24.995