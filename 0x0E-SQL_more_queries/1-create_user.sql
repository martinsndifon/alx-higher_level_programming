--  script that creates the MySQL server user user_0d_1.

CREATE IF NOT EXISTS USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEDGES ON *.* TO 'user_0d_1'@'localhost';
