# Generated by Django 4.1.3 on 2022-12-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("serviceapp", "0007_uploadidea_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadidea",
            name="payment",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="uploadidea",
            name="fileToUpload",
            field=models.FileField(null=True, upload_to="ideas/"),
        ),
        migrations.AlterField(
            model_name="uploadidea",
            name="status",
            field=models.BooleanField(null=True),
        ),
    ]
