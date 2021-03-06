# Generated by Django 2.2.8 on 2019-12-20 11:56

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='VectorMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Vector map name')),
                ('map_type', models.CharField(choices=[('world_en', 'World'), ('europe_en', 'Europe'), ('europe_simple_en', 'Europe (simple)'), ('africa_en', 'Africa'), ('asia_en', 'Asia'), ('australia_en', 'Australia'), ('north-america_en', 'North America'), ('south-america_en', 'South America')], max_length=255, verbose_name='map type')),
                ('width', models.PositiveIntegerField(blank=True, null=True, verbose_name='szerokość')),
                ('width_units', models.CharField(choices=[('px', 'piksele (px)'), ('%', 'procenty (%)'), ('em', 'relatywne do rozmiaru czcionki (em)')], default='px', max_length=2, verbose_name='jednostki szerokości')),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='wysokość')),
                ('height_units', models.CharField(choices=[('px', 'piksele (px)'), ('%', 'procenty (%)'), ('em', 'relatywne do rozmiaru czcionki (em)')], default='px', max_length=2, verbose_name='jednostki wysokości')),
                ('background_color', models.CharField(blank=True, help_text='Any CSS compatible format', max_length=255, null=True, verbose_name='kolor tła')),
                ('border_color', models.CharField(blank=True, help_text='Any CSS compatible format', max_length=255, null=True, verbose_name='border color')),
                ('border_opacity', models.FloatField(default=0.25, help_text='In range from 0 to 1', verbose_name='border opacity')),
                ('border_width', models.PositiveIntegerField(default=1, verbose_name='border width')),
                ('map_color', models.CharField(blank=True, help_text='Any CSS compatible format', max_length=255, null=True, verbose_name='color of map regions')),
                ('enable_zoom', models.BooleanField(default=True, verbose_name='enable zoom')),
                ('enable_drag', models.BooleanField(default=True, verbose_name='enable drag')),
                ('initial_zoom', models.PositiveIntegerField(default=0, verbose_name='initial zoom')),
                ('hover_color', models.CharField(blank=True, help_text='Any CSS compatible format', max_length=255, null=True, verbose_name='hover color')),
                ('hover_opacity', models.FloatField(default=0.5, help_text='In range from 0 to 1', verbose_name='hover opacity')),
                ('selected_color', models.CharField(blank=True, help_text='Any CSS compatible format', max_length=255, null=True, verbose_name='selected color')),
                ('multi_select_regions', models.BooleanField(default=False, verbose_name='allow to multi select regions')),
                ('show_labels', models.BooleanField(default=False, verbose_name='Show ISO code labels')),
                ('show_tooltip', models.BooleanField(default=True, verbose_name='Show tooltip on mouseover')),
            ],
            options={
                'verbose_name': 'Vector map',
                'verbose_name_plural': 'Vector maps',
            },
        ),
        migrations.CreateModel(
            name='VectorMapPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_vector_map_vectormapplugin', serialize=False, to='cms.CMSPlugin')),
                ('vector_map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsplugin_vector_map.VectorMap', verbose_name='Choose a vector map')),
            ],
            options={
                'verbose_name': 'Vector map add-on',
                'verbose_name_plural': 'Vector maps add-ons',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(blank=True, help_text='Code of the country where the pin will appear', max_length=255, null=True, verbose_name='country code')),
                ('preselect', models.BooleanField(default=True, verbose_name='preselect region')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Pin text content')),
                ('vector_map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsplugin_vector_map.VectorMap', verbose_name='Vector map')),
            ],
            options={
                'verbose_name': 'Vector map pin',
                'verbose_name_plural': 'Vector map pins',
            },
        ),
    ]
