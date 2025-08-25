from django.db import models
from accounts.models import UserProfile

# Create your models here.

class Exercise(models.Model):
    exer_name = models.CharField(max_length=80, unique=True)
    muscular_group = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.exer_name

class Workout(models.Model):
    workout_type = models.CharField(max_length=80)
    muscular_workout_group = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.workout_type

class WorkoutExerciseRelationship(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    series = models.IntegerField()
    repetition = models.IntegerField()
    rest = models.IntegerField()
    order = models.IntegerField()

    def __str__(self):
        return f'{self.exercise.exer_name} - {self.workout.workout_type}'

class UserWorkout(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.workout.workout_type}'