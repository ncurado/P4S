#!/bin/bash

while true; do
    read -p "Do you wish to install a Postgres Container (Yes) or use your own DB (No) ?" yn
    case $yn in
        [Yy]* ) cp docker-compose-db-postgres.yml docker-compose.yml; 
                echo "If you want to use the predefined values, just press enter on all questions.";
                read -p "DB Username [app_user]: " dbusername;
                dbusername=${dbusername:-app_user};
                read -p "DB Password [app_user_password]: " dbpassword;
                dbpassword=${dbpassword:-app_user_password};
                read -p "DB Name [app]: " db;
                db=${db:-app};
                exec 3<> .env.prod.db;
                echo "POSTGRES_USER=${dbusername}" >&3;
                echo "POSTGRES_PASSWORD=${dbpassword}" >&3;
                echo "POSTGRES_DB=${db}" >&3;
                exec 3>&-;
                exec 3<> .env.prod;
                echo "DEBUG=0" >&3;
                NEW_UUID=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1);
                echo "SECRET_KEY=${NEW_UUID}" >&3;
                echo "DJANGO_ALLOWED_HOSTS=*" >&3; 
                echo "SQL_ENGINE=django.db.backends.postgresql" >&3;
                echo "SQL_DATABASE=${db}" >&3;
                echo "SQL_USER=${dbusername}" >&3;
                echo "SQL_PASSWORD=${dbpassword}" >&3;
                echo "SQL_HOST=db" >&3;
                echo "SQL_PORT=5432" >&3;
                exec 3>&-;
                break;;
        [Nn]* ) cp docker-compose-db-other.yml docker-compose.yml; 
                read -p "DB Name: " db;
                read -p "DB Host: " dbhost;
                read -p "DB Port: " dbport;
                read -p "DB Username: " dbusername;
                read -p "DB Password: " dbpassword;
                rm -rf .env.prod.db;
                exec 3<> .env.prod;
                echo "DEBUG=0" >&3;
                NEW_UUID=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1);
                echo "SECRET_KEY=${NEW_UUID}" >&3;
                echo "DJANGO_ALLOWED_HOSTS=*" >&3; 
                echo "SQL_ENGINE=django.db.backends.mysql" >&3;
                echo "SQL_DATABASE=${db}" >&3;
                echo "SQL_USER=${dbusername}" >&3;
                echo "SQL_PASSWORD=${dbpassword}" >&3;
                echo "SQL_HOST=${dbhost}" >&3;
                echo "SQL_PORT=${dbport}" >&3;
                exec 3>&-;
                break;;
        * )     echo "Please answer yes or no.";;
    esac
done