# AFA TECH SOLUTIONS

## Backend
```
cd backend && python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # renseigner la clé secrète et MySQL
mysql -u root -p -e "CREATE DATABASE afatech CHARACTER SET utf8mb4;"
python manage.py makemigrations core && python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
## Frontend
```
cd frontend && cp .env.example .env && npm install && npm run dev
```
Admin Django : http://localhost:8000/admin/ — Tableau de bord Vue : http://localhost:5173/admin
