# Generated by Django 2.0.4 on 2018-06-02 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(blank=True, max_length=255, verbose_name='Primeiro nome')),
                ('segundo_nome', models.CharField(blank=True, max_length=255, verbose_name='Segundo nome')),
                ('phone_cell', models.CharField(blank=True, max_length=30, verbose_name='Celular')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('genero', models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino')], max_length=50, verbose_name='Genero')),
                ('estado_civil', models.CharField(choices=[('Solteira', 'Solteira'), ('Casada', 'Casada'), ('Viuva', 'Viuva'), ('Divorciada', 'Divorciada')], max_length=50, verbose_name='Genero')),
                ('naturalidade', models.CharField(max_length=255, verbose_name='Naturalidade')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=255, verbose_name='Celular')),
                ('fone', models.CharField(max_length=255, verbose_name='Telefone Fixo')),
                ('cpf', models.CharField(blank=True, max_length=255, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=255, verbose_name='RG')),
                ('emissor', models.CharField(blank=True, max_length=255, verbose_name='Orgão emissor')),
                ('profissao', models.CharField(blank=True, max_length=255, verbose_name='Profissão')),
                ('empresa', models.CharField(blank=True, max_length=255, verbose_name='Empresa')),
                ('peso', models.CharField(blank=True, max_length=255, verbose_name='Peso')),
                ('altura', models.CharField(blank=True, max_length=255, verbose_name='Altura')),
                ('nome_mae', models.CharField(max_length=255, verbose_name='Nome da Mãe')),
                ('nome_pai', models.CharField(max_length=255, verbose_name='Nome do Pai')),
                ('nome_responsavel', models.CharField(max_length=255, verbose_name='Nome do Responsável')),
                ('alergias', models.TextField(max_length=255, verbose_name='Alergias?')),
                ('observacoes', models.TextField(max_length=255, verbose_name='Observações')),
                ('convenio', models.CharField(max_length=255, verbose_name='Convênio')),
                ('numero_carteira', models.CharField(max_length=255, verbose_name='Número da Carteira')),
                ('validade', models.CharField(max_length=255, verbose_name='Validade')),
                ('endereco', models.ForeignKey(on_delete='Endereço', to='endereco.Address')),
            ],
        ),
    ]