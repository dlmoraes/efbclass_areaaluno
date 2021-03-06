# Generated by Django 3.1.7 on 2021-03-25 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('matricula', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=150)),
                ('dta_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('foto_perfil', models.CharField(blank=True, max_length=200)),
                ('tipo_acesso', models.IntegerField(choices=[(1, 'Aluno'), (2, 'Instrutor'), (3, 'Administrador')], default=1)),
                ('cod_ativacao', models.CharField(max_length=200)),
                ('status', models.IntegerField(choices=[(1, 'Ativo'), (2, 'Inativo'), (3, 'Suspenso')], default=1)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('departamento', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['departamento'],
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('empresa', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['empresa'],
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('equipe', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoTurma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('regional', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Regional',
                'verbose_name_plural': 'Regionais',
                'ordering': ['regional'],
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('setor', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
                'ordering': ['setor'],
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('alunos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('equipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.equipe')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.grupoturma')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
                'ordering': ['equipes', 'alunos'],
            },
        ),
        migrations.CreateModel(
            name='MovTeste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('pontuacao', models.IntegerField()),
                ('ultima_posicao', models.CharField(blank=True, max_length=30)),
                ('ultima_questao', models.CharField(blank=True, max_length=30)),
                ('alunos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('topicos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.topico')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='grupoturma',
            name='membros',
            field=models.ManyToManyField(through='aluno.Turma', to='aluno.Aluno'),
        ),
        migrations.CreateModel(
            name='Discussao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=200)),
                ('imagem', models.CharField(blank=True, max_length=255)),
                ('dicussao_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
            ],
            options={
                'verbose_name': 'Discuss??o',
                'verbose_name_plural': 'Discuss??es',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('mensagem', models.TextField()),
                ('comenta_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
            ],
            options={
                'verbose_name': 'Coment??rio',
                'verbose_name_plural': 'Coment??rios',
                'ordering': ['comenta_aluno'],
            },
        ),
    ]
