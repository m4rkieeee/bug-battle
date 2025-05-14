
# 🐞 Uitgebreidere Challenge 4 – Verdwenen Evaluatievragen



# Context
Op het Mentor-platform worden per les evaluatievragen gekoppeld aan het type les.
Denk aan theorielessen, praktijklessen, coaching, enz. 
Elke EvaluationQuestion is gekoppeld aan een specifiek LessonType.

Een instructeur wil de evaluatie starten van een geplande les (object van Lesson).
De evaluatiepagina opent correct, maar er worden geen vragen weergegeven.

data voorbereiden:
```bash
python manage.py load_dummydata
```
Dit commando zet data klaar en ook de admin interface inloggen via 'admin' en 'iFixBugsAtNight'

applicatie starten:
```bash
python manage.py runserver
```

❌ Probleem
De view in views.py (EvaluationView) haalt wel “actieve” vragen op, maar filtert niet op het lesson_type van de geplande les. 
Hierdoor krijg je of te veel vragen, of (zoals in dit geval) geen vragen als ze gekoppeld 
zijn aan specifieke LessonTypes.

❌ Probleem 2 (voor gevorderden)
Het formulier slaat nu niks op, zorg ervoor dat ook de antwoorden opgeslagen kunnen worden.

