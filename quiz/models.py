from django.db import models


class Quiz(models.Model):
    title       = models.CharField(max_length = 150)
    author      = models.CharField(max_length = 50)
    img_url     = models.URLField(max_length = 2000)
    description = models.CharField(max_length = 500)

    class Meta:
        db_table = 'quizzes'

class QuizQuestion(models.Model):
    question     = models.CharField(max_length = 150)
    sorting_quiz = models.ForeignKey('Quiz', on_delete = models.CASCADE, null=True)
    answer       = models.CharField(max_length = 50)
    img_url      = models.URLField(max_length = 2000, null = True)

    class Meta:
        db_table = 'quiz_questions'

class QuizChoice(models.Model):
    choice        = models.CharField(max_length = 100)
    quiz_question = models.ForeignKey('QuizQuestion', on_delete = models.CASCADE, null = True)

    class Meta:
        db_table = 'quiz_choices'

class QuizResultMessage(models.Model):
    result = models.CharField(max_length = 50)
    score  = models.CharField(max_length = 50)

    class Meta:
        db_table = 'quiz_result_message'