from django.contrib import admin
from .models import Exercise, Workout, WorkoutExerciseRelationship, UserWorkout

# Register your models here.

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(WorkoutExerciseRelationship)
admin.site.register(UserWorkout)