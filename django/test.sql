INSERT INTO main_block."Physical_process"(name)
VALUES
('Гидрогазодинамика');


INSERT INTO main_block."Type_of_power_equipment"(name)
VALUES
('Паровые и газовые турбины'),
('Котельные установки'),
('Теплообменники');

INSERT INTO main_block."Ph.p._T.p.e."(id_Ph.p, id_T.p.e)
VALUES
(1,1),
(1,2),
(1,3);

INSERT INTO main_block."Area"(id_area, name_area)
VALUES
(0, 'Root'),
(1, 'Область расчетного случая'),
(2, 'Область объекта');

INSERT INTO main_block."Areas_tree"(id_subarea, id_area, name_subarea, id_parent_area)
VALUES
(0, 0, 'Root', NULL),
(1, 1, 'Сопловые каналы', 0),
(2, 1, 'Рабочие каналы', 0),
(3, 1, 'Труба круглого сечения', 0),
(4, 1, 'Конфузор', 0),
(5, 1, 'Диффузор', 0),
(6, 1, 'Конвективный газоход', 0),
(7, 1, 'Трубный отвод', 0),
(8, 2, 'Проточная часть турбины', 2),
(9, 2, 'Новый объект', 2),
(10, 2, 'Внезапное расширение/сужение', 2);

INSERT INTO main_block."Experiment_class"(id_Ph.p._T.p.e, id_subarea, "Main_pict", "Geom_pict", "Reg_pict", "Tepl_pict")
VALUES
(1, 1, '1_main.jpg', '1_geom.jpg', '1_reg.jpg', '1_tepl.jpg'),
(1, 2, '1_main.jpg', '1_geom.jpg', '1_reg.jpg', '1_tepl.jpg'),
(1, 3, '1_main.jpg', '1_geom.jpg', '1_reg.jpg', '1_tepl.jpg'),
(1, 4, '1_main.jpg', '1_geom.jpg', '1_reg.jpg', '1_tepl.jpg'),
(1, 5, '1_main.jpg', '1_geom.jpg', '1_reg.jpg', '1_tepl.jpg'),
(2, 6, '1_main.jpg', '1_geom.jpg', '1_reg.jpg', '1_tepl.jpg'),
(3, 7, '1_main.jpg', '1_geom.jpg', '1_reg.jpg', '1_tepl.jpg'),
(3, 8, '1_main.jpg', '1_geom.jpg', '1_reg.jpg', '1_tepl.jpg'),
(3, 9, '1_main.jpg', '1_geom.jpg', '1_reg.jpg', '1_tepl.jpg'),
(3, 10, '1_main.jpg', '1_geom.jpg', '1_reg.jpg', '1_tepl.jpg');



INSERT INTO main_block."Parametrs"(id_type, name_param, short_name_param, unit_param)
VALUES
(1, 'Угол входа потока', 'α0', 'град'),
(1, 'Угол выхода потока', 'α1', 'град'),
(1, 'Хорда лопатки', 'b', 'мм'),
(1, 'Высота лопатки', 'l', 'мм'),
(1, 'Средний диаметр', 'dcp', 'мм'),
(1, 'Шаг лопаток', 't', 'мм'),
(1, 'Относительный шаг', 't/b', 'безразмерный параметр'),
(1, 'Угол установки', 'ßy', 'град'),
(1, 'Относительная высота', 'b/l', 'безразмерный параметр'),
(2, 'Число Рейнольдса', 'Re', 'безразмерный параметр'),
(3, 'Температура на входе', 't1', '°C'),
(3, 'Среда', NULL, 'тип'),
(3, 'Давление на выходе', 'P', 'бар'),
(4, 'Глобальный элемент', 'Ge', 'мм'),
(4, 'Тип сетки', NULL, 'тип'),
(4, 'Вид глобальной ячейки', NULL, 'тип');


INSERT INTO main_block."String_values"(id_param, value)
VALUES
(12, 'Вода'),
(12, 'Воздух'),
(12, 'Пар'),
(15, 'Неструктурированная'),
(15, 'Структурированная'),
(16, 'Кубическая'),
(16, 'Октаэдрическая'),
(16, 'Тетраэдрическая');

INSERT INTO main_block."Experiment"(ID*, id_exp, id_param, id_data)
VALUES
(1, 1, 1, 1),
(1, 1, 2, 1),
(1, 1, 3, 1),
(1, 1, 4, 1),
(1, 1, 5, 1),
(1, 1, 6, 1),
(1, 1, 7, 1),
(1, 1, 8, 1),
(1, 1, 9, 1),
(1, 1, 10, 1),
(1, 1, 11, 1),
(1, 1, 12, 1),
(1, 1, 13, 1),
(1, 1, 14, 1),
(1, 1, 15, 1),
(1, 1, 16, 1);

INSERT INTO main_block."Parametrs_values"(id_value, value_number, value_range, value_string, value_image)
VALUES
(1, 1, NULL, NULL),
(2, 1, NULL, NULL),
(3, 1, NULL, NULL),
(4, 1, NULL, NULL),
(5, 1, NULL, NULL),
(6, 1, NULL, NULL),
(7, 1, NULL, NULL),
(8, 1, NULL, NULL),
(9, 1, NULL, NULL),
(10, 1, NULL, NULL),
(11, 1, NULL, NULL),
(12, 1, NULL, NULL),
(13, 1, NULL, NULL),
(14, 1, NULL, NULL),
(15, 1, NULL, NULL),
(16, 1, NULL, NULL);