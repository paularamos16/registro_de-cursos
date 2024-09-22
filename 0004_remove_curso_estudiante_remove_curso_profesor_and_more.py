

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_curso_estudiante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='estudiante',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='profesor',
        ),
        migrations.AddField(
            model_name='curso',
            name='estudiante',
            field=models.ManyToManyField(related_name='cursos', to='main.estudiante'),
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='main.profesor'),
        ),
    ]