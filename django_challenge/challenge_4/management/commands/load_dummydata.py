from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from challenge_4.models import LessonType, Lesson, EvaluationQuestion
from challenge_2.models import Training, TrainingSubscription

class Command(BaseCommand):
    help = "Laadt dummydata in voor evaluatie: lesstypes, lessen en vragen"

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Verwijdert eerst alle bestaande gegevens uit Lesson, LessonType en EvaluationQuestion',
        )

    def handle(self, *args, **options):
        if options['reset']:
            self.stdout.write("⚠️  Verwijderen van bestaande gegevens...")
            EvaluationQuestion.objects.all().delete()
            Lesson.objects.all().delete()
            LessonType.objects.all().delete()
            self.stdout.write(self.style.WARNING("⬛ Alle bestaande data gewist."))

        self.stdout.write("⏳ Dummydata aan het aanmaken...")

        # Lesstypes
        types = [
            ("theorie", "Theorieles"),
            ("praktijk", "Praktijkles"),
            ("coaching", "Coaching"),
        ]

        lesson_type_objs = {}
        for code, name in types:
            lt, _ = LessonType.objects.get_or_create(code=code, defaults={"name": name})
            lesson_type_objs[code] = lt

        # Evaluatievragen
        questions = [
            ("Wat vond je van de uitleg?", "theorie"),
            ("Hoe duidelijk waren de praktijkopdrachten?", "praktijk"),
            ("Had je voldoende persoonlijke begeleiding?", "coaching"),
            ("Zou je deze les aanraden aan anderen?", "praktijk"),
            ("Was de sfeer goed tijdens de les?", "theorie"),
        ]

        for text, type_code in questions:
            EvaluationQuestion.objects.get_or_create(
                text=text,
                lesson_type=lesson_type_objs[type_code],
                defaults={"active": True}
            )

        # Lessen
        now = timezone.now()
        lessons = [
            ("HTML & CSS basis", now - timedelta(days=2), "theorie"),
            ("Praktijkoefening Django Models", now - timedelta(days=1), "praktijk"),
            ("1-op-1 begeleiding: portfolio", now, "coaching"),
        ]

        for title, date, type_code in lessons:
            Lesson.objects.get_or_create(
                title=title,
                date=date,
                lesson_type=lesson_type_objs[type_code]
            )

        user, created = User.objects.get_or_create(username="admin", is_superuser=True, is_staff=True)

        user.set_password("iFixBugsAtNight")

        training = Training.objects.create(name="Python Beginners")
        training2 = Training.objects.create(name="Bug Hunt for Beginners")
        training3 = Training.objects.create(name="Training die ik nog moet vormgeven.")

        u1 = User.objects.create_user("alice")
        u2 = User.objects.create_user("bob")
        u3 = User.objects.create_user("carla")

        TrainingSubscription.objects.create(student=u1, training=training, subscribed=True)
        TrainingSubscription.objects.create(student=u1, training=training2, subscribed=True)
        TrainingSubscription.objects.create(student=u2, training=training, subscribed=False)
        TrainingSubscription.objects.create(student=u2, training=training2, subscribed=False)
        TrainingSubscription.objects.create(student=u3, training=training, subscribed=True)

        self.stdout.write(self.style.SUCCESS("✅ Dummydata succesvol aangemaakt."))
