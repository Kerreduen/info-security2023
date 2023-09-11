---
## Front matter
lang: ru-RU
title: "Лабораторная работа №3: отчет."
subtitle: "Дискреционное разграничение прав в Linux. Два пользователя."
author: "Евдокимов Максим Михайлович. Группа - НФИбд-01-20."

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Получение практических навыков работы в консоли с атрибутами файлов для групп пользователей.

# Задание

1. Создать нового пользователя и сравнить его параметры с пользователем из второй лабораторной.
2. Создать группы для пользователей guest и guest2, где guest будет главным.
3. Провести анализ уровней доступа в группе и на основе этих данных создать 2 новые таблицы подобные из второй лабораторной.

# Выполнение лабораторной работы

## Пункт 1, 2

В установленной операционной системе проверяем учётную запись пользователя guest (использую учётную запись администратора) "sudo useradd guest", убеждаемся что, и Задайте пароль для пользователя guest (использую учётную запись администратора) "sudo passwd guest".

![Создание пользователя 1 и вход от него](image/01.png){#fig:001 width=70% height=70%}

## Пункт 3, 4

Аналогично создаём второго пользователя guest2 "sudo useradd guest2" и "sudo passwd guest2" и добавляем пользователя guest2 в группу guest командой "gpasswd -a guest2 guest".

![Создание пользователя 2 и вход от него](image/02.png){#fig:002 width=70% height=70%}

![Создание пользователя 2 и вход от него](image/03.png){#fig:003 width=70% height=70%}

## Пункт 5, 6

Осуществите вход в систему от двух пользователей на двух разных консолях: guest на первой консоли и guest2 на второй консоли. Также для обоих пользователей командой "pwd" определяем директорию, в которой вы находитесь, сравнив её с приглашениями командной строки.

![Вход в систему и проверка директории](image/04.png){#fig:004 width=70% height=70%}

## Пункт 7, 8

Уточним имя вашего пользователя, его группу, кто входит в неё и к каким группам принадлежит он сам, для этого используем команду "groups guest" и "groups guest2". Сравните вывод команды "groups" с выводом команд "id -Gn" и "id -G", для каждого пользователя.

![Проанализировать группу и пользоавтелей в ней](image/05.png){#fig:005 width=70% height=70%}

Сравните полученную информацию с содержимым файла "/etc/group" командой "cat /etc/group" от имени администратора (max).

![Проверка групп 1](image/06.png){#fig:006 width=70% height=70%}

![Проверка групп 2](image/07.png){#fig:007 width=70% height=70%}

## Пункт 9, 10

От имени пользователя guest2 выполняем регистрацию пользователя guest2 в группе guest командой "newgrp guest". От имени пользователя guest изменим права директории "/home/guest", разрешив все действия для пользователей группы: "chmod g+rwx /home/guest".

![Регистрация и и изменение прав](image/08.png){#fig:008 width=70% height=70%}

## Пункт 11

От имени пользователя guest снимите с директории "/home/guest/dir1" все атрибуты командой "chmod 000 dirl". И проведём анализ и изменяя уровень доступа директории и файла "file1" в нём на основные операции для пользователя группы guest2.

![изменения через chmod](image/09.png){#fig:009 width=70% height=70%}

Проверяем как работает доступ на группе сделав простую проверку.

![Тестирование](image/10.png){#fig:010 width=70% height=70%}

# Таблицы

## 11.1 Установленные права и разрешённые действия 2

![Таблица с уровнями доступа 1](image/11.png){#fig:011 width=70% height=70%}

![Таблица с уровнями доступа 2](image/12.png){#fig:012 width=70% height=70%}

## 11.2 Минимальной необходимые права для выполнения операций 2

![Таблица соответствия операции и необходимого уровня доступа](image/13.png){#fig:013 width=70% height=70%}

# Выводы

В ходе выполнения лабораторной работы были получены основные знания и навыки по работе с группами и несколькими пользователями.

# Список литературы {.unnumbered}

1. [Основные команды для работы с Linux](https://eternalhost.net/blog/sozdanie-saytov/osnovnye-komandy-linux)
2. [Основы управления пользоателем и командой su](https://losst.pro/komanda-su-v-linux)
3. [Файл лабораторной работы](https://esystem.rudn.ru/pluginfile.php/2090275/mod_resource/content/4/003-lab_discret_2users.pdf)
4. [Linux всё о правах доступа к файлам](https://itdid.ru/file_permissions.html)
