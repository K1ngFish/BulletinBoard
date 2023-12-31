# BulletinBoard

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)

## Задание

Нам необходимо разработать интернет-ресурс для фанатского сервера одной
известной ММОRPG — что-то вроде доски объявлений. Пользователи нашего ресурса
должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с
кодом подтверждения регистрации. После регистрации им становится доступно
создание и редактирование объявлений. Объявления состоят из заголовка и текста,
внутри которого могут быть картинки, встроенные видео и другой контент.

Пользователи могут отправлять отклики на объявления других пользователей,
состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. 

Также пользователю должна быть доступна приватная
страница с откликами на его объявления, внутри которой он может фильтровать
отклики по объявлениям, удалять их и принимать (при принятии отклика
пользователю, оставившему отклик, также должно прийти уведомление). 

Кроме того, пользователь обязательно должен определить объявление в одну из следующих
категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники,
Зельевары, Мастера заклинаний.

Также мы бы хотели иметь возможность отправлять пользователям новостные
рассылки.

## Особенности

Проект реализован на на **Python** и **Django**.

:one: announcements, в котором реализованы основные модели и представления сайта,

:two: accounts, которое отвечает за регистрацию и авторизацию пользоваталей.

Регистрация и авторизация реализована как внутри проекта, так и посредством **OAuth** через *Yandex* и *Google*.


## Используемые библиотеки:
:white_check_mark: [CKEditor 4](https://ckeditor.com/docs/ckeditor4/latest/index.html). Предлагает широкие возможности форматирования текста, включая вставку картинок,

:white_check_mark: [Celery](https://docs.celeryq.dev/en/stable/),

:white_check_mark: [Redis](https://redis.io/docs/).



![thanks](https://img.shields.io/badge/thank_you-for_your_attention-blue)

