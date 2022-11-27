CREATE DATABASE IF NOT EXISTS ventas2022
        CHARACTER SET = 'utf8'
        COLLATE = 'utf8_general_ci'

DROP USER IF EXISTS 'adminuser'@'backend';
DROP USER IF EXISTS 'adminuser'@'mysqldatabase';

CREATE USER IF NOT EXISTS 'adminuser'@'backend' IDENTIFIED BY 'adminuser123';
CREATE USER IF NOT EXISTS 'adminuser'@'mysqldatabase' IDENTIFIED BY 'adminuser123';

GRANT USAGE ON ventas2022.* TO 'adminuser'@'backend';
GRANT USAGE ON ventas2022.* TO 'adminuser'@'mysqldatabase';

FLUSH PRIVILEGES;
