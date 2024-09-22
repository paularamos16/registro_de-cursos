

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='cursos', to='main.estudiante'),
        ),
    ]