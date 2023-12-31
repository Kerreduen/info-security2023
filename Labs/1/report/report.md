---
## Front matter
lang: ru-RU
title: "Лабораторная работа №1: отчет."
subtitle: "Установка и конфигурация операционной системы на виртуальную машину."
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

Целью данной работы является приобретение практических навыков
установки операционной системы на виртуальную машину, настройки минимально необходимых для дальнейшей работы сервисов.

# Задание

1. Создать и настроить виртуальную машину через VirtualBox.
2. Скачать и устоновить образ CentOS.
3. Запуск образа диска дополнений гостевой ОС и настроить систему.

# Выполнение лабораторной работы

## Пункт 1: создание виртуальной машины

Запустив VirtualBox создаёт новую виртуальную машину которую назовём "centos", создав предварительно для него папку в директории пользователя и оставив версию Red Hat так как она рекомендована инструкцией.

![Начало создания виртуальной машины](image/01.png){#fig:001 width=70% height=70%}

На следующем пункте оставляем всё без изменений так как таких параметров достаточно и при необходимости их можно увеличить.

![Настройка памяти и процессоров](image/02.png){#fig:002 width=70% height=70%}

Здесь я предоставил виртуальной машине 30 ГБ вместо 20, с запасом и указал "выделения в полном размере".

![Настройка виртуального жёсткого диска](image/03.png){#fig:003 width=70% height=70%}

Проверив введённые создаю виртуальную машину.

![Просмотр итога](image/04.png){#fig:004 width=70% height=70%}

## Пункт 2: Скачивание и настройка носителя

Предварительно скачав подходящую версию образа CentOS 7 использую её как носителя, и запускаю виртуальную машину.

![Указание носителя для виртуальной машины](image/05.png){#fig:005 width=70% height=70%}

## Пункт 3: Устоновка CentOS

Первум шагом при устоновки является выбор языка устоновки. Выберем для удобства русский.

![Выбор языка устоновки](image/06.png){#fig:006 width=70% height=70%}

Дальше мы видем образ устоновки где идут основные параметры устоновки.

![Образ устоновки](image/07.png){#fig:007 width=70% height=70%}

В первом разделе "Дата и время" мы проверяем праильно ли был устоновлем часовой пояс, время и дата.

![Дата и время](image/08.png){#fig:008 width=70% height=70%}

Второй раздел позваляет настроить порядок инициализации языков которые используется на клавиатуре.

![Раскладка клавиатуры](image/09.png){#fig:009 width=70% height=70%}

В третьем разделе можно выбрать дополнительный язык (к основному английскому), выбираем русский.

![Языковая поддержка](image/10.png){#fig:010 width=70% height=70%}

Дальше смотрим раздел "источника установки", оставляем ранее утановленный образ диска.

![Источник установки (образ CentOS)](image/11.png){#fig:011 width=70% height=70%}

В разделе среды выбираем "сервер GUI" так как он нам подходит и также в дополнительных указываем "Средства разработки".

![Выбор базового окружения](image/12.png){#fig:012 width=70% height=70%}

Дальше выбираем место устоновки наше созданное виртуальное пространство.

![Место устоновки](image/13.png){#fig:013 width=70% height=70%}

В в следуешем разделе отключаем KDUMP так как он не понадовится.

![Убрать KDUMP](image/14.png){#fig:014 width=70% height=70%}

И в последнем нужном нам разделе мы включаем ethernet и называем узел (хост) также как и пользователь.

![Настройка сети и узла](image/15.png){#fig:015 width=70% height=70%}

## Пункт 4: Настройка пользоыателя и root

На данном этапе начинается сама установка компонентов в это время мы можем настроить root-права и создать первого пользователя.

![Процесс устоновки и конфигурации](image/16.png){#fig:016 width=70% height=70%}

здесь мы указываем удобный нам пороль для получения root-прав.

![root пороль](image/17.png){#fig:017 width=70% height=70%}

В этом разделе мы указываем основные параметры для нашего пользователя: имя, права администратора и пороль.

![Создание пользователя](image/18.png){#fig:018 width=70% height=70%}

После не большого ожидания завершаем устоновку перезапустив виртуальную машину.

![Завершение устоновки](image/19.png){#fig:019 width=70% height=70%}

## Пункт 5: Устоновка образа диска доп. гост. ОС

После перезапуска у нас открывается последнее окно, приняв лицензию, мы завершаем устоновку и входим в систему.

![Финальная настройка](image/20.png){#fig:020 width=70% height=70%}

Здесь мы принимаем лицензию от CentOS.

![Соглашение с лицензией](image/21.png){#fig:021 width=70% height=70%}

После закрытия ознакомительной части при первом запуске мы выходим из окна системы и переходим в раздел устройства выше и подключаем образ диска дополнительного гостевого ОС.

![Подключение доп. гост. ОС](image/22.png){#fig:022 width=70% height=70%}

И устанавливаем его. дождавшись завершения установки перезапускаем виртуальную машину и среда готова к использованию.

![Устоновка образа доп. гост. ОС](image/23.png){#fig:023 width=70% height=70%}

# Контрольные вопросы

## 1. Какую информацию содержит учётная запись пользователя?

Все важные данные о пользователя в систему, хранятся в файлах "/etc/passwd", так в учётной записи хранится в первую очередь ID пользователя (где 0 это с root-правами и в системе CentOS 1-999 обычные пользователи), логин, пороль, идентификаторе группы, идентификаторе пользователя, начальный каталог и регистрационная оболочка. Если детально расмотреть структуру хранящихся данных то у нас получится такая строка данных: "User ID":"Password":"UID":"GID":"User Info":"Home Dir":"Shell".

## 2. Укажите команды терминала и приведите примеры:

– для получения справки по команде;
Для этого можно использовать команду "man", данная команда может предоставить инструкцию или справку по использованию команды или программы. Если нужна краткая информация можно применить команду "whatis".

– для перемещения по файловой системе;
Чтобы перемещаться нужно знать где ты и куда можешь пойти для этого есть команда "ls" позволяющая просмотреть содержание нынешней папки, а также комадна "ll" позволяющая просмотреть начинку директории. И самая главная команда "cd" - меняет текущий каталог на указанный, при пустом вводе перемещает на уровень выше в древе каталога.

– для просмотра содержимого каталога;
Как я указал выше для этого есть команда "ls" позволяющая просмотреть содержание нынешней папки, а также комадна "ll" позволяющая просмотреть начинку директории.

– для определения объёма каталога;
В большенстве систем на linux можно использовать команду "sudo du" (особенно утилита du) она выведит занимаемое котологом место на диске.

– для создания / удаления каталогов / файлов;
Стандартная команда для создание каталога или директории (файлов) "mkdir", а также команды для взаимодействия с ними: "cp" - основная задача копирование и дублирование, "mv" - перемещение и переиминовывание, "rm" - удаление папок и файлов. Также есть команда "cat" - показывает что содержит файл или стандартный ввод, а также "ln" - создающая фактически ссылку как в windows ярлыки.

– для задания определённых прав на файл / каталог;
фЕдинственная универсальная команда помимо задания прав при создании файла это "chmod".

– для просмотра истории команд.
Для этого есть стандартная команда "history", так помимо опций указав число после команды она выведет именно столько последних команд.

## 3. Что такое файловая система? Приведите примеры с краткой характеристикой.

Одно из определений гласит "Файловая система связывает носитель информации (хранилище) с прикладным программным обеспечением, организуя доступ к конкретным файлам при помощи функционала взаимодействия программ API". Тоесть файловая система это набор драйверов встроенных в систему которая при обращение программы к файлу по его имени (адресу) предостовляет информацию, касающуюся типа носителя, на котором записан файл, и структуры хранения данных. Получается на деле драйверы ФС оптимизируют запись и считывание отдельных частей файлов для ускоренной обработки запросов.

Так на система типа Linux можно увидеть много разных ФС: Ext2, Ext3, Ext4, JFS, ReiserFS, XFS, Btrfs, ZFS и т.д. А например на Windows в основном используется NTFS для внутрених файлов и FAT32 (или NTFS) для флешек и внешних насителей есть и другие, но они не так важны и универсальны. И на Android особенно более современных стоит Ext4 - внутренняя и FAT32 - внешняя.

NTFS (файловая система новой технологии) - стандарт был реализован в Windows NT в 1995 году, и по сей день является основным в Windows. Система NTFS имеет допустимый предел размера файлов до 16 гигабайт и размер диска (памяти) до 16 Эксабайт, а также Использование метод «прозрачного шифрования» (Encryption File System) разделяя доступ к файлом для разных пользователей и приложений.

## 4. Как посмотреть, какие файловые системы подмонтированы в ОС?

На большинстве современных систем можно легко и быстро определить это в свойствах диска. Но на разных системах Linux есть свои способы это проверить через настройки системы или команды. Так например эту информацию можно получить через утилиту Gnome Диски.

## 5. Как удалить зависший процесс?

В windows быстрее всего это сделать через диспечер задач или консоль (Win+R; cmd; tasklist; Taskkill "процесс"). В сестемах Linux есть несколько команд для этого с разной степень серьёзности: "SIGINT" - оправляет приложение команду правильного безопасного завершения, "SIGQUIT" - отличается от предыдущей возможностью проигнорировать сигнал и созданием dump-памяти, "SIGHUP" - сообщает процессу о разрыве соединения с терминалом (в основном связана с неполадками интернета), "SIGTERM" - немедленное завершение процесса проводимого самим процессом или дочерними, "SIGKILL" - зевершение процесса через ядро не мгновенное; и команды для убийства: "kill" - и тут многое зависит от опции если её нет то используется одна из выше указанных, если стоит "-TERM" то пытается принудительно или настойчиво закрыть процесс, и если это не помагает то испольуем "-KILL" что направляет все силы на уничтожение процесса.

# Выводы

В результате выполнения работы мы ознакомились с основными этапами установки виртуальных машин и их настроек, а также создали виртуальную среду для выполнения последующих лабораторных работ.

# Список литературы {.unnumbered}

1. [Официальный сайт VirtualBox](https://www.virtualbox.org/)
2. [Официальный сайт CentOS](https://www.centos.org/)
3. [Источник скачивание CentOS](http://isoredirect.centos.org/centos/7/isos/x86_64/)
4. [Материал для выполнения лабораторной](https://esystem.rudn.ru/mod/folder/view.php?id=1031368)
