Автор: Constantine | myainetwork@gmail.com | http://infdots.blogspot.com
Лицензия: GNU/GPL v2

Этот сценарий был сделан для проверки PPPoE соединения и для переподключения. Этот сценарий был протестирован на Ubuntu 14.04.
Для начала вы должны создать подключение PPPoE, запустив утилиту pppoeconf. После этого вы будете иметь подключение PPPoE с
именем dsl-provider. После этого сделайте клон из хранилища, запустив 'git clone https://github.com/constantinekg/ppp-reconnect'
и переместите pppoe-reconnect.py в ваш любимый каталог (в качестве примера в /etc). Поместите это в crontab (crontab -e):
*/10 * * * * /etc/pppoe-reconnect -d 8.8.8.8 -t 10 > /var/log/pppoe-reconnect.log
Это сделает проверку (10 раз) каждые 10 минут для Google DNS, выполнив команду Ping. Если Google DNS будет недоступен сценарий
сделает повторное подключение PPPoE.
