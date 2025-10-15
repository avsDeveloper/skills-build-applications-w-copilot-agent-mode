from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Define models for each collection
class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    team = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'teams'

class Activity(models.Model):
    user_email = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'activities'

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'workouts'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            User(email='tony@stark.com', name='Iron Man', team='Marvel'),
            User(email='steve@rogers.com', name='Captain America', team='Marvel'),
            User(email='bruce@wayne.com', name='Batman', team='DC'),
            User(email='clark@kent.com', name='Superman', team='DC'),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user_email='tony@stark.com', type='Running', duration=30),
            Activity(user_email='steve@rogers.com', type='Cycling', duration=45),
            Activity(user_email='bruce@wayne.com', type='Swimming', duration=60),
            Activity(user_email='clark@kent.com', type='Flying', duration=120),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=180)

        # Create workouts
        workouts = [
            Workout(name='Push Ups', difficulty='Easy'),
            Workout(name='Pull Ups', difficulty='Medium'),
            Workout(name='Squats', difficulty='Hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
