# AutoCurioso – curiosidades sobre marcas de carros (Django)

## Passo a passo (igual ao quadro)
1. Criar venv:            `python -m venv venv`
2. Ativar venv:           `venv\Scripts\Activate.ps1`   (Linux/Mac: `source venv/bin/activate`)
3. Instalar Django:       `pip install -r requirements.txt`
4. Criar projeto:         `django-admin startproject config .`   (já feito neste repositório)
5. Migrações:             `python manage.py makemigrations` e depois `python manage.py migrate`
6. Super usuário:         `python manage.py createsuperuser`
7. Rodar projeto:         `python manage.py runserver`
8. Criar app:             `python manage.py startapp curiosidades`   (já feito)
9. Criar models:          `curiosidades/models.py`   (Marca, Carro, Curiosidade, Comentario)
10. Registrar no admin:   `curiosidades/admin.py`

Site: http://127.0.0.1:8000/  ·  Admin: http://127.0.0.1:8000/admin/
