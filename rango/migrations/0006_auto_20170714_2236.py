from __future__ import unicode_literals
import uuid
from django.db import migrations, models

from rango.models import Category


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_category_slug'),
    ]

    def gen_uuid(apps, schema_editor):
        for row in Category.objects.all():
            row.slug = uuid.uuid4()
            row.save()

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=uuid.uuid4),
            preserve_default=True,
        ),
        migrations.RunPython(gen_uuid),

        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
]
