daemon = True
bind = 'unix:/home/kaev/myvenv/run/gunicorn.sock mybbs.wsgi:application'
workers=5
