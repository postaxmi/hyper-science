# Generated by Django 2.1.7 on 2019-02-20 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images_backend', '0006_auto_20190217_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributedefinition',
            name='kind',
        ),
        migrations.AddField(
            model_name='attributedefinition',
            name='value_type',
            field=models.CharField(choices=[('B', 'Boolean'), ('I', 'Integer'), ('D', 'Double'), ('S', 'String')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='instancevalue',
            name='category_dict',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='images_backend.CategoryDictionary'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categorydefinition',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='images_backend.CategoryDefinition'),
        ),
        migrations.AlterField(
            model_name='instancevalue',
            name='value',
            field=models.TextField(),
        ),
    ]
