-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Апр 18 2023 г., 06:13
-- Версия сервера: 8.0.24
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `слова для бота вк`
--

-- --------------------------------------------------------

--
-- Структура таблицы `word for bot`
--

CREATE TABLE `word for bot` (
  `RussianWord` varchar(20) DEFAULT NULL,
  `EnglishWord` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `word for bot`
--

INSERT INTO `word for bot` (`RussianWord`, `EnglishWord`) VALUES
('машина', 'car'),
('инструмент', 'tool'),
('жизнь', 'life'),
('час', 'hour'),
('день', 'day'),
('ночь', 'night'),
('месяц', 'month'),
('год', 'year'),
('время', 'time'),
('мир', 'world'),
('солнце', 'sun'),
('животное', 'animal'),
('дерево', 'tree');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
