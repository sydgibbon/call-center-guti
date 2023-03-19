-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-03-2023 a las 20:47:45
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `glpi`
--

--
-- Volcado de datos para la tabla `glpi_agenttypes`
--

REPLACE INTO `glpi_agenttypes` (`id`, `name`) VALUES(1, 'Core');

--
-- Volcado de datos para la tabla `glpi_apiclients`
--

REPLACE INTO `glpi_apiclients` (`id`, `entities_id`, `is_recursive`, `name`, `date_mod`, `date_creation`, `is_active`, `ipv4_range_start`, `ipv4_range_end`, `ipv6`, `app_token`, `app_token_date`, `dolog_method`, `comment`) VALUES(1, 0, 1, 'full access from localhost', NULL, NULL, 1, 2130706433, 2130706433, '::1', NULL, NULL, 0, NULL);

--
-- Volcado de datos para la tabla `glpi_autoupdatesystems`
--

REPLACE INTO `glpi_autoupdatesystems` (`id`, `name`, `comment`) VALUES(1, 'UpdateSource1', '');

--
-- Volcado de datos para la tabla `glpi_blacklists`
--

REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(1, 3, 'invalid serial', 'N/A', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(2, 3, 'invalid serial', '(null string)', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(3, 3, 'invalid serial', 'INVALID', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(4, 3, 'invalid serial', 'SYS-1234567890', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(5, 3, 'invalid serial', 'SYS-9876543210', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(6, 3, 'invalid serial', 'SN-12345', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(7, 3, 'invalid serial', 'SN-1234567890', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(8, 3, 'invalid serial', '/^0+$/', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(9, 3, 'invalid serial', '/^1+$/', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(10, 3, 'invalid serial', '/\\d\\.\\d(\\.\\d)?/', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(11, 3, 'invalid serial', '/^(0|1)+$/', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(12, 3, 'invalid serial', '0123456789', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(13, 3, 'invalid serial', '12345', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(14, 3, 'invalid serial', '123456', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(15, 3, 'invalid serial', '1234567', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(16, 3, 'invalid serial', '12345678', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(17, 3, 'invalid serial', '123456789', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(18, 3, 'invalid serial', '1234567890', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(19, 3, 'invalid serial', '123456789000', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(20, 3, 'invalid serial', '12345678901234567', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(21, 3, 'invalid serial', 'NNNNNNN', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(22, 3, 'invalid serial', 'xxxxxxxxxxx', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(23, 3, 'invalid serial', 'EVAL', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(24, 3, 'invalid serial', 'IATPASS', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(25, 3, 'invalid serial', 'none', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(26, 3, 'invalid serial', 'To Be Filled By O.E.M.', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(27, 3, 'invalid serial', 'Tulip Computers', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(28, 3, 'invalid serial', 'Serial Number xxxxxx', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(29, 3, 'invalid serial', 'SN-123456fvgv3i0b8o5n6n7k', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(30, 3, 'invalid serial', 'Unknow', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(31, 3, 'invalid serial', 'System Serial Number', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(32, 3, 'invalid serial', 'MB-1234567890', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(33, 3, 'invalid serial', 'empty', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(34, 3, 'invalid serial', 'Not Specified', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(35, 3, 'invalid serial', 'OEM_Serial', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(36, 3, 'invalid serial', 'SystemSerialNumb', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(37, 4, 'invalid UUID', 'FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(38, 4, 'invalid UUID', '03000200-0400-0500-0006-000700080009', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(39, 4, 'invalid UUID', '6AB5B300-538D-1014-9FB5-B0684D007B53', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(40, 4, 'invalid UUID', '01010101-0101-0101-0101-010101010101', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(41, 4, 'invalid UUID', '2', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(42, 2, 'empty MAC', '', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(43, 2, 'invalid MAC', '20:41:53:59:4e:ff', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(44, 2, 'invalid MAC', '02:00:4e:43:50:49', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(45, 2, 'invalid MAC', 'e2:e6:16:20:0a:35', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(46, 2, 'invalid MAC', 'd2:0a:2d:a0:04:be', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(47, 2, 'invalid MAC', '00:a0:c6:00:00:00', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(48, 2, 'invalid MAC', 'd2:6b:25:2f:2c:e7', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(49, 2, 'invalid MAC', '33:50:6f:45:30:30', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(50, 2, 'invalid MAC', '0a:00:27:00:00:00', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(51, 2, 'invalid MAC', '00:50:56:C0:00:01', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(52, 2, 'invalid MAC', '00:50:56:C0:00:08', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(53, 2, 'invalid MAC', '02:80:37:EC:02:00', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(54, 2, 'invalid MAC', '50:50:54:50:30:30', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(55, 2, 'invalid MAC', '24:b6:20:52:41:53', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(56, 2, 'invalid MAC', '00:50:56:C0:00:02', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(57, 2, 'invalid MAC', '/00:50:56:C0:[0-9a-f]+:[0-9a-f]+/i', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(58, 2, 'invalid MAC', 'FE:FF:FF:FF:FF:FF', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(59, 2, 'invalid MAC', '00:00:00:00:00:00', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(60, 2, 'invalid MAC', '00:0b:ca:fe:00:00', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(61, 6, 'Unknow', 'Unknow', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(62, 6, 'To Be Filled By O.E.M.', 'To Be Filled By O.E.M.', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(63, 6, '*', '*', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(64, 6, 'System Product Name', 'System Product Name', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(65, 6, 'Product Name', 'Product Name', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(66, 6, 'System Name', 'System Name', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(67, 6, 'All Series', 'All Series', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(68, 8, 'System manufacturer', 'System manufacturer', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(69, 1, 'empty IP', '', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(70, 1, 'zero IP', '0.0.0.0', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(71, 1, 'localhost', '127.0.0.1', NULL, NULL, NULL);
REPLACE INTO `glpi_blacklists` (`id`, `type`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(72, 1, 'IPV6 localhost', '::1', NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_cables`
--

REPLACE INTO `glpi_cables` (`id`, `name`, `entities_id`, `is_recursive`, `itemtype_endpoint_a`, `itemtype_endpoint_b`, `items_id_endpoint_a`, `items_id_endpoint_b`, `socketmodels_id_endpoint_a`, `socketmodels_id_endpoint_b`, `sockets_id_endpoint_a`, `sockets_id_endpoint_b`, `cablestrands_id`, `color`, `otherserial`, `states_id`, `users_id_tech`, `cabletypes_id`, `comment`, `date_mod`, `date_creation`, `is_deleted`) VALUES(1, 'Cable1', 0, 0, 'Computer', 'Computer', 1, 1, 1, 1, 0, 0, 1, '#dddddd', '12312321', 2, 0, 1, 'Comment', '2023-03-19 19:40:27', '2023-03-19 19:40:27', 0);

--
-- Volcado de datos para la tabla `glpi_cablestrands`
--

REPLACE INTO `glpi_cablestrands` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'CableStrand1', 'Comment', '2023-03-19 19:39:31', '2023-03-19 19:39:31');

--
-- Volcado de datos para la tabla `glpi_cabletypes`
--

REPLACE INTO `glpi_cabletypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'CableType1', 'Comment', '2023-03-19 19:39:17', '2023-03-19 19:39:17');

--
-- Volcado de datos para la tabla `glpi_calendars`
--

REPLACE INTO `glpi_calendars` (`id`, `name`, `entities_id`, `is_recursive`, `comment`, `date_mod`, `cache_duration`, `date_creation`) VALUES(1, 'Default', 0, 1, 'Default calendar', NULL, '[0,43200,43200,43200,43200,43200,0]', NULL);

--
-- Volcado de datos para la tabla `glpi_calendarsegments`
--

REPLACE INTO `glpi_calendarsegments` (`id`, `calendars_id`, `entities_id`, `is_recursive`, `day`, `begin`, `end`) VALUES(1, 1, 0, 0, 1, '08:00:00', '20:00:00');
REPLACE INTO `glpi_calendarsegments` (`id`, `calendars_id`, `entities_id`, `is_recursive`, `day`, `begin`, `end`) VALUES(2, 1, 0, 0, 2, '08:00:00', '20:00:00');
REPLACE INTO `glpi_calendarsegments` (`id`, `calendars_id`, `entities_id`, `is_recursive`, `day`, `begin`, `end`) VALUES(3, 1, 0, 0, 3, '08:00:00', '20:00:00');
REPLACE INTO `glpi_calendarsegments` (`id`, `calendars_id`, `entities_id`, `is_recursive`, `day`, `begin`, `end`) VALUES(4, 1, 0, 0, 4, '08:00:00', '20:00:00');
REPLACE INTO `glpi_calendarsegments` (`id`, `calendars_id`, `entities_id`, `is_recursive`, `day`, `begin`, `end`) VALUES(5, 1, 0, 0, 5, '08:00:00', '20:00:00');

--
-- Volcado de datos para la tabla `glpi_cartridgeitems`
--

REPLACE INTO `glpi_cartridgeitems` (`id`, `entities_id`, `is_recursive`, `name`, `ref`, `locations_id`, `cartridgeitemtypes_id`, `manufacturers_id`, `users_id_tech`, `groups_id_tech`, `is_deleted`, `comment`, `alarm_threshold`, `stock_target`, `date_mod`, `date_creation`, `pictures`) VALUES(1, 0, 0, 'CartridgeCon2horasdesueno', 'reference', 1, 1, 2, 0, 0, 0, 'Comment1', 10, 2, '2023-03-19 19:33:19', '2023-03-19 19:33:19', NULL);

--
-- Volcado de datos para la tabla `glpi_cartridgeitemtypes`
--

REPLACE INTO `glpi_cartridgeitemtypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'CartridgeType1', 'comment', '2023-03-19 19:33:01', '2023-03-19 19:33:01');

--
-- Volcado de datos para la tabla `glpi_changetemplatemandatoryfields`
--

REPLACE INTO `glpi_changetemplatemandatoryfields` (`id`, `changetemplates_id`, `num`) VALUES(1, 1, 21);

--
-- Volcado de datos para la tabla `glpi_changetemplates`
--

REPLACE INTO `glpi_changetemplates` (`id`, `name`, `entities_id`, `is_recursive`, `comment`) VALUES(1, 'Default', 0, 1, NULL);

--
-- Volcado de datos para la tabla `glpi_computermodels`
--

REPLACE INTO `glpi_computermodels` (`id`, `name`, `comment`, `product_number`, `weight`, `required_units`, `depth`, `power_connections`, `power_consumption`, `is_half_rack`, `picture_front`, `picture_rear`, `pictures`, `date_mod`, `date_creation`) VALUES(1, 'ComputerModel1', '', '', 0, 1, 1, 0, 0, 0, NULL, NULL, NULL, '2023-03-19 19:16:21', '2023-03-19 19:16:21');
REPLACE INTO `glpi_computermodels` (`id`, `name`, `comment`, `product_number`, `weight`, `required_units`, `depth`, `power_connections`, `power_consumption`, `is_half_rack`, `picture_front`, `picture_rear`, `pictures`, `date_mod`, `date_creation`) VALUES(2, 'ComputerModel2', 'Comment', '23423432423434', 2, 3, 1, 2, 123, 0, NULL, NULL, NULL, '2023-03-19 19:16:45', '2023-03-19 19:16:45');

--
-- Volcado de datos para la tabla `glpi_computers`
--

REPLACE INTO `glpi_computers` (`id`, `entities_id`, `name`, `serial`, `otherserial`, `contact`, `contact_num`, `users_id_tech`, `groups_id_tech`, `comment`, `date_mod`, `autoupdatesystems_id`, `locations_id`, `networks_id`, `computermodels_id`, `computertypes_id`, `is_template`, `template_name`, `manufacturers_id`, `is_deleted`, `is_dynamic`, `users_id`, `groups_id`, `states_id`, `ticket_tco`, `uuid`, `date_creation`, `is_recursive`, `last_inventory_update`, `last_boot`) VALUES(1, 0, 'Computer1', '333333333333', '2222222', 'ALTERNATEUSERNAME', '123232323', 0, 0, '', '2023-03-19 19:17:32', 1, 1, 1, 2, 3, 0, NULL, 2, 0, 0, 0, 0, 1, '0.0000', 'uuid', '2023-03-19 19:17:32', 0, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_computertypes`
--

REPLACE INTO `glpi_computertypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'PC', '', '2023-03-19 19:15:32', '2023-03-19 19:15:32');
REPLACE INTO `glpi_computertypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'Laptop', '', '2023-03-19 19:15:36', '2023-03-19 19:15:36');
REPLACE INTO `glpi_computertypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(3, 'All-In-One', '', '2023-03-19 19:15:46', '2023-03-19 19:15:46');

--
-- Volcado de datos para la tabla `glpi_configs`
--

REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(1, 'core', 'version', '10.0.6');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(2, 'core', 'show_jobs_at_login', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(3, 'core', 'cut', '250');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(4, 'core', 'list_limit', '15');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(5, 'core', 'list_limit_max', '50');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(6, 'core', 'url_maxlength', '30');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(7, 'core', 'event_loglevel', '5');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(8, 'core', 'notifications_mailing', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(9, 'core', 'admin_email', 'admsys@localhost');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(10, 'core', 'admin_email_name', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(11, 'core', 'from_email', NULL);
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(12, 'core', 'from_email_name', NULL);
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(13, 'core', 'noreply_email', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(14, 'core', 'noreply_email_name', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(15, 'core', 'replyto_email', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(16, 'core', 'replyto_email_name', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(17, 'core', 'mailing_signature', 'SIGNATURE');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(18, 'core', 'use_anonymous_helpdesk', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(19, 'core', 'use_anonymous_followups', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(20, 'core', 'language', 'en_US');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(21, 'core', 'priority_1', '#fff2f2');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(22, 'core', 'priority_2', '#ffe0e0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(23, 'core', 'priority_3', '#ffcece');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(24, 'core', 'priority_4', '#ffbfbf');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(25, 'core', 'priority_5', '#ffadad');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(26, 'core', 'priority_6', '#ff5555');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(27, 'core', 'date_tax', '2005-12-31');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(28, 'core', 'cas_host', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(29, 'core', 'cas_port', '443');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(30, 'core', 'cas_uri', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(31, 'core', 'cas_logout', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(32, 'core', 'cas_version', 'CAS_VERSION_2_0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(33, 'core', 'existing_auth_server_field_clean_domain', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(34, 'core', 'planning_begin', '08:00:00');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(35, 'core', 'planning_end', '20:00:00');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(36, 'core', 'utf8_conv', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(37, 'core', 'use_public_faq', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(38, 'core', 'url_base', 'http://localhost/glpi');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(39, 'core', 'show_link_in_mail', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(40, 'core', 'text_login', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(41, 'core', 'founded_new_version', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(42, 'core', 'dropdown_max', '100');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(43, 'core', 'ajax_wildcard', '*');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(44, 'core', 'ajax_limit_count', '10');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(45, 'core', 'is_users_auto_add', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(46, 'core', 'date_format', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(47, 'core', 'number_format', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(48, 'core', 'csv_delimiter', ';');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(49, 'core', 'is_ids_visible', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(50, 'core', 'smtp_mode', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(51, 'core', 'smtp_host', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(52, 'core', 'smtp_port', '25');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(53, 'core', 'smtp_username', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(54, 'core', 'proxy_name', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(55, 'core', 'proxy_port', '8080');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(56, 'core', 'proxy_user', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(57, 'core', 'add_followup_on_update_ticket', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(58, 'core', 'keep_tickets_on_delete', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(59, 'core', 'time_step', '5');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(60, 'core', 'decimal_number', '2');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(61, 'core', 'helpdesk_doc_url', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(62, 'core', 'central_doc_url', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(63, 'core', 'documentcategories_id_forticket', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(64, 'core', 'monitors_management_restrict', '2');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(65, 'core', 'phones_management_restrict', '2');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(66, 'core', 'peripherals_management_restrict', '2');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(67, 'core', 'printers_management_restrict', '2');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(68, 'core', 'use_log_in_files', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(69, 'core', 'time_offset', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(70, 'core', 'is_contact_autoupdate', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(71, 'core', 'is_user_autoupdate', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(72, 'core', 'is_group_autoupdate', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(73, 'core', 'is_location_autoupdate', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(74, 'core', 'state_autoupdate_mode', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(75, 'core', 'is_contact_autoclean', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(76, 'core', 'is_user_autoclean', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(77, 'core', 'is_group_autoclean', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(78, 'core', 'is_location_autoclean', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(79, 'core', 'state_autoclean_mode', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(80, 'core', 'use_flat_dropdowntree', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(81, 'core', 'use_autoname_by_entity', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(82, 'core', 'softwarecategories_id_ondelete', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(83, 'core', 'x509_email_field', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(84, 'core', 'x509_cn_restrict', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(85, 'core', 'x509_o_restrict', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(86, 'core', 'x509_ou_restrict', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(87, 'core', 'default_mailcollector_filesize_max', '2097152');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(88, 'core', 'followup_private', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(89, 'core', 'task_private', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(90, 'core', 'default_software_helpdesk_visible', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(91, 'core', 'names_format', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(92, 'core', 'default_requesttypes_id', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(93, 'core', 'use_noright_users_add', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(94, 'core', 'cron_limit', '5');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(95, 'core', 'priority_matrix', '{\"1\":{\"1\":1,\"2\":1,\"3\":2,\"4\":2,\"5\":2},\"2\":{\"1\":1,\"2\":2,\"3\":2,\"4\":3,\"5\":3},\"3\":{\"1\":2,\"2\":2,\"3\":3,\"4\":4,\"5\":4},\"4\":{\"1\":2,\"2\":3,\"3\":4,\"4\":4,\"5\":5},\"5\":{\"1\":2,\"2\":3,\"3\":4,\"4\":5,\"5\":5}}');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(96, 'core', 'urgency_mask', '62');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(97, 'core', 'impact_mask', '62');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(98, 'core', 'user_deleted_ldap', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(99, 'core', 'user_restored_ldap', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(100, 'core', 'auto_create_infocoms', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(101, 'core', 'use_slave_for_search', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(102, 'core', 'proxy_passwd', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(103, 'core', 'smtp_passwd', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(104, 'core', 'show_count_on_tabs', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(105, 'core', 'refresh_views', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(106, 'core', 'set_default_tech', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(107, 'core', 'allow_search_view', '2');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(108, 'core', 'allow_search_all', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(109, 'core', 'allow_search_global', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(110, 'core', 'display_count_on_home', '5');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(111, 'core', 'use_password_security', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(112, 'core', 'password_min_length', '8');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(113, 'core', 'password_need_number', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(114, 'core', 'password_need_letter', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(115, 'core', 'password_need_caps', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(116, 'core', 'password_need_symbol', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(117, 'core', 'use_check_pref', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(118, 'core', 'notification_to_myself', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(119, 'core', 'duedateok_color', '#06ff00');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(120, 'core', 'duedatewarning_color', '#ffb800');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(121, 'core', 'duedatecritical_color', '#ff0000');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(122, 'core', 'duedatewarning_less', '20');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(123, 'core', 'duedatecritical_less', '5');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(124, 'core', 'duedatewarning_unit', '%');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(125, 'core', 'duedatecritical_unit', '%');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(126, 'core', 'realname_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(127, 'core', 'firstname_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(128, 'core', 'email1_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(129, 'core', 'email2_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(130, 'core', 'email3_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(131, 'core', 'email4_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(132, 'core', 'phone_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(133, 'core', 'phone2_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(134, 'core', 'mobile_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(135, 'core', 'comment_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(136, 'core', 'title_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(137, 'core', 'category_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(138, 'core', 'language_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(139, 'core', 'entity_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(140, 'core', 'registration_number_ssofield', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(141, 'core', 'ssovariables_id', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(142, 'core', 'ssologout_url', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(143, 'core', 'translate_kb', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(144, 'core', 'translate_dropdowns', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(145, 'core', 'translate_reminders', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(146, 'core', 'pdffont', 'helvetica');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(147, 'core', 'keep_devices_when_purging_item', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(148, 'core', 'maintenance_mode', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(149, 'core', 'maintenance_text', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(150, 'core', 'attach_ticket_documents_to_mail', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(151, 'core', 'backcreated', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(152, 'core', 'task_state', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(153, 'core', 'palette', 'auror');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(154, 'core', 'page_layout', 'vertical');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(155, 'core', 'fold_menu', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(156, 'core', 'fold_search', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(157, 'core', 'savedsearches_pinned', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(158, 'core', 'timeline_order', 'natural');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(159, 'core', 'itil_layout', '');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(160, 'core', 'richtext_layout', 'classic');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(161, 'core', 'lock_use_lock_item', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(162, 'core', 'lock_autolock_mode', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(163, 'core', 'lock_directunlock_notification', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(164, 'core', 'lock_item_list', '[]');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(165, 'core', 'lock_lockprofile_id', '8');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(166, 'core', 'set_default_requester', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(167, 'core', 'highcontrast_css', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(168, 'core', 'default_central_tab', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(169, 'core', 'smtp_check_certificate', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(170, 'core', 'enable_api', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(171, 'core', 'enable_api_login_credentials', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(172, 'core', 'enable_api_login_external_token', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(173, 'core', 'url_base_api', 'http://localhost/glpi/apirest.php/');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(174, 'core', 'login_remember_time', '604800');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(175, 'core', 'login_remember_default', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(176, 'core', 'use_notifications', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(177, 'core', 'notifications_ajax', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(178, 'core', 'notifications_ajax_check_interval', '5');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(179, 'core', 'notifications_ajax_sound', NULL);
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(180, 'core', 'notifications_ajax_icon_url', '/pics/glpi.png');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(181, 'core', 'dbversion', '10.0.6@21cffee0fbb5afbf0d580cabdf6fd7a922598f97');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(182, 'core', 'smtp_max_retries', '5');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(183, 'core', 'smtp_sender', NULL);
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(184, 'core', 'instance_uuid', NULL);
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(185, 'core', 'registration_uuid', 'PTHnuqaeNgjTSBF74bqRFgoAPf2Nr97W0c2rXfWU');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(186, 'core', 'smtp_retry_time', '5');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(187, 'core', 'purge_addrelation', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(188, 'core', 'purge_deleterelation', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(189, 'core', 'purge_createitem', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(190, 'core', 'purge_deleteitem', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(191, 'core', 'purge_restoreitem', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(192, 'core', 'purge_updateitem', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(193, 'core', 'purge_item_software_install', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(194, 'core', 'purge_software_item_install', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(195, 'core', 'purge_software_version_install', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(196, 'core', 'purge_infocom_creation', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(197, 'core', 'purge_profile_user', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(198, 'core', 'purge_group_user', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(199, 'core', 'purge_adddevice', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(200, 'core', 'purge_updatedevice', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(201, 'core', 'purge_deletedevice', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(202, 'core', 'purge_connectdevice', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(203, 'core', 'purge_disconnectdevice', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(204, 'core', 'purge_userdeletedfromldap', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(205, 'core', 'purge_comments', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(206, 'core', 'purge_datemod', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(207, 'core', 'purge_all', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(208, 'core', 'purge_user_auth_changes', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(209, 'core', 'purge_plugins', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(210, 'core', 'purge_refusedequipment', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(211, 'core', 'display_login_source', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(212, 'core', 'devices_in_menu', '[\"Item_DeviceSimcard\"]');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(213, 'core', 'password_expiration_delay', '-1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(214, 'core', 'password_expiration_notice', '-1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(215, 'core', 'password_expiration_lock_delay', '-1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(216, 'core', 'default_dashboard_central', 'central');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(217, 'core', 'default_dashboard_assets', 'assets');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(218, 'core', 'default_dashboard_helpdesk', 'assistance');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(219, 'core', 'default_dashboard_mini_ticket', 'mini_tickets');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(220, 'core', 'impact_enabled_itemtypes', '[\"Appliance\",\"Cluster\",\"Computer\",\"Datacenter\",\"DCRoom\",\"Domain\",\"Enclosure\",\"Monitor\",\"NetworkEquipment\",\"PDU\",\"Peripheral\",\"Phone\",\"Printer\",\"Rack\",\"Software\",\"DatabaseInstance\"]');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(221, 'core', 'document_max_size', '40');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(222, 'core', 'planning_work_days', '[0,1,2,3,4,5,6]');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(223, 'core', 'system_user', '6');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(224, 'core', 'support_legacy_data', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(225, 'core', 'initialized_rules_collections', '[\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\",\"RuleTicketCollection\",\"RuleAssetCollection\",\"RuleDictionnaryOperatingSystemCollection\",\"RuleDictionnaryOperatingSystemVersionCollection\",\"RuleDictionnaryOperatingSystemEditionCollection\"]');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(226, 'core', 'timeline_action_btn_layout', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(227, 'core', 'timeline_date_format', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(228, 'inventory', 'enabled_inventory', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(229, 'inventory', 'import_software', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(230, 'inventory', 'import_volume', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(231, 'inventory', 'import_antivirus', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(232, 'inventory', 'import_registry', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(233, 'inventory', 'import_process', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(234, 'inventory', 'import_vm', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(235, 'inventory', 'import_monitor_on_partial_sn', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(236, 'inventory', 'import_unmanaged', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(237, 'inventory', 'component_processor', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(238, 'inventory', 'component_memory', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(239, 'inventory', 'component_harddrive', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(240, 'inventory', 'component_networkcard', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(241, 'inventory', 'component_graphiccard', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(242, 'inventory', 'component_soundcard', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(243, 'inventory', 'component_drive', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(244, 'inventory', 'component_networkdrive', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(245, 'inventory', 'component_networkcardvirtual', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(246, 'inventory', 'component_control', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(247, 'inventory', 'component_battery', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(248, 'inventory', 'component_simcard', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(249, 'inventory', 'states_id_default', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(250, 'inventory', 'entities_id_default', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(251, 'inventory', 'location', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(252, 'inventory', 'group', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(253, 'inventory', 'vm_type', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(254, 'inventory', 'vm_components', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(255, 'inventory', 'vm_as_computer', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(256, 'inventory', 'component_removablemedia', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(257, 'inventory', 'component_powersupply', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(258, 'inventory', 'inventory_frequency', '24');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(259, 'inventory', 'import_monitor', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(260, 'inventory', 'import_printer', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(261, 'inventory', 'import_peripheral', '1');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(262, 'inventory', 'stale_agents_delay', '0');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(263, 'inventory', 'stale_agents_action', '[0]');
REPLACE INTO `glpi_configs` (`id`, `context`, `name`, `value`) VALUES(264, 'inventory', 'stale_agents_status', '0');

--
-- Volcado de datos para la tabla `glpi_consumableitems`
--

REPLACE INTO `glpi_consumableitems` (`id`, `entities_id`, `is_recursive`, `name`, `ref`, `locations_id`, `consumableitemtypes_id`, `manufacturers_id`, `users_id_tech`, `groups_id_tech`, `is_deleted`, `comment`, `alarm_threshold`, `stock_target`, `date_mod`, `date_creation`, `otherserial`, `pictures`) VALUES(1, 0, 0, 'ConsumableKindOfModelProbably', 'ref', 1, 1, 2, 0, 0, 0, '', 10, 0, '2023-03-19 19:33:56', '2023-03-19 19:33:56', '2223232323', NULL);

--
-- Volcado de datos para la tabla `glpi_consumableitemtypes`
--

REPLACE INTO `glpi_consumableitemtypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'asdsadasdas', '', '2023-03-19 19:33:44', '2023-03-19 19:33:44');

--
-- Volcado de datos para la tabla `glpi_crontasklogs`
--

REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(1, 5, 0, '2023-03-19 19:12:52', 0, 0, 0, 'Run mode: GLPI');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(2, 5, 1, '2023-03-19 19:12:52', 2, 0.176698, 0, 'Action completed, no processing required');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(3, 6, 0, '2023-03-19 19:18:51', 0, 0, 0, 'Run mode: GLPI');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(4, 6, 3, '2023-03-19 19:18:51', 2, 0.0246718, 0, 'Action completed, no processing required');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(5, 9, 0, '2023-03-19 19:26:17', 0, 0, 0, 'Run mode: GLPI');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(6, 9, 5, '2023-03-19 19:26:17', 2, 0.069602, 0, 'Action completed, no processing required');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(7, 12, 0, '2023-03-19 19:31:54', 0, 0, 0, 'Run mode: GLPI');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(8, 12, 7, '2023-03-19 19:31:54', 2, 0.0264449, 0, 'Action completed, no processing required');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(9, 13, 0, '2023-03-19 19:37:20', 0, 0, 0, 'Run mode: GLPI');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(10, 13, 9, '2023-03-19 19:37:20', 2, 0.0341418, 0, 'Action completed, no processing required');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(11, 14, 0, '2023-03-19 19:42:36', 0, 0, 0, 'Run mode: GLPI');
REPLACE INTO `glpi_crontasklogs` (`id`, `crontasks_id`, `crontasklogs_id`, `date`, `state`, `elapsed`, `volume`, `content`) VALUES(12, 14, 11, '2023-03-19 19:42:36', 2, 0.033371, 0, 'Action completed, no processing required');

--
-- Volcado de datos para la tabla `glpi_crontasks`
--

REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'CartridgeItem', 'cartridge', 86400, 10, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(3, 'ConsumableItem', 'consumable', 86400, 10, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(4, 'SoftwareLicense', 'software', 86400, NULL, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(5, 'Contract', 'contract', 86400, NULL, 1, 1, 3, 0, 24, 30, '2023-03-19 15:12:00', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(6, 'Infocom', 'infocom', 86400, NULL, 1, 1, 3, 0, 24, 30, '2023-03-19 15:18:00', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(7, 'CronTask', 'logs', 86400, 30, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(9, 'MailCollector', 'mailgate', 600, 10, 1, 1, 3, 0, 24, 30, '2023-03-19 15:26:00', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(10, 'DBconnection', 'checkdbreplicate', 300, NULL, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(11, 'CronTask', 'checkupdate', 604800, NULL, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(12, 'CronTask', 'session', 86400, NULL, 1, 1, 3, 0, 24, 30, '2023-03-19 15:31:00', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(13, 'CronTask', 'graph', 3600, NULL, 1, 1, 3, 0, 24, 30, '2023-03-19 15:37:00', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(14, 'ReservationItem', 'reservation', 3600, NULL, 1, 1, 3, 0, 24, 30, '2023-03-19 15:42:00', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(15, 'Ticket', 'closeticket', 43200, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(16, 'Ticket', 'alertnotclosed', 43200, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(17, 'SlaLevel_Ticket', 'slaticket', 300, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(18, 'Ticket', 'createinquest', 86400, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(19, 'CronTask', 'watcher', 86400, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(20, 'CommonITILRecurrentCron', 'RecurrentItems', 3600, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(21, 'PlanningRecall', 'planningrecall', 300, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(22, 'QueuedNotification', 'queuednotification', 60, 50, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(23, 'QueuedNotification', 'queuednotificationclean', 86400, 30, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(24, 'CronTask', 'temp', 3600, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(25, 'MailCollector', 'mailgateerror', 86400, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(26, 'CronTask', 'circularlogs', 86400, 4, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(27, 'ObjectLock', 'unlockobject', 86400, 4, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(28, 'SavedSearch', 'countAll', 604800, NULL, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(29, 'SavedSearch_Alert', 'savedsearchesalerts', 86400, NULL, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(30, 'Telemetry', 'telemetry', 2592000, NULL, 0, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(31, 'Certificate', 'certificate', 86400, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(32, 'OlaLevel_Ticket', 'olaticket', 300, NULL, 1, 1, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(33, 'PurgeLogs', 'PurgeLogs', 604800, 24, 1, 2, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(34, 'Ticket', 'purgeticket', 604800, NULL, 0, 2, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(35, 'Document', 'cleanorphans', 604800, NULL, 0, 2, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(36, 'User', 'passwordexpiration', 86400, 100, 0, 2, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(37, 'Glpi\\Marketplace\\Controller', 'checkAllUpdates', 86400, NULL, 1, 2, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(38, 'CleanSoftwareCron', 'cleansoftware', 2592000, 1000, 0, 2, 3, 0, 24, 300, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(39, 'Domain', 'DomainsAlert', 86400, NULL, 1, 2, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(40, 'Glpi\\Inventory\\Inventory', 'cleantemp', 86400, NULL, 0, 2, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(41, 'Glpi\\Inventory\\Inventory', 'cleanorphans', 604800, NULL, 1, 2, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(42, 'PendingReasonCron', 'pendingreason_autobump_autosolve', 1800, NULL, 1, 2, 3, 0, 24, 60, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_crontasks` (`id`, `itemtype`, `name`, `frequency`, `param`, `state`, `mode`, `allowmode`, `hourmin`, `hourmax`, `logs_lifetime`, `lastrun`, `lastcode`, `comment`, `date_mod`, `date_creation`) VALUES(43, 'Agent', 'Cleanoldagents', 86400, NULL, 1, 2, 3, 0, 24, 30, NULL, NULL, NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_dashboards_dashboards`
--

REPLACE INTO `glpi_dashboards_dashboards` (`id`, `key`, `name`, `context`, `users_id`) VALUES(1, 'central', 'Central', 'core', 0);
REPLACE INTO `glpi_dashboards_dashboards` (`id`, `key`, `name`, `context`, `users_id`) VALUES(2, 'assets', 'Assets', 'core', 0);
REPLACE INTO `glpi_dashboards_dashboards` (`id`, `key`, `name`, `context`, `users_id`) VALUES(3, 'assistance', 'Assistance', 'core', 0);
REPLACE INTO `glpi_dashboards_dashboards` (`id`, `key`, `name`, `context`, `users_id`) VALUES(4, 'mini_tickets', 'Mini ticket Dashboard', 'mini_core', 0);

--
-- Volcado de datos para la tabla `glpi_dashboards_items`
--

REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(1, 1, 'bn_count_Computer_4a315743-151c-40cb-a20b-762250668dac', 'bn_count_Computer', 3, 0, 3, 2, '{\"color\":\"#e69393\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(2, 1, 'bn_count_Software_0690f524-e826-47a9-b50a-906451196b83', 'bn_count_Software', 0, 0, 3, 2, '{\"color\":\"#aaddac\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(3, 1, 'bn_count_Rack_c6502e0a-5991-46b4-a771-7f355137306b', 'bn_count_Rack', 6, 2, 3, 2, '{\"color\":\"#0e87a0\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(4, 1, 'bn_count_SoftwareLicense_e755fd06-283e-4479-ba35-2d548f8f8a90', 'bn_count_SoftwareLicense', 0, 2, 3, 2, '{\"color\":\"#27ab3c\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(5, 1, 'bn_count_Monitor_7059b94c-583c-4ba7-b100-d40461165318', 'bn_count_Monitor', 3, 2, 3, 2, '{\"color\":\"#b52d30\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(6, 1, 'bn_count_Ticket_a74c0903-3387-4a07-9111-b0938af8f1e7', 'bn_count_Ticket', 14, 7, 3, 2, '{\"color\":\"#ffdc64\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(7, 1, 'bn_count_Problem_c1cf5cfb-f626-472e-82a1-49c3e200e746', 'bn_count_Problem', 20, 7, 3, 2, '{\"color\":\"#f08d7b\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(8, 1, 'count_Computer_Manufacturer_6129c451-42b5-489d-b693-c362adf32d49', 'count_Computer_Manufacturer', 0, 4, 5, 4, '{\"color\":\"#f8faf9\",\"widgettype\":\"donut\",\"use_gradient\":\"1\",\"limit\":\"5\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(9, 1, 'top_ticket_user_requester_c74f52a8-046a-4077-b1a6-c9f840d34b82', 'top_ticket_user_requester', 14, 9, 6, 5, '{\"color\":\"#f9fafb\",\"widgettype\":\"hbar\",\"use_gradient\":\"1\",\"limit\":\"5\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(10, 1, 'bn_count_tickets_late_04c47208-d7e5-4aca-9566-d46e68c45c67', 'bn_count_tickets_late', 17, 7, 3, 2, '{\"color\":\"#f8911f\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(11, 1, 'ticket_status_2e4e968b-d4e6-4e33-9ce9-a1aaff53dfde', 'ticket_status', 14, 0, 12, 7, '{\"color\":\"#fafafa\",\"widgettype\":\"stackedbars\",\"use_gradient\":\"0\",\"limit\":\"12\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(12, 1, 'top_ticket_ITILCategory_37736ba9-d429-4cb3-9058-ef4d111d9269', 'top_ticket_ITILCategory', 20, 9, 6, 5, '{\"color\":\"#fbf9f9\",\"widgettype\":\"hbar\",\"use_gradient\":\"1\",\"limit\":\"5\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(13, 1, 'bn_count_Printer_517684b0-b064-49dd-943e-fcb6f915e453', 'bn_count_Printer', 9, 2, 3, 2, '{\"color\":\"#365a8f\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(14, 1, 'bn_count_Phone_f70c489f-02c1-46e5-978b-94a95b5038ee', 'bn_count_Phone', 9, 0, 3, 2, '{\"color\":\"#d5e1ec\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(15, 1, 'bn_count_Change_ab950dbd-cd25-466d-8dff-7dcaca386564', 'bn_count_Change', 23, 7, 3, 2, '{\"color\":\"#cae3c4\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(16, 1, 'bn_count_Group_b84a93f2-a26c-49d7-82a4-5446697cc5b0', 'bn_count_Group', 4, 8, 4, 2, '{\"color\":\"#e0e0e0\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(17, 1, 'bn_count_Profile_770b35e8-68e9-4b4f-9e09-5a11058f069f', 'bn_count_Profile', 4, 10, 4, 2, '{\"color\":\"#e0e0e0\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(18, 1, 'bn_count_Supplier_36ff9011-e4cf-4d89-b9ab-346b9857d734', 'bn_count_Supplier', 8, 8, 3, 2, '{\"color\":\"#c9c9c9\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(19, 1, 'bn_count_KnowbaseItem_a3785a56-bed4-4a30-8387-f251f5365b3b', 'bn_count_KnowbaseItem', 8, 10, 3, 2, '{\"color\":\"#c9c9c9\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(20, 1, 'bn_count_Entity_9b82951a-ba52-45cc-a2d3-1d238ec37adf', 'bn_count_Entity', 0, 10, 4, 2, '{\"color\":\"#f9f9f9\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(21, 1, 'bn_count_Document_7dc7f4b8-61ff-4147-b994-5541bddd7b66', 'bn_count_Document', 11, 8, 3, 2, '{\"color\":\"#b4b4b4\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(22, 1, 'bn_count_Project_4d412ee2-8b79-469b-995f-4c0a05ab849d', 'bn_count_Project', 11, 10, 3, 2, '{\"color\":\"#b3b3b3\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(23, 1, 'bn_count_NetworkEquipment_c537e334-d584-43bc-b6de-b4a939143e89', 'bn_count_NetworkEquipment', 6, 0, 3, 2, '{\"color\":\"#bfe7ea\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(24, 1, 'bn_count_User_ac0cbe52-3593-43c1-8ecc-0eb115de494d', 'bn_count_User', 0, 8, 4, 2, '{\"color\":\"#fafafa\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(25, 1, 'count_Monitor_MonitorModel_5a476ff9-116e-4270-858b-c003c20841a9', 'count_Monitor_MonitorModel', 5, 4, 5, 4, '{\"color\":\"#f5fafa\",\"widgettype\":\"donut\",\"use_gradient\":\"1\",\"limit\":\"5\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(26, 1, 'count_NetworkEquipment_State_81f2ae35-b366-4065-ac26-02ea4e3704a6', 'count_NetworkEquipment_State', 10, 4, 4, 4, '{\"color\":\"#f5f3ef\",\"widgettype\":\"donut\",\"use_gradient\":\"1\",\"limit\":\"5\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(27, 2, 'bn_count_Computer_34cfbaf9-a471-4852-b48c-0dadea7644de', 'bn_count_Computer', 0, 0, 4, 3, '{\"color\":\"#f3d0d0\",\"widgettype\":\"bigNumber\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(28, 2, 'bn_count_Software_60091467-2137-49f4-8834-f6602a482079', 'bn_count_Software', 4, 0, 4, 3, '{\"color\":\"#d1f1a8\",\"widgettype\":\"bigNumber\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(29, 2, 'bn_count_Printer_c9a385d4-76a3-4971-ad0e-1470efeafacc', 'bn_count_Printer', 8, 3, 4, 3, '{\"color\":\"#5da8d6\",\"widgettype\":\"bigNumber\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(30, 2, 'bn_count_PDU_60053eb6-8dda-4416-9a4b-afd51889bd09', 'bn_count_PDU', 12, 3, 4, 3, '{\"color\":\"#ffb62f\",\"widgettype\":\"bigNumber\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(31, 2, 'bn_count_Rack_0fdc196f-20d2-4f63-9ddb-b75c165cc664', 'bn_count_Rack', 12, 0, 4, 3, '{\"color\":\"#f7d79a\",\"widgettype\":\"bigNumber\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(32, 2, 'bn_count_Phone_c31fde2d-510a-4482-b17d-2f65b61eae08', 'bn_count_Phone', 16, 3, 4, 3, '{\"color\":\"#a0cec2\",\"widgettype\":\"bigNumber\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(33, 2, 'bn_count_Enclosure_c21ce30a-58c3-456a-81ec-3c5f01527a8f', 'bn_count_Enclosure', 16, 0, 4, 3, '{\"color\":\"#d7e8e4\",\"widgettype\":\"bigNumber\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(34, 2, 'bn_count_NetworkEquipment_76f1e239-777b-4552-b053-ae5c64190347', 'bn_count_NetworkEquipment', 8, 0, 4, 3, '{\"color\":\"#c8dae4\",\"widgettype\":\"bigNumber\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(35, 2, 'bn_count_SoftwareLicense_576e58fe-a386-480f-b405-1c2315b8ab47', 'bn_count_SoftwareLicense', 4, 3, 4, 3, '{\"color\":\"#9bc06b\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(36, 2, 'bn_count_Monitor_890e16d3-b121-48c6-9713-d9c239d9a970', 'bn_count_Monitor', 0, 3, 4, 3, '{\"color\":\"#dc6f6f\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(37, 2, 'count_Computer_Manufacturer_986e92e8-32e8-4a6f-806f-6f5383acbb3f', 'count_Computer_Manufacturer', 4, 6, 4, 4, '{\"color\":\"#f3f5f1\",\"widgettype\":\"hbar\",\"use_gradient\":\"1\",\"limit\":\"5\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(38, 2, 'count_Computer_State_290c5920-9eab-4db8-8753-46108e60f1d8', 'count_Computer_State', 0, 6, 4, 4, '{\"color\":\"#fbf7f7\",\"widgettype\":\"donut\",\"use_gradient\":\"1\",\"limit\":\"5\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(39, 2, 'count_Computer_ComputerType_c58f9c7e-22d5-478b-8226-d2a752bcbb09', 'count_Computer_ComputerType', 8, 6, 4, 4, '{\"color\":\"#f5f9fa\",\"widgettype\":\"donut\",\"use_gradient\":\"1\",\"limit\":\"5\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(40, 2, 'count_NetworkEquipment_Manufacturer_8132b21c-6f7f-4dc1-af54-bea794cb96e9', 'count_NetworkEquipment_Manufacturer', 12, 6, 4, 4, '{\"color\":\"#fcf8ed\",\"widgettype\":\"hbar\",\"use_gradient\":\"0\",\"limit\":\"5\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(41, 2, 'count_Monitor_Manufacturer_43b0c16b-af82-418e-aac1-f32b39705c0d', 'count_Monitor_Manufacturer', 16, 6, 4, 4, '{\"color\":\"#f9fbfb\",\"widgettype\":\"donut\",\"use_gradient\":\"1\",\"limit\":\"5\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(42, 3, 'bn_count_Ticket_344e761b-f7e8-4617-8c90-154b266b4d67', 'bn_count_Ticket', 0, 0, 3, 2, '{\"color\":\"#ffdc64\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(43, 3, 'bn_count_Problem_bdb4002b-a674-4493-820f-af85bed44d2a', 'bn_count_Problem', 0, 4, 3, 2, '{\"color\":\"#f0967b\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(44, 3, 'bn_count_Change_b9b87513-4f40-41e6-8621-f51f9a30fb19', 'bn_count_Change', 0, 6, 3, 2, '{\"color\":\"#cae3c4\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(45, 3, 'bn_count_tickets_late_1e9ae481-21b4-4463-a830-dec1b68ec5e7', 'bn_count_tickets_late', 0, 2, 3, 2, '{\"color\":\"#f8911f\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(46, 3, 'bn_count_tickets_incoming_336a36d9-67fe-4475-880e-447bd766b8fe', 'bn_count_tickets_incoming', 3, 6, 3, 2, '{\"color\":\"#a0e19d\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(47, 3, 'bn_count_tickets_closed_e004bab5-f2b6-4060-a401-a2a8b9885245', 'bn_count_tickets_closed', 9, 8, 3, 2, '{\"color\":\"#515151\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(48, 3, 'bn_count_tickets_assigned_7455c855-6df8-4514-a3d9-8b0fce52bd63', 'bn_count_tickets_assigned', 6, 6, 3, 2, '{\"color\":\"#eaf5f7\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(49, 3, 'bn_count_tickets_solved_5e9759b3-ee7e-4a14-b68f-1ac024ef55ee', 'bn_count_tickets_solved', 9, 6, 3, 2, '{\"color\":\"#d8d8d8\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(50, 3, 'bn_count_tickets_waiting_102b2c2a-6ac6-4d73-ba47-8b09382fe00e', 'bn_count_tickets_waiting', 3, 8, 3, 2, '{\"color\":\"#ffcb7d\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(51, 3, 'bn_count_TicketRecurrent_13f79539-61f6-45f7-8dde-045706e652f2', 'bn_count_TicketRecurrent', 0, 8, 3, 2, '{\"color\":\"#fafafa\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(52, 3, 'bn_count_tickets_planned_267bf627-9d5e-4b6c-b53d-b8623d793ccf', 'bn_count_tickets_planned', 6, 8, 3, 2, '{\"color\":\"#6298d5\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(53, 3, 'top_ticket_ITILCategory_0cba0c84-6c62-4cd8-8564-18614498d8e4', 'top_ticket_ITILCategory', 12, 6, 4, 4, '{\"color\":\"#f1f5ef\",\"widgettype\":\"donut\",\"use_gradient\":\"1\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(54, 3, 'top_ticket_RequestType_b9e43f34-8e94-4a6e-9023-c5d1e2ce7859', 'top_ticket_RequestType', 16, 6, 4, 4, '{\"color\":\"#f9fafb\",\"widgettype\":\"hbar\",\"use_gradient\":\"1\",\"limit\":\"4\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(55, 3, 'top_ticket_Entity_a8e65812-519c-488e-9892-9adbe22fbd5c', 'top_ticket_Entity', 20, 6, 4, 4, '{\"color\":\"#f7f1f0\",\"widgettype\":\"donut\",\"use_gradient\":\"1\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(56, 3, 'ticket_evolution_76fd4926-ee5e-48db-b6d6-e2947c190c5e', 'ticket_evolution', 3, 0, 12, 6, '{\"color\":\"#f3f7f8\",\"widgettype\":\"areas\",\"use_gradient\":\"0\",\"limit\":\"12\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(57, 3, 'ticket_status_5b256a35-b36b-4db5-ba11-ea7c125f126e', 'ticket_status', 15, 0, 11, 6, '{\"color\":\"#f7f3f2\",\"widgettype\":\"stackedbars\",\"use_gradient\":\"0\",\"limit\":\"12\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(58, 4, 'bn_count_tickets_closed_ccf7246b-645a-40d2-8206-fa33c769e3f5', 'bn_count_tickets_closed', 24, 0, 4, 2, '{\"color\":\"#fafafa\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(59, 4, 'bn_count_Ticket_d5bf3576-5033-40fb-bbdb-292294a7698e', 'bn_count_Ticket', 0, 0, 4, 2, '{\"color\":\"#ffd957\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(60, 4, 'bn_count_tickets_incoming_055e813c-b0ce-4687-91ef-559249e8ddd8', 'bn_count_tickets_incoming', 4, 0, 4, 2, '{\"color\":\"#6fd169\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(61, 4, 'bn_count_tickets_waiting_793c665b-b620-4b3a-a5a8-cf502defc008', 'bn_count_tickets_waiting', 8, 0, 4, 2, '{\"color\":\"#ffcb7d\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(62, 4, 'bn_count_tickets_assigned_d3d2f697-52b4-435e-9030-a760dd649085', 'bn_count_tickets_assigned', 12, 0, 4, 2, '{\"color\":\"#eaf4f7\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(63, 4, 'bn_count_tickets_planned_0c7f3569-c23b-4ee3-8e85-279229b23e70', 'bn_count_tickets_planned', 16, 0, 4, 2, '{\"color\":\"#6298d5\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');
REPLACE INTO `glpi_dashboards_items` (`id`, `dashboards_dashboards_id`, `gridstack_id`, `card_id`, `x`, `y`, `width`, `height`, `card_options`) VALUES(64, 4, 'bn_count_tickets_solved_ae2406cf-e8e8-410b-b355-46e3f5705ee8', 'bn_count_tickets_solved', 20, 0, 4, 2, '{\"color\":\"#d7d7d7\",\"widgettype\":\"bigNumber\",\"use_gradient\":\"0\",\"limit\":\"7\"}');

--
-- Volcado de datos para la tabla `glpi_dcrooms`
--

REPLACE INTO `glpi_dcrooms` (`id`, `name`, `entities_id`, `is_recursive`, `locations_id`, `vis_cols`, `vis_rows`, `blueprint`, `datacenters_id`, `is_deleted`, `date_mod`, `date_creation`) VALUES(1, 'ServerRoom1', 0, 0, 1, 1, 1, NULL, 0, 0, '2023-03-19 19:36:19', '2023-03-19 19:36:19');

--
-- Volcado de datos para la tabla `glpi_devicefirmwaretypes`
--

REPLACE INTO `glpi_devicefirmwaretypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'BIOS', NULL, NULL, NULL);
REPLACE INTO `glpi_devicefirmwaretypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'UEFI', NULL, NULL, NULL);
REPLACE INTO `glpi_devicefirmwaretypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(3, 'Firmware', NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_devicememorytypes`
--

REPLACE INTO `glpi_devicememorytypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'EDO', NULL, NULL, NULL);
REPLACE INTO `glpi_devicememorytypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'DDR', NULL, NULL, NULL);
REPLACE INTO `glpi_devicememorytypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(3, 'SDRAM', NULL, NULL, NULL);
REPLACE INTO `glpi_devicememorytypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(4, 'SDRAM-2', NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_devicesimcards`
--

REPLACE INTO `glpi_devicesimcards` (`id`, `designation`, `comment`, `entities_id`, `is_recursive`, `manufacturers_id`, `voltage`, `devicesimcardtypes_id`, `date_mod`, `date_creation`, `allow_voip`) VALUES(1, 'SimcardComponent', 'Comment', 0, 0, 4, 123, 1, '2023-03-19 19:40:50', '2023-03-19 19:40:50', 1);

--
-- Volcado de datos para la tabla `glpi_devicesimcardtypes`
--

REPLACE INTO `glpi_devicesimcardtypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'Full SIM', NULL, NULL, NULL);
REPLACE INTO `glpi_devicesimcardtypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'Mini SIM', NULL, NULL, NULL);
REPLACE INTO `glpi_devicesimcardtypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(3, 'Micro SIM', NULL, NULL, NULL);
REPLACE INTO `glpi_devicesimcardtypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(4, 'Nano SIM', NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_displaypreferences`
--

REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(1, 'Computer', 4, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(2, 'Computer', 45, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(3, 'Computer', 40, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(4, 'Computer', 5, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(5, 'Computer', 23, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(6, 'DocumentType', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(7, 'Monitor', 31, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(8, 'Monitor', 23, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(9, 'Monitor', 3, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(10, 'Monitor', 4, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(11, 'Printer', 31, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(12, 'NetworkEquipment', 31, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(13, 'NetworkEquipment', 23, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(14, 'Printer', 23, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(15, 'Printer', 3, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(16, 'Software', 4, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(17, 'Software', 5, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(18, 'Software', 23, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(19, 'CartridgeItem', 4, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(20, 'CartridgeItem', 34, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(21, 'Peripheral', 3, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(22, 'Peripheral', 23, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(23, 'Peripheral', 31, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(24, 'Computer', 31, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(25, 'Computer', 3, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(26, 'Computer', 19, 8, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(27, 'Computer', 17, 9, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(28, 'NetworkEquipment', 3, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(29, 'NetworkEquipment', 4, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(30, 'NetworkEquipment', 11, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(31, 'NetworkEquipment', 19, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(32, 'Printer', 4, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(33, 'Printer', 19, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(34, 'Monitor', 19, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(35, 'Monitor', 7, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(36, 'Peripheral', 4, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(37, 'Peripheral', 19, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(38, 'Peripheral', 7, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(39, 'Contact', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(40, 'Contact', 4, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(41, 'Contact', 5, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(42, 'Contact', 6, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(43, 'Contact', 9, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(44, 'Supplier', 9, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(45, 'Supplier', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(46, 'Supplier', 4, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(47, 'Supplier', 5, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(48, 'Supplier', 10, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(49, 'Supplier', 6, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(50, 'Contract', 4, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(51, 'Contract', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(52, 'Contract', 5, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(53, 'Contract', 6, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(54, 'Contract', 7, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(55, 'Contract', 11, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(56, 'CartridgeItem', 23, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(57, 'CartridgeItem', 3, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(58, 'DocumentType', 6, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(59, 'DocumentType', 4, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(60, 'DocumentType', 5, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(61, 'Document', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(62, 'Document', 4, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(63, 'Document', 7, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(64, 'Document', 5, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(65, 'Document', 16, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(66, 'User', 34, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(67, 'User', 5, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(68, 'User', 6, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(69, 'User', 3, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(70, 'ConsumableItem', 34, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(71, 'ConsumableItem', 4, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(72, 'ConsumableItem', 23, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(73, 'ConsumableItem', 3, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(74, 'NetworkEquipment', 40, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(75, 'Printer', 40, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(76, 'Monitor', 40, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(77, 'Peripheral', 40, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(78, 'User', 8, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(79, 'Phone', 31, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(80, 'Phone', 23, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(81, 'Phone', 3, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(82, 'Phone', 4, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(83, 'Phone', 40, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(84, 'Phone', 19, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(85, 'Phone', 7, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(86, 'Group', 16, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(87, 'AllAssets', 31, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(88, 'ReservationItem', 4, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(89, 'ReservationItem', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(90, 'Budget', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(91, 'Software', 72, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(92, 'Software', 163, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(93, 'Budget', 5, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(94, 'Budget', 4, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(95, 'Budget', 19, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(96, 'CronTask', 8, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(97, 'CronTask', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(98, 'CronTask', 4, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(99, 'CronTask', 7, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(100, 'RequestType', 14, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(101, 'RequestType', 15, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(102, 'NotificationTemplate', 4, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(103, 'NotificationTemplate', 16, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(104, 'Notification', 5, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(105, 'Notification', 6, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(106, 'Notification', 2, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(107, 'Notification', 4, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(108, 'Notification', 80, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(109, 'Notification', 86, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(110, 'MailCollector', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(111, 'MailCollector', 19, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(112, 'AuthLDAP', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(113, 'AuthLDAP', 19, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(114, 'AuthMail', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(115, 'AuthMail', 19, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(116, 'IPNetwork', 18, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(117, 'WifiNetwork', 10, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(118, 'Profile', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(119, 'Profile', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(120, 'Profile', 19, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(121, 'Transfer', 19, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(122, 'TicketValidation', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(123, 'TicketValidation', 2, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(124, 'TicketValidation', 8, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(125, 'TicketValidation', 4, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(126, 'TicketValidation', 9, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(127, 'TicketValidation', 7, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(128, 'NotImportedEmail', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(129, 'NotImportedEmail', 5, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(130, 'NotImportedEmail', 4, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(131, 'NotImportedEmail', 6, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(132, 'NotImportedEmail', 16, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(133, 'NotImportedEmail', 19, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(134, 'RuleRightParameter', 11, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(135, 'Ticket', 12, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(136, 'Ticket', 19, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(137, 'Ticket', 15, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(138, 'Ticket', 3, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(139, 'Ticket', 4, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(140, 'Ticket', 5, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(141, 'Ticket', 7, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(142, 'Calendar', 19, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(143, 'Holiday', 11, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(144, 'Holiday', 12, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(145, 'Holiday', 13, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(146, 'SLA', 4, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(147, 'Ticket', 18, 8, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(148, 'AuthLDAP', 30, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(149, 'AuthMail', 6, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(150, 'FQDN', 11, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(151, 'FieldUnicity', 1, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(152, 'FieldUnicity', 80, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(153, 'FieldUnicity', 4, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(154, 'FieldUnicity', 3, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(155, 'FieldUnicity', 86, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(156, 'FieldUnicity', 30, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(157, 'Problem', 21, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(158, 'Problem', 12, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(159, 'Problem', 19, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(160, 'Problem', 15, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(161, 'Problem', 3, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(162, 'Problem', 7, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(163, 'Problem', 18, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(164, 'Vlan', 11, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(165, 'TicketRecurrent', 11, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(166, 'TicketRecurrent', 12, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(167, 'TicketRecurrent', 13, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(168, 'TicketRecurrent', 15, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(169, 'TicketRecurrent', 14, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(170, 'Reminder', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(171, 'Reminder', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(172, 'Reminder', 4, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(173, 'Reminder', 5, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(174, 'Reminder', 6, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(175, 'Reminder', 7, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(176, 'IPNetwork', 10, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(177, 'IPNetwork', 11, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(178, 'IPNetwork', 12, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(179, 'IPNetwork', 17, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(180, 'NetworkName', 12, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(181, 'NetworkName', 13, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(182, 'RSSFeed', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(183, 'RSSFeed', 4, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(184, 'RSSFeed', 5, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(185, 'RSSFeed', 19, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(186, 'RSSFeed', 6, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(187, 'RSSFeed', 7, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(188, 'Blacklist', 12, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(189, 'Blacklist', 11, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(190, 'ReservationItem', 5, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(191, 'QueuedNotification', 16, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(192, 'QueuedNotification', 7, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(193, 'QueuedNotification', 20, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(194, 'QueuedNotification', 21, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(195, 'QueuedNotification', 22, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(196, 'QueuedNotification', 15, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(197, 'Change', 12, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(198, 'Change', 19, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(199, 'Change', 15, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(200, 'Change', 7, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(201, 'Change', 18, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(202, 'Project', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(203, 'Project', 4, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(204, 'Project', 12, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(205, 'Project', 5, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(206, 'Project', 15, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(207, 'Project', 21, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(208, 'ProjectState', 12, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(209, 'ProjectState', 11, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(210, 'ProjectTask', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(211, 'ProjectTask', 12, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(212, 'ProjectTask', 14, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(213, 'ProjectTask', 5, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(214, 'ProjectTask', 7, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(215, 'ProjectTask', 8, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(216, 'ProjectTask', 13, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(217, 'CartridgeItem', 9, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(218, 'ConsumableItem', 9, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(219, 'ReservationItem', 9, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(220, 'SoftwareLicense', 1, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(221, 'SoftwareLicense', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(222, 'SoftwareLicense', 10, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(223, 'SoftwareLicense', 162, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(224, 'SoftwareLicense', 5, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(225, 'SavedSearch', 8, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(226, 'SavedSearch', 9, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(227, 'SavedSearch', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(228, 'SavedSearch', 10, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(229, 'SavedSearch', 11, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(230, 'Plugin', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(231, 'Plugin', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(232, 'Plugin', 4, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(233, 'Plugin', 5, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(234, 'Plugin', 6, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(235, 'Plugin', 7, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(236, 'Plugin', 8, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(237, 'Cluster', 31, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(238, 'Cluster', 19, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(239, 'Domain', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(240, 'Domain', 4, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(241, 'Domain', 2, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(242, 'Domain', 6, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(243, 'Domain', 7, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(244, 'DomainRecord', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(245, 'DomainRecord', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(246, 'Appliance', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(247, 'Appliance', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(248, 'Appliance', 4, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(249, 'Appliance', 5, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(250, 'Lockedfield', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(251, 'Lockedfield', 13, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(252, 'Lockedfield', 5, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(253, 'Unmanaged', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(254, 'Unmanaged', 4, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(255, 'Unmanaged', 3, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(256, 'Unmanaged', 5, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(257, 'Unmanaged', 7, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(258, 'Unmanaged', 10, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(259, 'Unmanaged', 18, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(260, 'Unmanaged', 14, 8, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(261, 'Unmanaged', 15, 9, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(262, 'Unmanaged', 9, 10, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(263, 'NetworkPortType', 10, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(264, 'NetworkPortType', 11, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(265, 'NetworkPortType', 12, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(266, 'NetworkPort', 3, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(267, 'NetworkPort', 30, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(268, 'NetworkPort', 31, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(269, 'NetworkPort', 32, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(270, 'NetworkPort', 33, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(271, 'NetworkPort', 34, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(272, 'NetworkPort', 35, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(273, 'NetworkPort', 36, 8, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(274, 'NetworkPort', 38, 9, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(275, 'NetworkPort', 39, 10, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(276, 'NetworkPort', 40, 11, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(277, 'NetworkPort', 6, 12, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(278, 'USBVendor', 10, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(279, 'USBVendor', 11, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(280, 'PCIVendor', 10, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(281, 'PCIVendor', 11, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(282, 'Agent', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(283, 'Agent', 4, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(284, 'Agent', 10, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(285, 'Agent', 8, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(286, 'Agent', 11, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(287, 'Agent', 6, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(288, 'Agent', 15, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(289, 'Database', 2, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(290, 'Database', 3, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(291, 'Database', 6, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(292, 'Database', 9, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(293, 'Database', 10, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(294, 'Glpi\\Socket', 5, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(295, 'Glpi\\Socket', 6, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(296, 'Glpi\\Socket', 9, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(297, 'Glpi\\Socket', 8, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(298, 'Glpi\\Socket', 7, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(299, 'Cable', 4, 1, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(300, 'Cable', 31, 2, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(301, 'Cable', 6, 3, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(302, 'Cable', 15, 4, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(303, 'Cable', 24, 5, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(304, 'Cable', 8, 6, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(305, 'Cable', 10, 7, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(306, 'Cable', 13, 8, 0);
REPLACE INTO `glpi_displaypreferences` (`id`, `itemtype`, `num`, `rank`, `users_id`) VALUES(307, 'Cable', 14, 9, 0);

--
-- Volcado de datos para la tabla `glpi_documenttypes`
--

REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(1, 'JPEG', 'jpg', 'jpg-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(2, 'PNG', 'png', 'png-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(3, 'GIF', 'gif', 'gif-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(4, 'BMP', 'bmp', 'bmp-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(5, 'Photoshop', 'psd', 'psd-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(6, 'TIFF', 'tif', 'tif-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(7, 'AIFF', 'aiff', 'aiff-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(8, 'Windows Media', 'asf', 'asf-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(9, 'Windows Media', 'avi', 'avi-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(10, 'BZip', 'bz2', 'bz2-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(11, 'Word', 'doc', 'doc-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(12, 'DjVu', 'djvu', '', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(13, 'PostScript', 'eps', 'ps-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(14, 'GZ', 'gz', 'gz-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(15, 'HTML', 'html', 'html-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(16, 'Midi', 'mid', 'mid-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(17, 'QuickTime', 'mov', 'mov-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(18, 'MP3', 'mp3', 'mp3-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(19, 'MPEG', 'mpg', 'mpg-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(20, 'Ogg Vorbis', 'ogg', 'ogg-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(21, 'PDF', 'pdf', 'pdf-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(22, 'PowerPoint', 'ppt', 'ppt-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(23, 'PostScript', 'ps', 'ps-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(24, 'QuickTime', 'qt', 'qt-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(25, 'RealAudio', 'ra', 'ra-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(26, 'RealAudio', 'ram', 'ram-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(27, 'RealAudio', 'rm', 'rm-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(28, 'RTF', 'rtf', 'rtf-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(29, 'StarOffice', 'sdd', 'sdd-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(30, 'StarOffice', 'sdw', 'sdw-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(31, 'Stuffit', 'sit', 'sit-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(32, 'OpenOffice Impress', 'sxi', 'sxi-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(33, 'OpenOffice', 'sxw', 'sxw-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(34, 'Flash', 'swf', 'swf-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(35, 'TGZ', 'tgz', 'tgz-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(36, 'texte', 'txt', 'txt-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(37, 'WAV', 'wav', 'wav-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(38, 'Excel', 'xls', 'xls-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(39, 'XML', 'xml', 'xml-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(40, 'Windows Media', 'wmv', 'wmv-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(41, 'Zip', 'zip', 'zip-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(42, 'MNG', 'mng', '', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(43, 'Adobe Illustrator', 'ai', 'ai-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(44, 'C source', 'c', 'c-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(45, 'Debian', 'deb', 'deb-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(46, 'DVI', 'dvi', 'dvi-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(47, 'C header', 'h', 'h-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(48, 'Pascal', 'pas', 'pas-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(49, 'RedHat/Mandrake/SuSE', 'rpm', 'rpm-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(50, 'OpenOffice Calc', 'sxc', 'sxc-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(51, 'LaTeX', 'tex', 'tex-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(52, 'GIMP multi-layer', 'xcf', 'xcf-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(53, 'JPEG', 'jpeg', 'jpg-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(54, 'Oasis Open Office Writer', 'odt', 'odt-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(55, 'Oasis Open Office Calc', 'ods', 'ods-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(56, 'Oasis Open Office Impress', 'odp', 'odp-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(57, 'Oasis Open Office Impress Template', 'otp', 'odp-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(58, 'Oasis Open Office Writer Template', 'ott', 'odt-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(59, 'Oasis Open Office Calc Template', 'ots', 'ods-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(60, 'Oasis Open Office Math', 'odf', 'odf-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(61, 'Oasis Open Office Draw', 'odg', 'odg-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(62, 'Oasis Open Office Draw Template', 'otg', 'odg-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(63, 'Oasis Open Office Base', 'odb', 'odb-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(64, 'Oasis Open Office HTML', 'oth', 'oth-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(65, 'Oasis Open Office Writer Master', 'odm', 'odm-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(66, 'Oasis Open Office Chart', 'odc', '', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(67, 'Oasis Open Office Image', 'odi', '', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(68, 'Word XML', 'docx', 'doc-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(69, 'Excel XML', 'xlsx', 'xls-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(70, 'PowerPoint XML', 'pptx', 'ppt-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(71, 'Comma-Separated Values', 'csv', 'csv-dist.png', NULL, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_documenttypes` (`id`, `name`, `ext`, `icon`, `mime`, `is_uploadable`, `date_mod`, `comment`, `date_creation`) VALUES(72, 'Scalable Vector Graphics', 'svg', 'svg-dist.png', NULL, 1, NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_domainrecordtypes`
--

REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(1, 'A', '[]', 0, 1, 'Host address');
REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(2, 'AAAA', '[]', 0, 1, 'IPv6 host address');
REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(3, 'ALIAS', '[]', 0, 1, 'Auto resolved alias');
REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(4, 'CNAME', '[{\"key\":\"target\",\"label\":\"Target\",\"placeholder\":\"sip.example.com.\",\"is_fqdn\":true}]', 0, 1, 'Canonical name for an alias');
REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(5, 'MX', '[{\"key\":\"priority\",\"label\":\"Priority\",\"placeholder\":\"10\"},{\"key\":\"server\",\"label\":\"Server\",\"placeholder\":\"mail.example.com.\",\"is_fqdn\":true}]', 0, 1, 'Mail eXchange');
REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(6, 'NS', '[]', 0, 1, 'Name Server');
REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(7, 'PTR', '[]', 0, 1, 'Pointer');
REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(8, 'SOA', '[{\"key\":\"primary_name_server\",\"label\":\"Primary name server\",\"placeholder\":\"ns1.example.com.\",\"is_fqdn\":true},{\"key\":\"primary_contact\",\"label\":\"Primary contact\",\"placeholder\":\"admin.example.com.\",\"is_fqdn\":true},{\"key\":\"serial\",\"label\":\"Serial\",\"placeholder\":\"2020010101\"},{\"key\":\"zone_refresh_timer\",\"label\":\"Zone refresh timer\",\"placeholder\":\"86400\"},{\"key\":\"failed_refresh_retry_timer\",\"label\":\"Failed refresh retry timer\",\"placeholder\":\"7200\"},{\"key\":\"zone_expiry_timer\",\"label\":\"Zone expiry timer\",\"placeholder\":\"1209600\"},{\"key\":\"minimum_ttl\",\"label\":\"Minimum TTL\",\"placeholder\":\"300\"}]', 0, 1, 'Start Of Authority');
REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(9, 'SRV', '[{\"key\":\"priority\",\"label\":\"Priority\",\"placeholder\":\"0\"},{\"key\":\"weight\",\"label\":\"Weight\",\"placeholder\":\"10\"},{\"key\":\"port\",\"label\":\"Port\",\"placeholder\":\"5060\"},{\"key\":\"target\",\"label\":\"Target\",\"placeholder\":\"sip.example.com.\",\"is_fqdn\":true}]', 0, 1, 'Location of service');
REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(10, 'TXT', '[{\"key\":\"data\",\"label\":\"TXT record data\",\"placeholder\":\"Your TXT record data\",\"quote_value\":true}]', 0, 1, 'Descriptive text');
REPLACE INTO `glpi_domainrecordtypes` (`id`, `name`, `fields`, `entities_id`, `is_recursive`, `comment`) VALUES(11, 'CAA', '[{\"key\":\"flag\",\"label\":\"Flag\",\"placeholder\":\"0\"},{\"key\":\"tag\",\"label\":\"Tag\",\"placeholder\":\"issue\"},{\"key\":\"value\",\"label\":\"Value\",\"placeholder\":\"letsencrypt.org\",\"quote_value\":true}]', 0, 1, 'Certification Authority Authorization');

--
-- Volcado de datos para la tabla `glpi_domainrelations`
--

REPLACE INTO `glpi_domainrelations` (`id`, `name`, `entities_id`, `is_recursive`, `comment`) VALUES(1, 'Belongs', 0, 1, 'Item belongs to domain');
REPLACE INTO `glpi_domainrelations` (`id`, `name`, `entities_id`, `is_recursive`, `comment`) VALUES(2, 'Manage', 0, 1, 'Item manages domain');

--
-- Volcado de datos para la tabla `glpi_enclosuremodels`
--

REPLACE INTO `glpi_enclosuremodels` (`id`, `name`, `comment`, `product_number`, `weight`, `required_units`, `depth`, `power_connections`, `power_consumption`, `is_half_rack`, `picture_front`, `picture_rear`, `pictures`, `date_mod`, `date_creation`) VALUES(1, 'EnclosureModel1', 'Comment', '123123', 2, 1, 1, 0, 0, 0, NULL, NULL, NULL, '2023-03-19 19:37:11', '2023-03-19 19:37:11');

--
-- Volcado de datos para la tabla `glpi_enclosures`
--

REPLACE INTO `glpi_enclosures` (`id`, `name`, `entities_id`, `is_recursive`, `locations_id`, `serial`, `otherserial`, `enclosuremodels_id`, `users_id_tech`, `groups_id_tech`, `is_template`, `template_name`, `is_deleted`, `orientation`, `power_supplies`, `states_id`, `comment`, `manufacturers_id`, `date_mod`, `date_creation`) VALUES(1, 'Enclosure1', 0, 0, 1, '123123123', '23132323', 1, 0, 0, 0, NULL, 0, NULL, 1, 2, 'Comment', 2, '2023-03-19 19:37:19', '2023-03-19 19:37:19');

--
-- Volcado de datos para la tabla `glpi_entities`
--

REPLACE INTO `glpi_entities` (`id`, `name`, `entities_id`, `completename`, `comment`, `level`, `sons_cache`, `ancestors_cache`, `registration_number`, `address`, `postcode`, `town`, `state`, `country`, `website`, `phonenumber`, `fax`, `email`, `admin_email`, `admin_email_name`, `from_email`, `from_email_name`, `noreply_email`, `noreply_email_name`, `replyto_email`, `replyto_email_name`, `notification_subject_tag`, `ldap_dn`, `tag`, `authldaps_id`, `mail_domain`, `entity_ldapfilter`, `mailing_signature`, `cartridges_alert_repeat`, `consumables_alert_repeat`, `use_licenses_alert`, `send_licenses_alert_before_delay`, `use_certificates_alert`, `send_certificates_alert_before_delay`, `certificates_alert_repeat_interval`, `use_contracts_alert`, `send_contracts_alert_before_delay`, `use_infocoms_alert`, `send_infocoms_alert_before_delay`, `use_reservations_alert`, `use_domains_alert`, `send_domains_alert_close_expiries_delay`, `send_domains_alert_expired_delay`, `autoclose_delay`, `autopurge_delay`, `notclosed_delay`, `calendars_strategy`, `calendars_id`, `auto_assign_mode`, `tickettype`, `max_closedate`, `inquest_config`, `inquest_rate`, `inquest_delay`, `inquest_URL`, `autofill_warranty_date`, `autofill_use_date`, `autofill_buy_date`, `autofill_delivery_date`, `autofill_order_date`, `tickettemplates_strategy`, `tickettemplates_id`, `changetemplates_strategy`, `changetemplates_id`, `problemtemplates_strategy`, `problemtemplates_id`, `entities_strategy_software`, `entities_id_software`, `default_contract_alert`, `default_infocom_alert`, `default_cartridges_alarm_threshold`, `default_consumables_alarm_threshold`, `delay_send_emails`, `is_notif_enable_default`, `inquest_duration`, `date_mod`, `date_creation`, `autofill_decommission_date`, `suppliers_as_private`, `anonymize_support_agents`, `display_users_initials`, `contracts_strategy_default`, `contracts_id_default`, `enable_custom_css`, `custom_css_code`, `latitude`, `longitude`, `altitude`, `transfers_strategy`, `transfers_id`, `agent_base_url`) VALUES(0, 'Root Entity', NULL, 'Root Entity', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -2, -2, -10, -10, 0, 0, 0, -10, 1, NULL, 1, 0, 0, NULL, '0', '0', '0', '0', '0', 0, 1, 0, 1, 0, 1, -10, 0, 0, 0, 10, 10, 0, 1, 0, NULL, NULL, '0', 0, 0, 1, 0, 0, 0, NULL, NULL, NULL, NULL, 0, 0, NULL);

--
-- Volcado de datos para la tabla `glpi_events`
--

REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(1, 0, 'system', '2023-03-17 19:47:56', 'login', 3, ' は IP: ::1 からのログインに失敗しました');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(2, 0, 'system', '2023-03-19 19:12:54', 'login', 3, 'glpi は IP: ::1 からログインしました');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(3, 1, 'Location', '2023-03-19 19:14:30', 'setup', 4, 'glpi adds the item Cordoba');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(4, 2, 'Location', '2023-03-19 19:14:48', 'setup', 4, 'glpi adds the item Trelew');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(5, 1, 'State', '2023-03-19 19:15:09', 'setup', 4, 'glpi adds the item Live');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(6, 2, 'State', '2023-03-19 19:15:14', 'setup', 4, 'glpi adds the item Down');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(7, 1, 'ComputerType', '2023-03-19 19:15:32', 'setup', 4, 'glpi adds the item PC');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(8, 2, 'ComputerType', '2023-03-19 19:15:36', 'setup', 4, 'glpi adds the item Laptop');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(9, 3, 'ComputerType', '2023-03-19 19:15:46', 'setup', 4, 'glpi adds the item All-In-One');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(10, 1, 'Manufacturer', '2023-03-19 19:15:55', 'setup', 4, 'glpi adds the item Lenovo');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(11, 2, 'Manufacturer', '2023-03-19 19:16:00', 'setup', 4, 'glpi adds the item ASUS');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(12, 3, 'Manufacturer', '2023-03-19 19:16:03', 'setup', 4, 'glpi adds the item MSI');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(13, 4, 'Manufacturer', '2023-03-19 19:16:09', 'setup', 4, 'glpi adds the item HP');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(14, 1, 'ComputerModel', '2023-03-19 19:16:21', 'setup', 4, 'glpi adds the item ComputerModel1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(15, 2, 'ComputerModel', '2023-03-19 19:16:45', 'setup', 4, 'glpi adds the item ComputerModel2');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(16, 1, 'Network', '2023-03-19 19:17:17', 'setup', 4, 'glpi adds the item Network1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(17, 1, 'AutoUpdateSystem', '2023-03-19 19:17:29', 'setup', 4, 'glpi adds the item UpdateSource1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(18, 1, 'computers', '2023-03-19 19:17:32', 'inventory', 4, 'glpi adds the item Computer1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(19, 1, 'MonitorType', '2023-03-19 19:18:13', 'setup', 4, 'glpi adds the item MonitorType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(20, 1, 'MonitorModel', '2023-03-19 19:18:35', 'setup', 4, 'glpi adds the item MonitorModel');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(21, 1, 'monitors', '2023-03-19 19:18:51', 'inventory', 4, 'glpi adds the item Monitor1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(22, 1, 'software', '2023-03-19 19:20:51', 'inventory', 4, 'glpi adds the item Software1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(23, 2, 'software', '2023-03-19 19:21:10', 'inventory', 4, 'glpi adds the item Software2');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(24, 1, 'NetworkEquipmentType', '2023-03-19 19:25:10', 'setup', 4, 'glpi adds the item NetEquipmentType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(25, 1, 'NetworkEquipmentModel', '2023-03-19 19:26:05', 'setup', 4, 'glpi adds the item NetEquipmentModel1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(26, 1, 'networkequipment', '2023-03-19 19:26:16', 'inventory', 4, 'glpi adds the item NetworkDevice1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(27, 1, 'PeripheralType', '2023-03-19 19:27:28', 'setup', 4, 'glpi adds the item DeviceType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(28, 1, 'PeripheralModel', '2023-03-19 19:27:47', 'setup', 4, 'glpi adds the item Model1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(29, 1, 'peripherals', '2023-03-19 19:28:09', 'inventory', 4, 'glpi adds the item Device1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(30, 1, 'PrinterType', '2023-03-19 19:31:02', 'setup', 4, 'glpi adds the item PrinterType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(31, 1, 'PrinterModel', '2023-03-19 19:31:19', 'setup', 4, 'glpi adds the item PrinterModel1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(32, 1, 'printers', '2023-03-19 19:31:53', 'inventory', 4, 'glpi adds the item printer1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(33, 1, 'CartridgeItemType', '2023-03-19 19:33:01', 'setup', 4, 'glpi adds the item CartridgeType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(34, 1, 'cartridgeitems', '2023-03-19 19:33:19', 'inventory', 4, 'glpi adds the item CartridgeCon2horasdesueno');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(35, 1, 'ConsumableItemType', '2023-03-19 19:33:44', 'setup', 4, 'glpi adds the item asdsadasdas');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(36, 1, 'consumableitems', '2023-03-19 19:33:56', 'inventory', 4, 'glpi adds the item ConsumableKindOfModelProbably');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(37, 1, 'PhoneType', '2023-03-19 19:34:27', 'setup', 4, 'glpi adds the item PhoneType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(38, 1, 'PhoneModel', '2023-03-19 19:34:41', 'setup', 4, 'glpi adds the item PhoneModel1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(39, 1, 'PhonePowerSupply', '2023-03-19 19:35:12', 'setup', 4, 'glpi adds the item PhonePowerSupply1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(40, 1, 'phones', '2023-03-19 19:35:19', 'inventory', 4, 'glpi adds the item Phone1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(41, 1, 'RackType', '2023-03-19 19:35:43', 'setup', 4, 'glpi adds the item RackType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(42, 1, 'RackModel', '2023-03-19 19:35:56', 'setup', 4, 'glpi adds the item RackModel1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(43, 1, 'dcrooms', '2023-03-19 19:36:19', 'inventory', 4, 'glpi adds the item ServerRoom1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(44, 1, 'racks', '2023-03-19 19:36:30', 'inventory', 4, 'glpi adds the item Rack1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(45, 1, 'EnclosureModel', '2023-03-19 19:37:11', 'setup', 4, 'glpi adds the item EnclosureModel1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(46, 1, 'enclosure', '2023-03-19 19:37:19', 'inventory', 4, 'glpi adds the item Enclosure1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(47, 1, 'PDUType', '2023-03-19 19:37:48', 'setup', 4, 'glpi adds the item PduType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(48, 1, 'PDUModel', '2023-03-19 19:38:01', 'setup', 4, 'glpi adds the item PduModel1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(49, 1, 'pdus', '2023-03-19 19:38:06', 'inventory', 4, 'glpi adds the item Pdu1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(50, 1, 'PassiveDCEquipmentType', '2023-03-19 19:38:31', 'setup', 4, 'glpi adds the item PassiveDcType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(51, 1, 'PassiveDCEquipmentModel', '2023-03-19 19:38:51', 'setup', 4, 'glpi adds the item PassiveDcModel1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(52, 1, 'passivedcequipment', '2023-03-19 19:38:56', 'inventory', 4, 'glpi adds the item PassiveDc1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(53, 1, 'CableType', '2023-03-19 19:39:17', 'setup', 4, 'glpi adds the item CableType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(54, 1, 'CableStrand', '2023-03-19 19:39:31', 'setup', 4, 'glpi adds the item CableStrand1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(55, 1, 'Glpi\\SocketModel', '2023-03-19 19:39:44', 'setup', 4, 'glpi adds the item Socket1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(56, 2, 'Glpi\\SocketModel', '2023-03-19 19:40:04', 'setup', 4, 'glpi adds the item SocketModel1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(57, 1, 'Computer', '2023-03-19 19:40:20', 'socket', 4, 'glpi adds a socket');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(58, 1, 'cable', '2023-03-19 19:40:27', 'management', 4, 'glpi adds the item Cable1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(59, 1, 'DeviceSimcard', '2023-03-19 19:40:50', 'inventory', 4, 'glpi adds the item SimcardComponent');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(60, 1, 'LineType', '2023-03-19 19:41:13', 'setup', 4, 'glpi adds the item LineType1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(61, 1, 'LineOperator', '2023-03-19 19:41:26', 'setup', 4, 'glpi adds the item LineOperator1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(62, 1, 'lines', '2023-03-19 19:41:29', 'financial', 4, 'glpi adds the item Line1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(63, 1, 'OperatingSystem', '2023-03-19 19:42:10', 'setup', 4, 'glpi adds the item Windows11');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(64, 1, 'OperatingSystemArchitecture', '2023-03-19 19:42:18', 'setup', 4, 'glpi adds the item Arch1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(65, 1, 'OperatingSystemKernelVersion', '2023-03-19 19:42:25', 'setup', 4, 'glpi adds the item Kernel1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(66, 1, 'OperatingSystemVersion', '2023-03-19 19:42:33', 'setup', 4, 'glpi adds the item 1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(67, 1, 'OperatingSystemServicePack', '2023-03-19 19:42:47', 'setup', 4, 'glpi adds the item SvcPack1');
REPLACE INTO `glpi_events` (`id`, `items_id`, `type`, `date`, `service`, `level`, `message`) VALUES(68, 1, 'OperatingSystemEdition', '2023-03-19 19:42:58', 'setup', 4, 'glpi adds the item Edition1');

--
-- Volcado de datos para la tabla `glpi_filesystems`
--

REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'ext', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'ext2', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(3, 'ext3', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(4, 'ext4', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(5, 'FAT', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(6, 'FAT32', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(7, 'VFAT', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(8, 'HFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(9, 'HPFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(10, 'HTFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(11, 'JFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(12, 'JFS2', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(13, 'NFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(14, 'NTFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(15, 'ReiserFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(16, 'SMBFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(17, 'UDF', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(18, 'UFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(19, 'XFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(20, 'ZFS', NULL, NULL, NULL);
REPLACE INTO `glpi_filesystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(21, 'APFS', NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_interfacetypes`
--

REPLACE INTO `glpi_interfacetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'IDE', NULL, NULL, NULL);
REPLACE INTO `glpi_interfacetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'SATA', NULL, NULL, NULL);
REPLACE INTO `glpi_interfacetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(3, 'SCSI', NULL, NULL, NULL);
REPLACE INTO `glpi_interfacetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(4, 'USB', NULL, NULL, NULL);
REPLACE INTO `glpi_interfacetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(5, 'AGP', NULL, NULL, NULL);
REPLACE INTO `glpi_interfacetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(6, 'PCI', NULL, NULL, NULL);
REPLACE INTO `glpi_interfacetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(7, 'PCIe', NULL, NULL, NULL);
REPLACE INTO `glpi_interfacetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(8, 'PCI-X', NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_items_operatingsystems`
--

REPLACE INTO `glpi_items_operatingsystems` (`id`, `items_id`, `itemtype`, `operatingsystems_id`, `operatingsystemversions_id`, `operatingsystemservicepacks_id`, `operatingsystemarchitectures_id`, `operatingsystemkernelversions_id`, `license_number`, `licenseid`, `operatingsystemeditions_id`, `date_mod`, `date_creation`, `is_deleted`, `is_dynamic`, `entities_id`, `is_recursive`, `install_date`) VALUES(1, 1, 'Computer', 1, 1, 1, 1, 1, '123123123123', 'IDPRODUCT', 1, '2023-03-19 19:43:01', '2023-03-19 19:43:01', 0, 0, 0, 0, NULL);

--
-- Volcado de datos para la tabla `glpi_lineoperators`
--

REPLACE INTO `glpi_lineoperators` (`id`, `name`, `comment`, `mcc`, `mnc`, `entities_id`, `is_recursive`, `date_mod`, `date_creation`) VALUES(1, 'LineOperator1', 'Comment', 0, 0, 0, 0, '2023-03-19 19:41:26', '2023-03-19 19:41:26');

--
-- Volcado de datos para la tabla `glpi_lines`
--

REPLACE INTO `glpi_lines` (`id`, `name`, `entities_id`, `is_recursive`, `is_deleted`, `caller_num`, `caller_name`, `users_id`, `groups_id`, `lineoperators_id`, `locations_id`, `states_id`, `linetypes_id`, `date_creation`, `date_mod`, `comment`) VALUES(1, 'Line1', 0, 0, 0, '123123', '123123', 0, 0, 1, 1, 2, 1, '2023-03-19 19:41:29', '2023-03-19 19:41:29', '123123');

--
-- Volcado de datos para la tabla `glpi_linetypes`
--

REPLACE INTO `glpi_linetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'LineType1', '123123123', '2023-03-19 19:41:13', '2023-03-19 19:41:13');

--
-- Volcado de datos para la tabla `glpi_locations`
--

REPLACE INTO `glpi_locations` (`id`, `entities_id`, `is_recursive`, `name`, `locations_id`, `completename`, `comment`, `level`, `ancestors_cache`, `sons_cache`, `address`, `postcode`, `town`, `state`, `country`, `building`, `room`, `latitude`, `longitude`, `altitude`, `date_mod`, `date_creation`) VALUES(1, 0, 0, 'Cordoba', 0, 'Cordoba', '', 1, '[]', NULL, '', 'x5000', 'Cordoba', '', '', '', '', '', '', '', '2023-03-19 19:14:30', '2023-03-19 19:14:30');
REPLACE INTO `glpi_locations` (`id`, `entities_id`, `is_recursive`, `name`, `locations_id`, `completename`, `comment`, `level`, `ancestors_cache`, `sons_cache`, `address`, `postcode`, `town`, `state`, `country`, `building`, `room`, `latitude`, `longitude`, `altitude`, `date_mod`, `date_creation`) VALUES(2, 0, 0, 'Trelew', 0, 'Trelew', '', 1, '[]', NULL, '', '9100', 'Trelew', 'Chubut', 'Argentina', '', '', '', '', '', '2023-03-19 19:14:48', '2023-03-19 19:14:48');

--
-- Volcado de datos para la tabla `glpi_logs`
--

REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(1, 'RuleImportAsset', 1, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(2, 'RuleImportAsset', 1, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Is partial is Yes (1)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(3, 'RuleCriteria', 1, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(4, 'RuleImportAsset', 1, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type does not exist Yes (2)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(5, 'RuleCriteria', 2, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(6, 'RuleImportAsset', 1, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (1)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(7, 'RuleAction', 1, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(8, 'RuleImportAsset', 2, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(9, 'RuleImportAsset', 2, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type does not exist Yes (3)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(10, 'RuleCriteria', 3, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(11, 'RuleImportAsset', 2, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC is already present Yes (4)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(12, 'RuleCriteria', 4, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(13, 'RuleImportAsset', 2, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (5)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(14, 'RuleCriteria', 5, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(15, 'RuleImportAsset', 2, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; Port number is already present Yes (6)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(16, 'RuleCriteria', 6, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(17, 'RuleImportAsset', 2, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; Port number exists Yes (7)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(18, 'RuleCriteria', 7, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(19, 'RuleImportAsset', 2, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'General &#62; Restrict criteria to the same network port Yes Yes (8)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(20, 'RuleCriteria', 8, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(21, 'RuleImportAsset', 2, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (2)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(22, 'RuleAction', 2, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(23, 'RuleImportAsset', 3, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(24, 'RuleImportAsset', 3, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type does not exist Yes (9)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(25, 'RuleCriteria', 9, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(26, 'RuleImportAsset', 3, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC is already present Yes (10)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(27, 'RuleCriteria', 10, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(28, 'RuleImportAsset', 3, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (11)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(29, 'RuleCriteria', 11, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(30, 'RuleImportAsset', 3, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; Port number is already present Yes (12)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(31, 'RuleCriteria', 12, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(32, 'RuleImportAsset', 3, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; Port number exists Yes (13)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(33, 'RuleCriteria', 13, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(34, 'RuleImportAsset', 3, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (3)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(35, 'RuleAction', 3, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(36, 'RuleImportAsset', 4, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(37, 'RuleImportAsset', 4, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type does not exist Yes (14)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(38, 'RuleCriteria', 14, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(39, 'RuleImportAsset', 4, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (15)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(40, 'RuleCriteria', 15, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(41, 'RuleImportAsset', 4, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; Port number exists Yes (16)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(42, 'RuleCriteria', 16, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(43, 'RuleImportAsset', 4, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (4)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(44, 'RuleAction', 4, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(45, 'RuleImportAsset', 5, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(46, 'RuleImportAsset', 5, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type does not exist Yes (17)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(47, 'RuleCriteria', 17, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(48, 'RuleImportAsset', 5, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; IP is already present Yes (18)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(49, 'RuleCriteria', 18, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(50, 'RuleImportAsset', 5, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; IP exists Yes (19)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(51, 'RuleCriteria', 19, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(52, 'RuleImportAsset', 5, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; Port description is already present Yes (20)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(53, 'RuleCriteria', 20, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(54, 'RuleImportAsset', 5, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; Port description exists Yes (21)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(55, 'RuleCriteria', 21, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(56, 'RuleImportAsset', 5, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'General &#62; Restrict criteria to the same network port Yes Yes (22)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(57, 'RuleCriteria', 22, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(58, 'RuleImportAsset', 5, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (5)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(59, 'RuleAction', 5, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(60, 'RuleImportAsset', 6, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(61, 'RuleImportAsset', 6, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type does not exist Yes (23)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(62, 'RuleCriteria', 23, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(63, 'RuleImportAsset', 6, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; IP is already present Yes (24)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(64, 'RuleCriteria', 24, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(65, 'RuleImportAsset', 6, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; IP exists Yes (25)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(66, 'RuleCriteria', 25, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(67, 'RuleImportAsset', 6, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; Port description is already present Yes (26)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(68, 'RuleCriteria', 26, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(69, 'RuleImportAsset', 6, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; Port description exists Yes (27)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(70, 'RuleCriteria', 27, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(71, 'RuleImportAsset', 6, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (6)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(72, 'RuleAction', 6, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(73, 'RuleImportAsset', 7, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(74, 'RuleImportAsset', 7, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type does not exist Yes (28)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(75, 'RuleCriteria', 28, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(76, 'RuleImportAsset', 7, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; IP exists Yes (29)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(77, 'RuleCriteria', 29, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(78, 'RuleImportAsset', 7, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; Port description exists Yes (30)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(79, 'RuleCriteria', 30, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(80, 'RuleImportAsset', 7, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (7)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(81, 'RuleAction', 7, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(82, 'RuleImportAsset', 8, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(83, 'RuleImportAsset', 8, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type does not exist Yes (31)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(84, 'RuleCriteria', 31, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(85, 'RuleImportAsset', 8, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC is already present Yes (32)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(86, 'RuleCriteria', 32, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(87, 'RuleImportAsset', 8, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (33)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(88, 'RuleCriteria', 33, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(89, 'RuleImportAsset', 8, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'General &#62; Only criteria of this rule is in data Yes Yes (34)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(90, 'RuleCriteria', 34, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(91, 'RuleImportAsset', 8, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (8)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(92, 'RuleAction', 8, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(93, 'RuleImportAsset', 9, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(94, 'RuleImportAsset', 9, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type does not exist Yes (35)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(95, 'RuleCriteria', 35, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(96, 'RuleImportAsset', 9, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (36)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(97, 'RuleCriteria', 36, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(98, 'RuleImportAsset', 9, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'General &#62; Only criteria of this rule is in data Yes Yes (37)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(99, 'RuleCriteria', 37, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(100, 'RuleImportAsset', 9, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (9)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(101, 'RuleAction', 9, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(102, 'RuleImportAsset', 10, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(103, 'RuleImportAsset', 10, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (38)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(104, 'RuleCriteria', 38, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(105, 'RuleImportAsset', 10, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name does not exist Yes (39)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(106, 'RuleCriteria', 39, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(107, 'RuleImportAsset', 10, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (10)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(108, 'RuleAction', 10, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(109, 'RuleImportAsset', 11, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(110, 'RuleImportAsset', 11, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (40)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(111, 'RuleCriteria', 40, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(112, 'RuleImportAsset', 11, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number is already present Yes (41)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(113, 'RuleCriteria', 41, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(114, 'RuleImportAsset', 11, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (42)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(115, 'RuleCriteria', 42, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(116, 'RuleImportAsset', 11, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; UUID is already present Yes (43)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(117, 'RuleCriteria', 43, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(118, 'RuleImportAsset', 11, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; UUID exists Yes (44)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(119, 'RuleCriteria', 44, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(120, 'RuleImportAsset', 11, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (11)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(121, 'RuleAction', 11, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(122, 'RuleImportAsset', 12, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(123, 'RuleImportAsset', 12, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (45)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(124, 'RuleCriteria', 45, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(125, 'RuleImportAsset', 12, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number is already present Yes (46)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(126, 'RuleCriteria', 46, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(127, 'RuleImportAsset', 12, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (47)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(128, 'RuleCriteria', 47, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(129, 'RuleImportAsset', 12, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; UUID is empty Yes (48)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(130, 'RuleCriteria', 48, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(131, 'RuleImportAsset', 12, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (12)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(132, 'RuleAction', 12, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(133, 'RuleImportAsset', 13, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(134, 'RuleImportAsset', 13, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (49)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(135, 'RuleCriteria', 49, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(136, 'RuleImportAsset', 13, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; UUID exists Yes (50)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(137, 'RuleCriteria', 50, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(138, 'RuleImportAsset', 13, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (51)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(139, 'RuleCriteria', 51, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(140, 'RuleImportAsset', 13, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (13)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(141, 'RuleAction', 13, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(142, 'RuleImportAsset', 14, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(143, 'RuleImportAsset', 14, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (52)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(144, 'RuleCriteria', 52, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(145, 'RuleImportAsset', 14, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number is already present Yes (53)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(146, 'RuleCriteria', 53, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(147, 'RuleImportAsset', 14, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (54)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(148, 'RuleCriteria', 54, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(149, 'RuleImportAsset', 14, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (14)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(150, 'RuleAction', 14, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(151, 'RuleImportAsset', 15, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(152, 'RuleImportAsset', 15, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (55)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(153, 'RuleCriteria', 55, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(154, 'RuleImportAsset', 15, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; UUID is already present Yes (56)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(155, 'RuleCriteria', 56, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(156, 'RuleImportAsset', 15, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; UUID exists Yes (57)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(157, 'RuleCriteria', 57, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(158, 'RuleImportAsset', 15, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (15)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(159, 'RuleAction', 15, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(160, 'RuleImportAsset', 16, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(161, 'RuleImportAsset', 16, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (58)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(162, 'RuleCriteria', 58, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(163, 'RuleImportAsset', 16, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC is already present Yes (59)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(164, 'RuleCriteria', 59, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(165, 'RuleImportAsset', 16, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (60)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(166, 'RuleCriteria', 60, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(167, 'RuleImportAsset', 16, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (16)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(168, 'RuleAction', 16, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(169, 'RuleImportAsset', 17, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(170, 'RuleImportAsset', 17, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (61)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(171, 'RuleCriteria', 61, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(172, 'RuleImportAsset', 17, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name is already present Yes (62)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(173, 'RuleCriteria', 62, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(174, 'RuleImportAsset', 17, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name exists Yes (63)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(175, 'RuleCriteria', 63, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(176, 'RuleImportAsset', 17, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (17)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(177, 'RuleAction', 17, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(178, 'RuleImportAsset', 18, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(179, 'RuleImportAsset', 18, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (64)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(180, 'RuleCriteria', 64, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(181, 'RuleImportAsset', 18, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (65)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(182, 'RuleCriteria', 65, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(183, 'RuleImportAsset', 18, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (18)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(184, 'RuleAction', 18, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(185, 'RuleImportAsset', 19, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(186, 'RuleImportAsset', 19, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (66)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(187, 'RuleCriteria', 66, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(188, 'RuleImportAsset', 19, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; UUID exists Yes (67)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(189, 'RuleCriteria', 67, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(190, 'RuleImportAsset', 19, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (19)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(191, 'RuleAction', 19, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(192, 'RuleImportAsset', 20, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(193, 'RuleImportAsset', 20, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (68)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(194, 'RuleCriteria', 68, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(195, 'RuleImportAsset', 20, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (69)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(196, 'RuleCriteria', 69, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(197, 'RuleImportAsset', 20, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (20)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(198, 'RuleAction', 20, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(199, 'RuleImportAsset', 21, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(200, 'RuleImportAsset', 21, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (70)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(201, 'RuleCriteria', 70, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(202, 'RuleImportAsset', 21, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name exists Yes (71)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(203, 'RuleCriteria', 71, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(204, 'RuleImportAsset', 21, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (21)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(205, 'RuleAction', 21, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(206, 'RuleImportAsset', 22, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(207, 'RuleImportAsset', 22, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Computers (72)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(208, 'RuleCriteria', 72, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(209, 'RuleImportAsset', 22, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (22)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(210, 'RuleAction', 22, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(211, 'RuleImportAsset', 23, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(212, 'RuleImportAsset', 23, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Printers (73)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(213, 'RuleCriteria', 73, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(214, 'RuleImportAsset', 23, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name does not exist Yes (74)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(215, 'RuleCriteria', 74, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(216, 'RuleImportAsset', 23, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (23)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(217, 'RuleAction', 23, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(218, 'RuleImportAsset', 24, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(219, 'RuleImportAsset', 24, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Printers (75)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(220, 'RuleCriteria', 75, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(221, 'RuleImportAsset', 24, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (76)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(222, 'RuleCriteria', 76, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(223, 'RuleImportAsset', 24, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number is already present Yes (77)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(224, 'RuleCriteria', 77, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(225, 'RuleImportAsset', 24, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (24)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(226, 'RuleAction', 24, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(227, 'RuleImportAsset', 25, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(228, 'RuleImportAsset', 25, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Printers (78)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(229, 'RuleCriteria', 78, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(230, 'RuleImportAsset', 25, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (79)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(231, 'RuleCriteria', 79, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(232, 'RuleImportAsset', 25, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC is already present Yes (80)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(233, 'RuleCriteria', 80, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(234, 'RuleImportAsset', 25, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (25)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(235, 'RuleAction', 25, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(236, 'RuleImportAsset', 26, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(237, 'RuleImportAsset', 26, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Printers (81)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(238, 'RuleCriteria', 81, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(239, 'RuleImportAsset', 26, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (82)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(240, 'RuleCriteria', 82, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(241, 'RuleImportAsset', 26, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (26)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(242, 'RuleAction', 26, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(243, 'RuleImportAsset', 27, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(244, 'RuleImportAsset', 27, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Printers (83)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(245, 'RuleCriteria', 83, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(246, 'RuleImportAsset', 27, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (84)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(247, 'RuleCriteria', 84, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(248, 'RuleImportAsset', 27, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (27)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(249, 'RuleAction', 27, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(250, 'RuleImportAsset', 28, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(251, 'RuleImportAsset', 28, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Printers (85)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(252, 'RuleCriteria', 85, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(253, 'RuleImportAsset', 28, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (28)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(254, 'RuleAction', 28, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(255, 'RuleImportAsset', 29, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(256, 'RuleImportAsset', 29, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Network devices (86)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(257, 'RuleCriteria', 86, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(258, 'RuleImportAsset', 29, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name does not exist Yes (87)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(259, 'RuleCriteria', 87, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(260, 'RuleImportAsset', 29, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (29)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(261, 'RuleAction', 29, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(262, 'RuleImportAsset', 30, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(263, 'RuleImportAsset', 30, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Network devices (88)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(264, 'RuleCriteria', 88, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(265, 'RuleImportAsset', 30, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (89)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(266, 'RuleCriteria', 89, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(267, 'RuleImportAsset', 30, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number is already present Yes (90)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(268, 'RuleCriteria', 90, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(269, 'RuleImportAsset', 30, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (30)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(270, 'RuleAction', 30, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(271, 'RuleImportAsset', 31, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(272, 'RuleImportAsset', 31, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Network devices (91)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(273, 'RuleCriteria', 91, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(274, 'RuleImportAsset', 31, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (92)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(275, 'RuleCriteria', 92, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(276, 'RuleImportAsset', 31, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC is already present Yes (93)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(277, 'RuleCriteria', 93, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(278, 'RuleImportAsset', 31, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (31)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(279, 'RuleAction', 31, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(280, 'RuleImportAsset', 32, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(281, 'RuleImportAsset', 32, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Network devices (94)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(282, 'RuleCriteria', 94, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(283, 'RuleImportAsset', 32, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (95)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(284, 'RuleCriteria', 95, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(285, 'RuleImportAsset', 32, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (32)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(286, 'RuleAction', 32, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(287, 'RuleImportAsset', 33, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(288, 'RuleImportAsset', 33, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Network devices (96)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(289, 'RuleCriteria', 96, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(290, 'RuleImportAsset', 33, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (97)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(291, 'RuleCriteria', 97, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(292, 'RuleImportAsset', 33, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (33)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(293, 'RuleAction', 33, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(294, 'RuleImportAsset', 34, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(295, 'RuleImportAsset', 34, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Network devices (98)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(296, 'RuleCriteria', 98, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(297, 'RuleImportAsset', 34, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (34)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(298, 'RuleAction', 34, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(299, 'RuleImportAsset', 35, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(300, 'RuleImportAsset', 35, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Devices (99)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(301, 'RuleCriteria', 99, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(302, 'RuleImportAsset', 35, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (100)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(303, 'RuleCriteria', 100, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(304, 'RuleImportAsset', 35, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number is already present Yes (101)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(305, 'RuleCriteria', 101, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(306, 'RuleImportAsset', 35, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (35)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(307, 'RuleAction', 35, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(308, 'RuleImportAsset', 36, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(309, 'RuleImportAsset', 36, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Devices (102)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(310, 'RuleCriteria', 102, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(311, 'RuleImportAsset', 36, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (103)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(312, 'RuleCriteria', 103, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(313, 'RuleImportAsset', 36, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (36)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(314, 'RuleAction', 36, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(315, 'RuleImportAsset', 37, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(316, 'RuleImportAsset', 37, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Devices (104)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(317, 'RuleCriteria', 104, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(318, 'RuleImportAsset', 37, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (37)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(319, 'RuleAction', 37, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(320, 'RuleImportAsset', 38, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(321, 'RuleImportAsset', 38, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Monitors (105)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(322, 'RuleCriteria', 105, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(323, 'RuleImportAsset', 38, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (106)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(324, 'RuleCriteria', 106, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(325, 'RuleImportAsset', 38, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number is already present Yes (107)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(326, 'RuleCriteria', 107, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(327, 'RuleImportAsset', 38, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (38)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(328, 'RuleAction', 38, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(329, 'RuleImportAsset', 39, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(330, 'RuleImportAsset', 39, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Monitors (108)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(331, 'RuleCriteria', 108, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(332, 'RuleImportAsset', 39, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (109)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(333, 'RuleCriteria', 109, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(334, 'RuleImportAsset', 39, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (39)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(335, 'RuleAction', 39, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(336, 'RuleImportAsset', 40, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(337, 'RuleImportAsset', 40, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Monitors (110)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(338, 'RuleCriteria', 110, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(339, 'RuleImportAsset', 40, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (40)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(340, 'RuleAction', 40, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(341, 'RuleImportAsset', 41, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(342, 'RuleImportAsset', 41, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Phones (111)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(343, 'RuleCriteria', 111, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(344, 'RuleImportAsset', 41, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name does not exist Yes (112)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(345, 'RuleCriteria', 112, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(346, 'RuleImportAsset', 41, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (41)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(347, 'RuleAction', 41, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(348, 'RuleImportAsset', 42, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(349, 'RuleImportAsset', 42, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Phones (113)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(350, 'RuleCriteria', 113, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(351, 'RuleImportAsset', 42, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC is already present Yes (114)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(352, 'RuleCriteria', 114, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(353, 'RuleImportAsset', 42, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (115)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(354, 'RuleCriteria', 115, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(355, 'RuleImportAsset', 42, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (42)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(356, 'RuleAction', 42, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(357, 'RuleImportAsset', 43, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(358, 'RuleImportAsset', 43, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Phones (116)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(359, 'RuleCriteria', 116, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(360, 'RuleImportAsset', 43, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (117)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(361, 'RuleCriteria', 117, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(362, 'RuleImportAsset', 43, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (43)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(363, 'RuleAction', 43, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(364, 'RuleImportAsset', 44, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(365, 'RuleImportAsset', 44, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Phones (118)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(366, 'RuleCriteria', 118, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(367, 'RuleImportAsset', 44, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (44)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(368, 'RuleAction', 44, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(369, 'RuleImportAsset', 45, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(370, 'RuleImportAsset', 45, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Clusters (119)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(371, 'RuleCriteria', 119, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(372, 'RuleImportAsset', 45, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; UUID exists Yes (120)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(373, 'RuleCriteria', 120, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(374, 'RuleImportAsset', 45, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; UUID is already present Yes (121)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(375, 'RuleCriteria', 121, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(376, 'RuleImportAsset', 45, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (45)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(377, 'RuleAction', 45, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(378, 'RuleImportAsset', 46, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(379, 'RuleImportAsset', 46, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Clusters (122)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(380, 'RuleCriteria', 122, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(381, 'RuleImportAsset', 46, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; UUID exists Yes (123)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(382, 'RuleCriteria', 123, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(383, 'RuleImportAsset', 46, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (46)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(384, 'RuleAction', 46, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(385, 'RuleImportAsset', 47, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(386, 'RuleImportAsset', 47, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Clusters (124)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(387, 'RuleCriteria', 124, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(388, 'RuleImportAsset', 47, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (47)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(389, 'RuleAction', 47, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(390, 'RuleImportAsset', 48, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(391, 'RuleImportAsset', 48, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Enclosures (125)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(392, 'RuleCriteria', 125, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(393, 'RuleImportAsset', 48, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (126)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(394, 'RuleCriteria', 126, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(395, 'RuleImportAsset', 48, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number is already present Yes (127)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(396, 'RuleCriteria', 127, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(397, 'RuleImportAsset', 48, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (48)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(398, 'RuleAction', 48, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(399, 'RuleImportAsset', 49, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(400, 'RuleImportAsset', 49, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Enclosures (128)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(401, 'RuleCriteria', 128, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(402, 'RuleImportAsset', 49, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (129)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(403, 'RuleCriteria', 129, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(404, 'RuleImportAsset', 49, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (49)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(405, 'RuleAction', 49, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(406, 'RuleImportAsset', 50, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(407, 'RuleImportAsset', 50, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Enclosures (130)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(408, 'RuleCriteria', 130, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(409, 'RuleImportAsset', 50, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (50)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(410, 'RuleAction', 50, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(411, 'RuleImportAsset', 51, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(412, 'RuleImportAsset', 51, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name does not exist Yes (131)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(413, 'RuleCriteria', 131, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(414, 'RuleImportAsset', 51, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (51)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(415, 'RuleAction', 51, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(416, 'RuleImportAsset', 52, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(417, 'RuleImportAsset', 52, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (132)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(418, 'RuleCriteria', 132, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(419, 'RuleImportAsset', 52, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number is already present Yes (133)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(420, 'RuleCriteria', 133, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(421, 'RuleImportAsset', 52, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (52)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(422, 'RuleAction', 52, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(423, 'RuleImportAsset', 53, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(424, 'RuleImportAsset', 53, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (134)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(425, 'RuleCriteria', 134, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(426, 'RuleImportAsset', 53, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC is already present Yes (135)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(427, 'RuleCriteria', 135, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(428, 'RuleImportAsset', 53, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (53)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(429, 'RuleAction', 53, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(430, 'RuleImportAsset', 54, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(431, 'RuleImportAsset', 54, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Serial Number exists Yes (136)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(432, 'RuleCriteria', 136, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(433, 'RuleImportAsset', 54, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (54)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(434, 'RuleAction', 54, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(435, 'RuleImportAsset', 55, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(436, 'RuleImportAsset', 55, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Network Port &#62; MAC exists Yes (137)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(437, 'RuleCriteria', 137, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(438, 'RuleImportAsset', 55, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (55)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(439, 'RuleAction', 55, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(440, 'RuleImportAsset', 56, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(441, 'RuleImportAsset', 56, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is No item type defined (138)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(442, 'RuleCriteria', 138, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(443, 'RuleImportAsset', 56, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (56)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(444, 'RuleAction', 56, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(445, 'RuleImportAsset', 57, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(446, 'RuleImportAsset', 57, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Database instances (139)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(447, 'RuleCriteria', 139, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(448, 'RuleImportAsset', 57, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name exists Yes (140)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(449, 'RuleCriteria', 140, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(450, 'RuleImportAsset', 57, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name is already present Yes (141)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(451, 'RuleCriteria', 141, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(452, 'RuleImportAsset', 57, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Linked asset is already present Yes (142)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(453, 'RuleCriteria', 142, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(454, 'RuleImportAsset', 57, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (57)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(455, 'RuleAction', 57, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(456, 'RuleImportAsset', 58, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(457, 'RuleImportAsset', 58, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Database instances (143)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(458, 'RuleCriteria', 143, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(459, 'RuleImportAsset', 58, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name exists Yes (144)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(460, 'RuleCriteria', 144, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(461, 'RuleImportAsset', 58, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (58)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(462, 'RuleAction', 58, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(463, 'RuleImportAsset', 59, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(464, 'RuleImportAsset', 59, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Database instances (145)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(465, 'RuleCriteria', 145, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(466, 'RuleImportAsset', 59, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (59)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(467, 'RuleAction', 59, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(468, 'RuleImportAsset', 60, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(469, 'RuleImportAsset', 60, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Unmanaged devices (146)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(470, 'RuleCriteria', 146, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(471, 'RuleImportAsset', 60, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name exists Yes (147)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(472, 'RuleCriteria', 147, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(473, 'RuleImportAsset', 60, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name is already present Yes (148)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(474, 'RuleCriteria', 148, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(475, 'RuleImportAsset', 60, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (60)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(476, 'RuleAction', 60, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(477, 'RuleImportAsset', 61, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(478, 'RuleImportAsset', 61, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Unmanaged devices (149)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(479, 'RuleCriteria', 149, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(480, 'RuleImportAsset', 61, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Name exists Yes (150)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(481, 'RuleCriteria', 150, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(482, 'RuleImportAsset', 61, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Link if possible (61)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(483, 'RuleAction', 61, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(484, 'RuleImportAsset', 62, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(485, 'RuleImportAsset', 62, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Asset &#62; Item Type is Unmanaged devices (151)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(486, 'RuleCriteria', 151, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(487, 'RuleImportAsset', 62, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Inventory link Assign Import denied (no log) (62)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(488, 'RuleAction', 62, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(489, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'initialized_rules_collections []', '[\"RuleImportAssetCollection\"]');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(490, 'RuleMailCollector', 63, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(491, 'RuleMailCollector', 63, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Subject Email Header regular expression matches /.*/ (152)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(492, 'RuleCriteria', 152, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(493, 'RuleMailCollector', 63, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Entity Assign Root Entity (63)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(494, 'RuleAction', 63, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(495, 'RuleMailCollector', 64, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(496, 'RuleMailCollector', 64, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'X-Auto-Response-Suppress Email Header regular expression matches /S+/ (153)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(497, 'RuleCriteria', 153, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(498, 'RuleMailCollector', 64, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Reject Email (without email response) Assign Yes (64)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(499, 'RuleAction', 64, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(500, 'RuleMailCollector', 65, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(501, 'RuleMailCollector', 65, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Auto-Submitted Email Header regular expression matches /^(?!.*no).+$/i (154)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(502, 'RuleCriteria', 154, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(503, 'RuleMailCollector', 65, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Reject Email (without email response) Assign Yes (65)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(504, 'RuleAction', 65, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(505, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'initialized_rules_collections [\"RuleImportAssetCollection\"]', '[\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\"]');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(506, 'RuleRight', 66, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(507, 'RuleRight', 66, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Authentication type is LDAP Directories: (155)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(508, 'RuleCriteria', 155, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(509, 'RuleRight', 66, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Authentication type is Email Server: (156)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(510, 'RuleCriteria', 156, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(511, 'RuleRight', 66, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Entity Assign Root Entity (66)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(512, 'RuleAction', 66, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(513, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'initialized_rules_collections [\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\"]', '[\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\"]');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(514, 'RuleSoftwareCategory', 67, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(515, 'RuleSoftwareCategory', 67, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Software is * (157)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(516, 'RuleCriteria', 157, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(517, 'RuleSoftwareCategory', 67, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Import category from inventory tool Assign Yes (67)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(518, 'RuleAction', 67, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(519, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'initialized_rules_collections [\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\"]', '[\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\"]');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(520, 'RuleTicket', 68, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(521, 'RuleTicket', 68, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Ticket Location does not exist Yes (158)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(522, 'RuleCriteria', 158, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(523, 'RuleTicket', 68, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Unavailable exists Yes (159)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(524, 'RuleCriteria', 159, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(525, 'RuleTicket', 68, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Locations Copy from Item Yes (68)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(526, 'RuleAction', 68, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(527, 'RuleTicket', 69, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(528, 'RuleTicket', 69, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Ticket Location does not exist Yes (160)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(529, 'RuleCriteria', 160, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(530, 'RuleTicket', 69, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Requester Location exists Yes (161)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(531, 'RuleCriteria', 161, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(532, 'RuleTicket', 69, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Locations Copy from User Yes (69)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(533, 'RuleAction', 69, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(534, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'initialized_rules_collections [\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\"]', '[\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\",\"RuleTicketCollection\"]');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(535, 'RuleAsset', 70, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(536, 'RuleAsset', 70, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Item Type is Computers (162)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(537, 'RuleCriteria', 162, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(538, 'RuleAsset', 70, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Automatic Inventory is Yes (163)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(539, 'RuleCriteria', 163, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(540, 'RuleAsset', 70, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Alternate Username regular expression matches /(.*)@/ (164)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(541, 'RuleCriteria', 164, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(542, 'RuleAsset', 70, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'User Based Contact Information Assign the value from regular expression #0 (70)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(543, 'RuleAction', 70, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(544, 'RuleAsset', 71, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(545, 'RuleAsset', 71, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Item Type is Computers (165)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(546, 'RuleCriteria', 165, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(547, 'RuleAsset', 71, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Automatic Inventory is Yes (166)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(548, 'RuleCriteria', 166, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(549, 'RuleAsset', 71, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Alternate Username regular expression matches /(.*)[,|/]/ (167)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(550, 'RuleCriteria', 167, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(551, 'RuleAsset', 71, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'User Based Contact Information Assign the value from regular expression #0 (71)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(552, 'RuleAction', 71, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(553, 'RuleAsset', 72, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(554, 'RuleAsset', 72, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Item Type is Computers (168)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(555, 'RuleCriteria', 168, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(556, 'RuleAsset', 72, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Automatic Inventory is Yes (169)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(557, 'RuleCriteria', 169, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(558, 'RuleAsset', 72, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Alternate Username regular expression matches /(.*)/ (170)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(559, 'RuleCriteria', 170, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(560, 'RuleAsset', 72, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'User Based Contact Information Assign the value from regular expression #0 (72)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(561, 'RuleAction', 72, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(562, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'initialized_rules_collections [\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\",\"RuleTicketCollection\"]', '[\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\",\"RuleTicketCollection\",\"RuleAssetCollection\"]');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(563, 'RuleDictionnaryOperatingSystem', 73, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(564, 'RuleDictionnaryOperatingSystem', 73, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems regular expression matches /(SUSE|SunOS|Red Hat|CentOS|Ubuntu|Debian|Fedora|AlmaLinux|Oracle)(?:D+|)([d.]+) ?(?:(?([w ]+))?)?/ (171)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(565, 'RuleCriteria', 171, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(566, 'RuleDictionnaryOperatingSystem', 73, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems Add the result of regular expression #0 (73)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(567, 'RuleAction', 73, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(568, 'RuleDictionnaryOperatingSystem', 74, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(569, 'RuleDictionnaryOperatingSystem', 74, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems regular expression matches /(Microsoft)(?&#62;(R)|®)? (Windows) (XP|d.d|d{1,4}|Vista)(™)? ?(.*)/ (172)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(570, 'RuleCriteria', 172, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(571, 'RuleDictionnaryOperatingSystem', 74, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems Add the result of regular expression #1 (74)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(572, 'RuleAction', 74, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(573, 'RuleDictionnaryOperatingSystem', 75, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(574, 'RuleDictionnaryOperatingSystem', 75, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems regular expression matches /(Microsoft)(?&#62;(R)|®)? (?:(Hyper-V|Windows)(?:(R))?) ((?:Server|))(?:(R)|®)? (d{4}(?: R2)?)(?:[,s]++)?([^s]*)(?: Edition(?: x64)?)?');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(575, 'RuleCriteria', 173, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(576, 'RuleDictionnaryOperatingSystem', 75, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems Add the result of regular expression #1 #2 (75)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(577, 'RuleAction', 75, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(578, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'initialized_rules_collections [\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\",\"RuleTicketCollection\",\"RuleAssetCol', '[\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\",\"RuleTicketCollection\",\"RuleAssetCollection\",\"RuleDictionnaryOpera');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(579, 'RuleDictionnaryOperatingSystemVersion', 76, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(580, 'RuleDictionnaryOperatingSystemVersion', 76, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems regular expression matches /(SUSE|SunOS|Red Hat|CentOS|Ubuntu|Debian|Fedora|AlmaLinux|Oracle)(?:D+|)([d.]+) ?(?:(?([w ]+))?)?/ (174)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(581, 'RuleCriteria', 174, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(582, 'RuleDictionnaryOperatingSystemVersion', 76, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Version Add the result of regular expression #1 (76)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(583, 'RuleAction', 76, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(584, 'RuleDictionnaryOperatingSystemVersion', 77, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(585, 'RuleDictionnaryOperatingSystemVersion', 77, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems regular expression matches /(Microsoft)(?&#62;(R)|®)? (Windows) (XP|d.d|d{1,4}|Vista)(™)? ?(.*)/ (175)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(586, 'RuleCriteria', 175, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(587, 'RuleDictionnaryOperatingSystemVersion', 77, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Version Add the result of regular expression #2 (77)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(588, 'RuleAction', 77, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(589, 'RuleDictionnaryOperatingSystemVersion', 78, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(590, 'RuleDictionnaryOperatingSystemVersion', 78, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems regular expression matches /(Microsoft)(?&#62;(R)|®)? (?:(Hyper-V|Windows)(?:(R))?) ((?:Server|))(?:(R)|®)? (d{4}(?: R2)?)(?:[,s]++)?([^s]*)(?: Edition(?: x64)?)?');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(591, 'RuleCriteria', 176, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(592, 'RuleDictionnaryOperatingSystemVersion', 78, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Version Add the result of regular expression #3 (78)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(593, 'RuleAction', 78, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(594, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'initialized_rules_collections [\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\",\"RuleTicketCollection\",\"RuleAssetCol', '[\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\",\"RuleTicketCollection\",\"RuleAssetCollection\",\"RuleDictionnaryOpera');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(595, 'RuleDictionnaryOperatingSystemEdition', 79, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(596, 'RuleDictionnaryOperatingSystemEdition', 79, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems regular expression matches /(SUSE|SunOS|Red Hat|CentOS|Ubuntu|Debian|Fedora|AlmaLinux|Oracle)(?:D+|)([d.]+) ?(?:(?([w ]+))?)?/ (177)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(597, 'RuleCriteria', 177, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(598, 'RuleDictionnaryOperatingSystemEdition', 79, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Editions Add the result of regular expression #2 (79)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(599, 'RuleAction', 79, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(600, 'RuleDictionnaryOperatingSystemEdition', 80, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(601, 'RuleDictionnaryOperatingSystemEdition', 80, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems regular expression matches /(Microsoft)(?&#62;(R)|®)? (Windows) (XP|d.d|d{1,4}|Vista)(™)? ?(.*)/ (178)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(602, 'RuleCriteria', 178, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(603, 'RuleDictionnaryOperatingSystemEdition', 80, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Editions Add the result of regular expression #4 (80)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(604, 'RuleAction', 80, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(605, 'RuleDictionnaryOperatingSystemEdition', 81, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(606, 'RuleDictionnaryOperatingSystemEdition', 81, 'RuleCriteria', 17, '', '2023-03-17 19:45:27', 0, '', 'Operating Systems regular expression matches /(Microsoft)(?&#62;(R)|®)? (?:(Hyper-V|Windows)(?:(R))?) ((?:Server|))(?:(R)|®)? (d{4}(?: R2)?)(?:[,s]++)?([^s]*)(?: Edition(?: x64)?)?');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(607, 'RuleCriteria', 179, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(608, 'RuleDictionnaryOperatingSystemEdition', 81, 'RuleAction', 17, '', '2023-03-17 19:45:27', 0, '', 'Editions Add the result of regular expression #4 (81)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(609, 'RuleAction', 81, '0', 20, '', '2023-03-17 19:45:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(610, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'initialized_rules_collections [\"RuleImportAssetCollection\",\"RuleMailCollectorCollection\",\"RuleRightCollection\",\"RuleSoftwareCategoryCollection\",\"RuleTicketCollection\",\"RuleAssetCol', '{...}');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(611, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'language en_GB', 'en_US');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(612, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'version FILLED AT INSTALL', '10.0.6');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(613, 'Config', 1, '', 0, '', '2023-03-17 19:45:27', 1, 'dbversion FILLED AT INSTALL', '10.0.6@21cffee0fbb5afbf0d580cabdf6fd7a922598f97');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(614, 'Config', 1, '', 0, '', '2023-03-17 19:47:46', 1, 'registration_uuid ', 'PTHnuqaeNgjTSBF74bqRFgoAPf2Nr97W0c2rXfWU');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(615, 'Location', 1, '0', 20, 'glpi (2)', '2023-03-19 19:14:30', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(616, 'Location', 2, '0', 20, 'glpi (2)', '2023-03-19 19:14:48', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(617, 'State', 1, '0', 20, 'glpi (2)', '2023-03-19 19:15:09', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(618, 'State', 2, '0', 20, 'glpi (2)', '2023-03-19 19:15:14', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(619, 'ComputerType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:15:32', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(620, 'ComputerType', 2, '0', 20, 'glpi (2)', '2023-03-19 19:15:36', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(621, 'ComputerType', 3, '0', 20, 'glpi (2)', '2023-03-19 19:15:46', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(622, 'Manufacturer', 1, '0', 20, 'glpi (2)', '2023-03-19 19:15:55', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(623, 'Manufacturer', 2, '0', 20, 'glpi (2)', '2023-03-19 19:16:00', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(624, 'Manufacturer', 3, '0', 20, 'glpi (2)', '2023-03-19 19:16:03', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(625, 'Manufacturer', 4, '0', 20, 'glpi (2)', '2023-03-19 19:16:09', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(626, 'ComputerModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:16:21', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(627, 'ComputerModel', 2, '0', 20, 'glpi (2)', '2023-03-19 19:16:45', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(628, 'Network', 1, '0', 20, 'glpi (2)', '2023-03-19 19:17:17', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(629, 'AutoUpdateSystem', 1, '0', 20, 'glpi (2)', '2023-03-19 19:17:29', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(630, 'Computer', 1, '0', 20, 'glpi (2)', '2023-03-19 19:17:32', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(631, 'MonitorType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:18:13', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(632, 'MonitorModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:18:35', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(633, 'Monitor', 1, '0', 20, 'glpi (2)', '2023-03-19 19:18:51', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(634, 'Software', 1, '0', 20, 'glpi (2)', '2023-03-19 19:20:51', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(635, 'Software', 2, '0', 20, 'glpi (2)', '2023-03-19 19:21:10', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(636, 'NetworkEquipmentType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:25:10', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(637, 'NetworkEquipmentModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:26:05', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(638, 'NetworkEquipment', 1, '0', 20, 'glpi (2)', '2023-03-19 19:26:16', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(639, 'PeripheralType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:27:28', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(640, 'PeripheralModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:27:47', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(641, 'Peripheral', 1, '0', 20, 'glpi (2)', '2023-03-19 19:28:09', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(642, 'PrinterType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:31:02', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(643, 'PrinterModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:31:19', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(644, 'Printer', 1, '0', 20, 'glpi (2)', '2023-03-19 19:31:53', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(645, 'CartridgeItemType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:33:01', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(646, 'CartridgeItem', 1, '0', 20, 'glpi (2)', '2023-03-19 19:33:19', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(647, 'ConsumableItemType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:33:44', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(648, 'ConsumableItem', 1, '0', 20, 'glpi (2)', '2023-03-19 19:33:56', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(649, 'PhoneType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:34:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(650, 'PhoneModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:34:41', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(651, 'PhonePowerSupply', 1, '0', 20, 'glpi (2)', '2023-03-19 19:35:12', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(652, 'Phone', 1, '0', 20, 'glpi (2)', '2023-03-19 19:35:19', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(653, 'RackType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:35:43', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(654, 'RackModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:35:56', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(655, 'DCRoom', 1, '0', 20, 'glpi (2)', '2023-03-19 19:36:19', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(656, 'Rack', 1, '0', 20, 'glpi (2)', '2023-03-19 19:36:30', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(657, 'EnclosureModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:37:11', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(658, 'Enclosure', 1, '0', 20, 'glpi (2)', '2023-03-19 19:37:19', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(659, 'PDUType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:37:48', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(660, 'PDUModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:38:01', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(661, 'PDU', 1, '0', 20, 'glpi (2)', '2023-03-19 19:38:06', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(662, 'PassiveDCEquipmentType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:38:31', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(663, 'PassiveDCEquipmentModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:38:51', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(664, 'PassiveDCEquipment', 1, '0', 20, 'glpi (2)', '2023-03-19 19:38:56', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(665, 'CableType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:39:17', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(666, 'CableStrand', 1, '0', 20, 'glpi (2)', '2023-03-19 19:39:31', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(667, 'Glpi\\SocketModel', 1, '0', 20, 'glpi (2)', '2023-03-19 19:39:44', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(668, 'Glpi\\SocketModel', 2, '0', 20, 'glpi (2)', '2023-03-19 19:40:04', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(669, 'Location', 1, 'Glpi\\Socket', 17, 'glpi (2)', '2023-03-19 19:40:20', 0, '', 'Socket1 (1)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(670, 'Glpi\\Socket', 1, '0', 20, 'glpi (2)', '2023-03-19 19:40:20', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(671, 'Cable', 1, '0', 20, 'glpi (2)', '2023-03-19 19:40:27', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(672, 'DeviceSimcard', 1, '0', 20, 'glpi (2)', '2023-03-19 19:40:50', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(673, 'LineType', 1, '0', 20, 'glpi (2)', '2023-03-19 19:41:13', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(674, 'LineOperator', 1, '0', 20, 'glpi (2)', '2023-03-19 19:41:26', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(675, 'Line', 1, '0', 20, 'glpi (2)', '2023-03-19 19:41:29', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(676, 'OperatingSystem', 1, '0', 20, 'glpi (2)', '2023-03-19 19:42:10', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(677, 'OperatingSystemArchitecture', 1, '0', 20, 'glpi (2)', '2023-03-19 19:42:18', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(678, 'OperatingSystemKernelVersion', 1, '0', 20, 'glpi (2)', '2023-03-19 19:42:25', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(679, 'OperatingSystemVersion', 1, '0', 20, 'glpi (2)', '2023-03-19 19:42:33', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(680, 'OperatingSystemServicePack', 1, '0', 20, 'glpi (2)', '2023-03-19 19:42:47', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(681, 'OperatingSystemEdition', 1, '0', 20, 'glpi (2)', '2023-03-19 19:42:58', 0, '', '');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(682, 'OperatingSystem', 1, 'Computer', 15, 'glpi (2)', '2023-03-19 19:43:01', 0, '', 'Computer1 (1)');
REPLACE INTO `glpi_logs` (`id`, `itemtype`, `items_id`, `itemtype_link`, `linked_action`, `user_name`, `date_mod`, `id_search_option`, `old_value`, `new_value`) VALUES(683, 'Computer', 1, 'OperatingSystem', 15, 'glpi (2)', '2023-03-19 19:43:01', 0, '', 'Windows11 (1)');

--
-- Volcado de datos para la tabla `glpi_manufacturers`
--

REPLACE INTO `glpi_manufacturers` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'Lenovo', '', '2023-03-19 19:15:55', '2023-03-19 19:15:55');
REPLACE INTO `glpi_manufacturers` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'ASUS', '', '2023-03-19 19:16:00', '2023-03-19 19:16:00');
REPLACE INTO `glpi_manufacturers` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(3, 'MSI', '', '2023-03-19 19:16:03', '2023-03-19 19:16:03');
REPLACE INTO `glpi_manufacturers` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(4, 'HP', '', '2023-03-19 19:16:09', '2023-03-19 19:16:09');

--
-- Volcado de datos para la tabla `glpi_monitormodels`
--

REPLACE INTO `glpi_monitormodels` (`id`, `name`, `comment`, `product_number`, `weight`, `required_units`, `depth`, `power_connections`, `power_consumption`, `is_half_rack`, `picture_front`, `picture_rear`, `pictures`, `date_mod`, `date_creation`) VALUES(1, 'MonitorModel', 'werwer', '1213154645', 12, 1, 1, 22, 12, 0, NULL, NULL, NULL, '2023-03-19 19:18:35', '2023-03-19 19:18:35');

--
-- Volcado de datos para la tabla `glpi_monitors`
--

REPLACE INTO `glpi_monitors` (`id`, `entities_id`, `name`, `date_mod`, `contact`, `contact_num`, `users_id_tech`, `groups_id_tech`, `comment`, `serial`, `otherserial`, `size`, `have_micro`, `have_speaker`, `have_subd`, `have_bnc`, `have_dvi`, `have_pivot`, `have_hdmi`, `have_displayport`, `locations_id`, `monitortypes_id`, `monitormodels_id`, `manufacturers_id`, `is_global`, `is_deleted`, `is_template`, `template_name`, `users_id`, `groups_id`, `states_id`, `ticket_tco`, `is_dynamic`, `autoupdatesystems_id`, `uuid`, `date_creation`, `is_recursive`) VALUES(1, 0, 'Monitor1', '2023-03-19 19:18:51', 'Alternate', 'Alternate1', 0, 0, 'MonitorComment1', '23231323132323', '12323132313', '11.00', 1, 0, 0, 1, 0, 0, 0, 1, 2, 1, 1, 4, 0, 0, 0, NULL, 0, 0, 2, '0.0000', 0, 1, 'uuid23', '2023-03-19 19:18:51', 0);

--
-- Volcado de datos para la tabla `glpi_monitortypes`
--

REPLACE INTO `glpi_monitortypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'MonitorType1', 'MonitorTypeComment1', '2023-03-19 19:18:13', '2023-03-19 19:18:13');

--
-- Volcado de datos para la tabla `glpi_networkequipmentmodels`
--

REPLACE INTO `glpi_networkequipmentmodels` (`id`, `name`, `comment`, `product_number`, `weight`, `required_units`, `depth`, `power_connections`, `power_consumption`, `is_half_rack`, `picture_front`, `picture_rear`, `pictures`, `date_mod`, `date_creation`) VALUES(1, 'NetEquipmentModel1', 'Comment', '2131313', 2323, 1, 1, 2, 1, 1, NULL, NULL, NULL, '2023-03-19 19:26:05', '2023-03-19 19:26:05');

--
-- Volcado de datos para la tabla `glpi_networkequipments`
--

REPLACE INTO `glpi_networkequipments` (`id`, `entities_id`, `is_recursive`, `name`, `ram`, `serial`, `otherserial`, `contact`, `contact_num`, `users_id_tech`, `groups_id_tech`, `date_mod`, `comment`, `locations_id`, `networks_id`, `networkequipmenttypes_id`, `networkequipmentmodels_id`, `manufacturers_id`, `is_deleted`, `is_template`, `template_name`, `users_id`, `groups_id`, `states_id`, `ticket_tco`, `is_dynamic`, `uuid`, `date_creation`, `autoupdatesystems_id`, `sysdescr`, `cpu`, `uptime`, `last_inventory_update`, `snmpcredentials_id`) VALUES(1, 0, 0, 'NetworkDevice1', '23', '232131321', '121212121', 'Alternateusername1', 'Alternate1', 0, 0, '2023-03-19 19:26:16', 'NetDeviceComment', 1, 1, 1, 1, 4, 0, 0, NULL, 0, 0, 1, '0.0000', 0, 'uuid', '2023-03-19 19:26:16', 1, 'SysDescr', 0, '0', NULL, 1);

--
-- Volcado de datos para la tabla `glpi_networkequipmenttypes`
--

REPLACE INTO `glpi_networkequipmenttypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'NetEquipmentType1', 'comment', '2023-03-19 19:25:10', '2023-03-19 19:25:10');

--
-- Volcado de datos para la tabla `glpi_networkporttypes`
--

REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(1, 0, 0, 0, 'Name', 'Description References', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(2, 0, 0, 1, 'other', 'none of the following [RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(3, 0, 0, 2, 'regular1822', 'BBN Report 1822 [RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(4, 0, 0, 3, 'hdh1822', 'BBN Report 1822 [RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(5, 0, 0, 4, 'ddn-x25', 'BBN Report 1822 [RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(6, 0, 0, 5, 'x25', 'X.25 [RFC1382]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(7, 0, 0, 6, 'ethernet-csmacd', '[RFC1213]', 1, 'NetworkPortEthernet', '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(8, 0, 0, 7, 'IEEE802.3', 'DEPRECATED [RFC3635]', 1, 'NetworkPortEthernet', '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(9, 0, 0, 8, 'IEEE802.4', 'Token Bus-like Objects [RFC1239]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(10, 0, 0, 9, 'IEEE802.5', 'Token Ring-like Objects [RFC1748]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(11, 0, 0, 10, 'iso88026-man', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(12, 0, 0, 11, 'starLan', 'DEPRECATED [RFC3635]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(13, 0, 0, 12, 'proteon-10Mbit', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(14, 0, 0, 13, 'proteon-80Mbit', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(15, 0, 0, 14, 'hyperchannel', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(16, 0, 0, 15, 'FDDI', 'FDDI Objects [RFC1512]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(17, 0, 0, 16, 'lapb', 'LAP B [RFC1381]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(18, 0, 0, 17, 'sdlc', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(19, 0, 0, 18, 'ds1', 'T1/E1 Carrier Objects [RFC4805]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(20, 0, 0, 19, 'e1', 'obsolete [RFC4805]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(21, 0, 0, 20, 'basicISDN', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(22, 0, 0, 21, 'primaryISDN', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(23, 0, 0, 22, 'propPointToPointSerial', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(24, 0, 0, 23, 'ppp', 'Point-to-Point Protocol [RFC1213][RFC1471]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(25, 0, 0, 24, 'softwareLoopback', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(26, 0, 0, 25, 'eon', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(27, 0, 0, 26, 'ethernet-3Mbit', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(28, 0, 0, 27, 'nsip', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(29, 0, 0, 28, 'slip', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(30, 0, 0, 29, 'ultra', '[RFC1213]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(31, 0, 0, 30, 'ds3', 'DS3/E3 Interface Objects [RFC3896]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(32, 0, 0, 31, 'sip', 'SMDS Interface Objects [RFC1694]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(33, 0, 0, 32, 'frame-relay', 'Frame Relay Objects for DTE [RFC2115]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(34, 0, 0, 33, 'RS-232', 'RS-232 Objects [RFC1659]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(35, 0, 0, 34, 'Parallel', 'Parallel Printer Objects [RFC1660]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(36, 0, 0, 35, 'arcnet', 'ARC network', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(37, 0, 0, 36, 'arcnet-plus', 'ARC network plus', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(38, 0, 0, 37, 'atm', 'ATM', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(39, 0, 0, 38, 'MIOX25', 'MIOX25 [RFC1461]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(40, 0, 0, 39, 'SONET', 'SONET or SDH', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(41, 0, 0, 40, 'x25ple', 'X.25 packet level [RFC2127]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(42, 0, 0, 41, 'iso88022llc', '802.2 LLC', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(43, 0, 0, 42, 'localTalk', '', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(44, 0, 0, 43, 'smds-dxi', 'SMDS DXI', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(45, 0, 0, 44, 'frameRelayService', 'Frame Relay DCE [RFC2954]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(46, 0, 0, 45, 'v35', 'V.35', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(47, 0, 0, 46, 'hssi', 'HSSI', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(48, 0, 0, 47, 'hippi', 'HIPPI', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(49, 0, 0, 48, 'modem', 'generic modem', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(50, 0, 0, 49, 'aal5', 'AAL5 over ATM', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(51, 0, 0, 50, 'sonetPath', '', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(52, 0, 0, 51, 'sonetVT', '', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(53, 0, 0, 52, 'smds-icip', 'SMDS Inter-Carrier Interface Protocol', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(54, 0, 0, 53, 'propVirtual', 'proprietary vitural/internal interface [RFC2863]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(55, 0, 0, 54, 'propMultiLink', 'proprietary multi-link multiplexing [RFC2863]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(56, 0, 0, 55, 'ieee80212', '100BaseVG', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(57, 0, 0, 56, 'fibre-channel', 'Fibre Channel', 1, 'NetworkPortFiberchannel', '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(58, 0, 0, 57, 'hippiInterfaces', 'HIPPI interfaces [Philip_Cameron]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(59, 0, 0, 58, 'FrameRelayInterconnect', 'Interconnet over FR [Unknown]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(60, 0, 0, 59, 'aflane8023', 'ATM Emulated LAN for 802.3 [Keith_McCloghrie]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(61, 0, 0, 60, 'aflane8025', 'ATM Emulated LAN for 802.5 [Keith_McCloghrie]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(62, 0, 0, 61, 'cctEmul', 'ATM Emulated circuit [Guy_Fedorkow]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(63, 0, 0, 62, 'fastEther', 'DEPRECATED [RFC3635]', 1, 'NetworkPortEthernet', '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(64, 0, 0, 63, 'isdn', 'ISDN and X.25 [RFC1356]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(65, 0, 0, 64, 'v11', 'CCITT V.11/X.21 [Satish_Popat]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(66, 0, 0, 65, 'v36', 'CCITT V.36 [Satish_Popat]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(67, 0, 0, 66, 'g703-64k', 'CCITT G703 at 64Kbps [Satish_Popat]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(68, 0, 0, 67, 'g703-2mb', 'CCITT G703 at 2Mbps [Satish_Popat]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(69, 0, 0, 68, 'qllc', 'SNA QLLC [Satish_Popat]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(70, 0, 0, 69, 'fastEtherFX', 'DEPRECATED [RFC3635]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(71, 0, 0, 70, 'channel', 'channel [Steven_Schwell]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(72, 0, 0, 71, 'IEEE802.11', 'radio spread spectrum [Dawkoon_Paul_Lee]', 1, 'NetworkPortWifi', '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(73, 0, 0, 72, 'ibm370parChan', 'IBM System 360/370 OEMI Channel [Bill_Kwan]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(74, 0, 0, 73, 'ESCON', 'IBM Enterprise Systems Connection [Bill_Kwan]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(75, 0, 0, 74, 'DLSw', 'Data Link Switching [Bill_Kwan]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(76, 0, 0, 75, 'ISDNs', 'ISDN S/T interface [Ed_Alcoff]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(77, 0, 0, 76, 'ISDNu', 'ISDN U interface [Ed_Alcoff]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(78, 0, 0, 77, 'lapd', 'Link Access Protocol D [Ed_Alcoff]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(79, 0, 0, 78, 'ip-switch', 'IP Switching Objects [Joe_Wei]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(80, 0, 0, 79, 'rsrb', 'Remote Source Route Bridging [Bob_Clouston]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(81, 0, 0, 80, 'atm-logical', 'ATM Logical Port [RFC3606]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(82, 0, 0, 81, 'ds0', 'Digital Signal Level 0 [RFC2494]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(83, 0, 0, 82, 'ds0Bundle', 'group of ds0s on the same ds1 [RFC2494]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(84, 0, 0, 83, 'bsc', 'Bisynchronous Protocol [Bill_Kwan]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(85, 0, 0, 84, 'async', 'Asynchronous Protocol [Bill_Kwan]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(86, 0, 0, 85, 'cnr', 'Combat Net Radio [Herb_Jensen]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(87, 0, 0, 86, 'iso88025Dtr', 'ISO 802.5r DTR [Trevor_Warwick]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(88, 0, 0, 87, 'eplrs', 'Enhanced  Pos Loc Report Sys [Herb_Jensen]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(89, 0, 0, 88, 'arap', 'Appletalk Remote Access Protocol [Jim_Halpin]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(90, 0, 0, 89, 'propCnls', 'Proprietary Connectionless Proto. [Robert_Neill]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(91, 0, 0, 90, 'hostPad', 'CCITT-ITU X.29 PAD Protocol [Robert_Neill]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(92, 0, 0, 91, 'termPad', 'CCITT-ITU X.3 PAD Facility [Robert_Neill]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(93, 0, 0, 92, 'frameRelayMPI', 'Multiproto Interconnect over FR [Robert_Neill]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(94, 0, 0, 93, 'x213', 'CCITT-ITU X213 [Robert_Neill]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(95, 0, 0, 94, 'adsl', 'Asymmetric Digital Subscriber Loop [Gregory_Bathrick]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(96, 0, 0, 95, 'radsl', 'Rate-Adapt. Digital Subscriber Loop [Gregory_Bathrick]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(97, 0, 0, 96, 'sdsl', 'Symmetric Digital Subscriber Loop [Gregory_Bathrick]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(98, 0, 0, 97, 'vdsl', 'Very H-Speed Digital Subscrib. Loop [Gregory_Bathrick]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(99, 0, 0, 98, 'iso88025CRFPInt', 'ISO 802.5 CRFP [Trevor_Warwick]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(100, 0, 0, 99, 'myrinet', 'Myricom Myrinet [Bob_Felderman]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(101, 0, 0, 100, 'voiceEM', 'Voice recEive and transMit (E&#38;M) [Bob_Stewart]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(102, 0, 0, 101, 'voiceFXO', 'Voice Foreign Exchange Office [Bob_Stewart]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(103, 0, 0, 102, 'voiceFXS', 'Voice Foreign Exchange Station [Bob_Stewart]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(104, 0, 0, 103, 'voiceEncap', 'Voice encapsulation [Bob_Stewart]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(105, 0, 0, 104, 'voiceOverIp', 'Voice over IP encapsulation [Bob_Stewart]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(106, 0, 0, 105, 'atmDxi', 'ATM DXI [Gary_Hanson]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(107, 0, 0, 106, 'atmFuni', 'ATM FUNI [Gary_Hanson]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(108, 0, 0, 107, 'atmIma', 'ATM IMA [Chris_Martin]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(109, 0, 0, 108, 'pppMultilinkBundle', 'PPP Multilink Bundle [John_Shriver]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(110, 0, 0, 109, 'ipOverCdlc', 'IBM ipOverCdlc [Ken_White]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(111, 0, 0, 110, 'ipOverClaw', 'IBM Common Link Access to Workstn [Ken_White]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(112, 0, 0, 111, 'stackToStack', 'IBM stackToStack [Ken_White]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(113, 0, 0, 112, 'virtualIpAddress', 'IBM VIPA [Ken_White]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(114, 0, 0, 113, 'mpc', 'IBM multi-protocol channel support [Ken_White]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(115, 0, 0, 114, 'ipOverAtm', 'IBM ipOverAtm [RFC2320]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(116, 0, 0, 115, 'iso88025Fiber', 'ISO 802.5j Fiber Token Ring [Kevin_Lingle]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(117, 0, 0, 116, 'tdlc', 'IBM twinaxial data link control [John_Pechacek]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(118, 0, 0, 117, 'gigabitEthernet', 'DEPRECATED [RFC3635]', 1, 'NetworkPortEthernet', '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(119, 0, 0, 118, 'hdlc', 'HDLC [Sebastien_Rosset]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(120, 0, 0, 119, 'lapf', 'LAP F [Sebastien_Rosset]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(121, 0, 0, 120, 'v37', 'V.37 [Sebastien_Rosset]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(122, 0, 0, 121, 'x25mlp', 'Multi-Link Protocol [Sebastien_Rosset]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(123, 0, 0, 122, 'x25huntGroup', 'X25 Hunt Group [Sebastien_Rosset]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(124, 0, 0, 123, 'transpHdlc', 'Transp HDLC [Sebastien_Rosset]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(125, 0, 0, 124, 'interleave', 'Interleave channel [Karmous_Edwards]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(126, 0, 0, 125, 'fast', 'Fast channel [Karmous_Edwards]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(127, 0, 0, 126, 'ip', 'IP (for APPN HPR in IP networks) [Robert_Moore]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(128, 0, 0, 127, 'docsCableMaclayer', 'CATV Mac Layer [Azlina_Palmer]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(129, 0, 0, 128, 'docsCableDownstream', 'CATV Downstream interface [Azlina_Palmer]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(130, 0, 0, 129, 'docsCableUpstream', 'CATV Upstream interface [Azlina_Palmer]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(131, 0, 0, 130, 'a12MppSwitch', 'Avalon Parallel Processor [Ross_Harvey]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(132, 0, 0, 131, 'tunnel', 'Encapsulation interface [Dave_Thaler]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(133, 0, 0, 132, 'coffee', 'coffee pot [RFC2325]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(134, 0, 0, 133, 'ces', 'Circiut Emulation Service [Ron_Carmona]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(135, 0, 0, 134, 'atmSubInterface', '(x)  ATM Sub Interface [Keith_McCloghrie]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(136, 0, 0, 135, 'l2vlan', 'Layer 2 Virtual LAN using 802.1Q [Mike_MacFaden]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(137, 0, 0, 136, 'l3ipvlan', 'Layer 3 Virtual LAN - IP Protocol [Mike_MacFaden]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(138, 0, 0, 137, 'l3ipxvlan', 'Layer 3 Virtual LAN - IPX Prot. [Mike_MacFaden]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(139, 0, 0, 138, 'digitalPowerLine', 'IP over Power Lines [Hans_Scholtes]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(140, 0, 0, 139, 'mediaMailOverIp', '(xxx)  Multimedia Mail over IP [Hongchi_Shih]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(141, 0, 0, 140, 'dtm', 'Dynamic synchronous Transfer Mode [Jakob_Ellerstedt]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(142, 0, 0, 141, 'dcn', 'Data Communications Network [James_Card]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(143, 0, 0, 142, 'ipForward', 'IP Forwarding Interface [James_Card]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(144, 0, 0, 143, 'msdsl', 'Multi-rate Symmetric DSL [Gopinath_Durairaj]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(145, 0, 0, 144, 'ieee1394     IEEE1394', 'High Performance Serial Bus [Kenji_Fujisawa]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(146, 0, 0, 145, 'if-gsn', 'HIPPI-6400 [Jean_Michel_Pittet]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(147, 0, 0, 146, 'dvbRccMacLayer', 'DVB-RCC MAC Layer [Maarten_Oelering]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(148, 0, 0, 147, 'dvbRccDownstream', 'DVB-RCC Downstream Channel [Maarten_Oelering]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(149, 0, 0, 148, 'dvbRccUpstream', 'DVB-RCC Upstream Channel [Maarten_Oelering]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(150, 0, 0, 149, 'atmVirtual', 'ATM Virtual Interface [Subrahmanya_Hegde]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(151, 0, 0, 150, 'mplsTunnel', 'MPLS Tunnel Virtual Interface [Cheenu_Srinivasan]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(152, 0, 0, 151, 'srp', 'Spatial Reuse Protocol [Bill_Shetti]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(153, 0, 0, 152, 'voiceOverAtm', 'Voice over ATM [Chris_White]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(154, 0, 0, 153, 'voiceOverFrameRelay', 'Voice Over Frame Relay [Chris_White]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(155, 0, 0, 154, 'idsl', 'Digital Subscriber Loop over ISDN [Patrick_Gili]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(156, 0, 0, 155, 'compositeLink', 'Avici Composite Link Interface [Joseph_Dube]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(157, 0, 0, 156, 'ss7SigLink', 'SS7 Signaling Link [Cheenu_Srinivasan]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(158, 0, 0, 157, 'propWirelessP2P', 'Prop. P2P wireless interface [Joseph_Raja]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(159, 0, 0, 158, 'frForward', 'Frame forward Interface [Subrahmanya_Hegde]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(160, 0, 0, 159, 'rfc1483', 'Multiprotocol over ATM AAL5 [RFC1483]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(161, 0, 0, 160, 'USB', 'USB Interface [Bejamin_Dolnik]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(162, 0, 0, 161, 'ieee8023adLag', 'IEEE 802.3ad Link Aggregate [Les_Bell]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(163, 0, 0, 162, 'bgpPolicyAccounting', 'BGP Policy Accounting [Vinod_B_C]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(164, 0, 0, 163, 'frf16MfrBundle', 'FRF.16 Multilik Frame Relay [Pate_Prayson]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(165, 0, 0, 164, 'h323Gatekeeper', 'H323 Gatekeeper [Chris_White]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(166, 0, 0, 165, 'h323Proxy', 'H323 Voice and Video Proxy [Chris_White]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(167, 0, 0, 166, 'mpls', 'MPLS [Cheenu_Srinivasan]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(168, 0, 0, 167, 'mfSigLink', 'Multi-frequency signaling link [Cheenu_Srinivasan]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(169, 0, 0, 168, 'hdsl2', 'High Bit-Rate DSL, 2nd gen. [Bob_Ray]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(170, 0, 0, 169, 'shdsl', 'Multirate HDSL2 [Bob_Ray]', 1, 'NetworkPortEthernet', '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(171, 0, 0, 170, 'ds1FDL', 'Facility Data Link (4Kbps) on a DS1 [Bill_Kwan]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(172, 0, 0, 171, 'POS', 'Packet over SONET/SDH Interface [Ewart_Tempest]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(173, 0, 0, 172, 'dvbAsiIn', 'DVB-ASI Input [Hezi_Oved]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(174, 0, 0, 173, 'dvbAsiOut', 'DVB-ASI Output [Hezi_Oved]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(175, 0, 0, 174, 'plc', 'Power Line Communications [Andrew_Lunn]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(176, 0, 0, 175, 'NFAS', 'Non-Facility Associated Signaling [Sidney_Antommarchi]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(177, 0, 0, 176, 'TR008', 'TROO8 [Sidney_Antommarchi]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(178, 0, 0, 177, 'GR303RDT', 'Remote Digital Terminal [Sidney_Antommarchi]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(179, 0, 0, 178, 'GR303IDT', 'Integrated Digital Terminal [Sidney_Antommarchi]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(180, 0, 0, 179, 'ISUP', 'ISUP [Sidney_Antommarchi]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(181, 0, 0, 180, 'propDocsWirelessMaclayer', 'Cisco proprietary Maclayer [Joseph_Raja]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(182, 0, 0, 181, 'propDocsWirelessDownstream', 'Cisco proprietary Downstream [Joseph_Raja]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(183, 0, 0, 182, 'propDocsWirelessUpstream', 'Cisco proprietary Upstream [Joseph_Raja]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(184, 0, 0, 183, 'hiperlan2', 'HIPERLAN Type 2 Radio Interface [Jamshid_Khun_Jush]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(185, 0, 0, 184, 'propBWAp2Mp', 'PropBroadbandWirelessAccesspt2Multipt\n(use of this type for IEEE 802.16\nWMAN, interfaces as per IEEE 802.16\nis deprecated and iftype 237 should\nbe used instead) [Zvika_Zilberman]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(186, 0, 0, 185, 'sonetOverheadChannel', 'SONET Overhead Channel [ODSI_Coalition_K_Arv]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(187, 0, 0, 186, 'digitalWrapperOverheadChannel', 'Digital Wrapper\nOverhead [ODSI_Coalition_K_Arv]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(188, 0, 0, 187, 'aal2', 'ATM adaptation layer 2 [K_Ashoka]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(189, 0, 0, 188, 'radioMAC', 'MAC layer over radio links [Daniele_Behar]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(190, 0, 0, 189, 'atmRadio', 'ATM over radio links [Daniele_Behar]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(191, 0, 0, 190, 'IMT', 'Inter-Machine Trunks [Sidney_Antommarchi]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(192, 0, 0, 191, 'mvl', 'Multiple Virtual Lines DSL [Kevin_Baughman]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(193, 0, 0, 192, 'reachDSL', 'Long Reach DSL [Kevin_Baughman]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(194, 0, 0, 193, 'frDlciEndPt', 'Frame Relay DLCI End Point [Robert_Steinberger]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(195, 0, 0, 194, 'atmVciEndPt', 'ATM VCI End Point [Robert_Steinberger]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(196, 0, 0, 195, 'opticalChannel', 'Optical Channel [Mark_Stewart]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(197, 0, 0, 196, 'opticalTransport', 'Optical Transport [Mark_Stewart]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(198, 0, 0, 197, 'propAtm', 'Proprietary ATM [Subrahmanya_Hegde]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(199, 0, 0, 198, 'voiceOverCable', 'Voice Over Cable Interface [Eugene_Nechamkin]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(200, 0, 0, 199, 'infiniband', 'Infiniband [Bill_Strahm]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(201, 0, 0, 200, 'teLink', 'TE Link [Martin_Dubuc]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(202, 0, 0, 201, 'q2931', 'Q.2931 [Sidney_Antommarchi_2]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(203, 0, 0, 202, 'virtualTg', 'Virtual Trunk Group [Sidney_Antommarchi_2]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(204, 0, 0, 203, 'sipTg', 'SIP Trunk Group [Sidney_Antommarchi_2]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(205, 0, 0, 204, 'sipSig', 'SIP Signaling [Sidney_Antommarchi_2]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(206, 0, 0, 205, 'docsCableUpstreamChannel', 'CATV Upstream Channel [Greg_Nakanishi]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(207, 0, 0, 206, 'econet', 'Acorn Econet [Ben_Harris]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(208, 0, 0, 207, 'pon155', 'FSAN 155Mb Symetrical PON interface [Graham_Higgins]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(209, 0, 0, 208, 'pon622', 'FSAN 622Mb Symetrical PON interface [Graham_Higgins]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(210, 0, 0, 209, 'bridge', 'Transparent bridge interface [Yuzo_Watanabe]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(211, 0, 0, 210, 'linegroup', 'Interface common to multiple lines [Yuzo_Watanabe]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(212, 0, 0, 211, 'voiceEMFGD', 'voice E&#38;M Feature Group D [Taher_Shaikh]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(213, 0, 0, 212, 'voiceFGDEANA', 'voice FGD Exchange Access North American [Taher_Shaikh]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(214, 0, 0, 213, 'voiceDID', 'voice Direct Inward Dialing [Taher_Shaikh]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(215, 0, 0, 214, 'mpegTransport', 'MPEG transport interface [Gaurav_Aggarwal]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(216, 0, 0, 215, 'sixToFour', '6to4 interface  (DEPRECATED) [RFC4087]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(217, 0, 0, 216, 'gtp', 'GTP (GPRS Tunneling Protocol) [Rajesh_M_L]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(218, 0, 0, 217, 'pdnEtherLoop1', 'Paradyne EtherLoop 1 [Shu_Dong]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(219, 0, 0, 218, 'pdnEtherLoop2', 'Paradyne EtherLoop 2 [Shu_Dong]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(220, 0, 0, 219, 'opticalChannelGroup', 'Optical Channel Group [Hing_Kam_Lam]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(221, 0, 0, 220, 'homepna', 'HomePNA ITU-T G.989 [Stephen_Palm]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(222, 0, 0, 221, 'gfp', 'Generic Framing Procedure (GFP) [Italo_Busi]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(223, 0, 0, 222, 'ciscoISLvlan', 'Layer 2 Virtual LAN using Cisco ISL [Sandeep_Raghavendra]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(224, 0, 0, 223, 'actelisMetaLOOP', 'Acteleis proprietary MetaLOOP\nHigh Speed Link [Edward_Beili]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(225, 0, 0, 224, 'fcipLink', 'FCIP Link [Anil_Rijhsinghani]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(226, 0, 0, 225, 'rpr', 'Resilient Packet Ring Interface Type [IEEE 802.17]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(227, 0, 0, 226, 'qam', 'RF Qam Interface [Jeyachitra_Alagar]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(228, 0, 0, 227, 'lmp', 'Link Management Protocol [RFC4327]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(229, 0, 0, 228, 'cblVectaStar', 'Cambridge Broadband Networks Limited\nVectaStar [John_Naylon]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(230, 0, 0, 229, 'docsCableMCmtsDownstream', 'CATV Modular CMTS Downstream\nInterface [Eduardo_Cardona][\"Data-Over-Cable Service Interface Specifications:\nM-CMTS Operations Support System Interface Specification,\nCM-SP-M-OSSI-I01-050805\", DOCSIS, August 2005.][http://www.cablemodem.com/specifications][https://www.cablelabs.com/specifications/archives/docsis.html]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(231, 0, 0, 230, 'adsl2', 'Asymmetric Digital Subscriber Loop\nVersion 2 (DEPRECATED - REPLACED\nBY 238) [RFC4706]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(232, 0, 0, 231, 'macSecControlledIF', 'MACSecControlled [Paul_Congdon]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(233, 0, 0, 232, 'macSecUncontrolledIF', 'MACSecUncontrolled [Paul_Congdon]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(234, 0, 0, 233, 'aviciOpticalEther', 'Avici Optical Ethernet Aggregate [Somen_Bhattacharya]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(235, 0, 0, 234, 'atmbond', 'atmbond [https://www.itu.int/rec/T-REC-G.998.1-200501-I/en]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(236, 0, 0, 235, 'voiceFGDOS', 'voice FGD Operator Services [Lizzie_Cheung]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(237, 0, 0, 236, 'mocaVersion1', 'MultiMedia over Coax Alliance [Ladd_Wardani]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(238, 0, 0, 237, 'ieee80216WMAN', 'IEEE 802.16 WMAN interface [http://standards.ieee.org/getieee802/802.16.html]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(239, 0, 0, 238, 'adsl2plus', 'Asymmetric Digital Subscriber Loop\nVersion 2 -- Version 2 Plus and all\nvariants [RFC4706]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(240, 0, 0, 239, 'dvbRcsMacLayer', 'DVB-RCS MAC Layer [RFC5728][ETSI EN 301 790][https://web.archive.org/web/20181229131835/http://satlabs.org/pdf/SatLabs_System_Recommendations_v2.0_M&#38;C.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(241, 0, 0, 240, 'dvbTdm', 'DVB Satellite TDM [RFC5728][ETSI EN 300 421][ETSI EN 302 307][https://web.archive.org/web/20181229131835/http://satlabs.org/pdf/SatLabs_System_Recommendations_v2.0_M&#38;C.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(242, 0, 0, 241, 'dvbRcsTdma', 'DVB-RCS TDMA [RFC5728][ETSI EN 301 790][ETSI EN 300 421][https://web.archive.org/web/20181229131835/http://satlabs.org/pdf/SatLabs_System_Recommendations_v2.0_M&#38;C.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(243, 0, 0, 242, 'x86Laps', 'LAPS based on ITU-T X.86/Y.1323 [Orly_Nicklass][http://grouper.ieee.org/groups/802/3/ad_hoc/etholaps/public/docs/opening_report_0301.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(244, 0, 0, 243, 'wwanPP', '3GPP WWAN [Gabriel_Montenegro][https://www.3gpp.org/ftp/specs/archive/23_series/23.060/23060-740.zip]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(245, 0, 0, 244, 'wwanPP2', '3GPP2 WWAN [Gabriel_Montenegro][http://www.3gpp2.org/Public_html/Specs/C.S0017-005-A_v1.0_040617.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(246, 0, 0, 245, 'voiceEBS', 'voice P-phone EBS physical interface [Tom_Chou]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(247, 0, 0, 246, 'ifPwType', 'Pseudowire interface type [RFC5601]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(248, 0, 0, 247, 'ILAN', 'Internal LAN on a bridge per IEEE\n802.1ap [Glenn_Parsons][http://www.ieee802.org/1/files/private/ap-drafts/d3/802-1ap-D3-4.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(249, 0, 0, 248, 'PIP', 'Provider Instance Port on a bridge\nper IEEE 802.1ah PBB [Glenn_Parsons][http://www.ieee802.org/1/files/private/ah-drafts/d4/802-1ah-d4-2.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(250, 0, 0, 249, 'aluELP', 'Alcatel-Lucent Ethernet Link Protection [Xiaohua_Ma]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(251, 0, 0, 250, 'gpon', 'Gigabit-capable passive optical networks\n(G-PON)  as per ITU-T G.948 [Hyeri_Koh]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(252, 0, 0, 251, 'vdsl2', 'Very high speed digital subscriber\nline Version 2 (as per ITU-T Recommendation\nG.993.2) [Markus_Freudenberger][RFC5650]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(253, 0, 0, 252, 'capwapDot11Profile', 'WLAN Profile Interface [RFC5834]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(254, 0, 0, 253, 'capwapDot11Bss', 'WLAN BSS Interface [RFC5834]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(255, 0, 0, 254, 'capwapWtpVirtualRadio', 'WTP Virtual Radio Interface [RFC5833]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(256, 0, 0, 255, 'bits', 'bitsport [Du_Feng]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(257, 0, 0, 256, 'docsCableUpstreamRfPort', 'DOCSIS CATV Upstream RF\nPort [Michael_Patrick][https://www.cablelabs.com/specifications/CM-SP-EQAM-PMI-I01-081209.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(258, 0, 0, 257, 'cableDownstreamRfPort', 'CATV downstream RF port [Michael_Patrick]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(259, 0, 0, 258, 'vmwareVirtualNic', 'VMware Virtual Network Interface [Mike_MacFaden]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(260, 0, 0, 259, 'ieee802154', 'IEEE 802.15.4 WPAN interface [Juergen_Schoenwaelde][\"IEEE Std. 802.15.4-2006\", October 2006.]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(261, 0, 0, 260, 'otnOdu', 'OTN Optical Data Unit [Jim_Vance][https://www.itu.int/ITU-T/studygroups/com15/otn/OTNtutorial.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(262, 0, 0, 261, 'otnOtu', 'OTN Optical channel Transport Unit [Jim_Vance][https://www.itu.int/ITU-T/studygroups/com15/otn/OTNtutorial.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(263, 0, 0, 262, 'ifVfiType', 'VPLS Forwarding Instance Interface\nType [Manas_Pati]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(264, 0, 0, 263, 'g9981', 'G.998.1 bonded interface [RFC6768][RFC Errata 3591]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(265, 0, 0, 264, 'g9982', 'G.998.2 bonded interface [RFC6767][RFC Errata 3589]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(266, 0, 0, 265, 'g9983', 'G.998.3 bonded interface [RFC6766][RFC Errata 3588]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(267, 0, 0, 266, 'aluEpon (E-PON)', 'Ethernet Passive Optical Networks [Karel_Meijfroidt]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(268, 0, 0, 267, 'aluEponOnu', 'EPON Optical Network Unit [Karel_Meijfroidt]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(269, 0, 0, 268, 'aluEponPhysicalUni', 'EPON physical User to Network\ninterface [Karel_Meijfroidt]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(270, 0, 0, 269, 'aluEponLogicalLink', 'The emulation of a point-to-point\nlink over the EPON layer [Karel_Meijfroidt]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(271, 0, 0, 270, 'aluGponOnu', 'GPON Optical Network Unit [Karel_Meijfroidt][https://www.itu.int/rec/T-REC-G.984.2/en]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(272, 0, 0, 271, 'aluGponPhysicalUni', 'GPON physical User to Network\ninterface [Karel_Meijfroidt][https://www.itu.int/rec/T-REC-G.984.2/en]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(273, 0, 0, 272, 'vmwareNicTeam', 'VMware NIC Team [Michael_MacFaden][https://www.vmware.com/pdf/esx2_NIC_Teaming.pdf]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(274, 0, 0, 273, 'Reserved', 'The corresponding transmission value\nis allocated according to the following\nreference. [RFC6825]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(275, 0, 0, 274, 'Reserved', 'The corresponding transmission value\nis allocated according to the following reference. [RFC7257]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(276, 0, 0, 275, 'Reserved', 'The corresponding transmission value\nis allocated according to the following reference. [RFC7257]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(277, 0, 0, 276, 'Reserved', 'The corresponding transmission value\nis allocated according to the following reference. [RFC7257]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(278, 0, 0, 277, 'docsOfdmDownstream', 'CATV Downstream OFDM interface [https://www.cablelabs.com/specification/cable-modem-operations-support-system-interface-specification][Miguel_O_Alvarez]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(279, 0, 0, 278, 'docsOfdmaUpstream', 'CATV Upstream OFDMA interface [https://www.cablelabs.com/specification/cable-modem-operations-support-system-interface-specification][Miguel_O_Alvarez]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(280, 0, 0, 279, 'gfast', 'G.fast port [ITU-T G.9701]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(281, 0, 0, 280, 'sdci', 'SDCI (IO-Link) [IEC 61131-9 Edition 1.0 2013-09][Markus_Rentschler]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(282, 0, 0, 281, 'xboxWireless', 'Xbox wireless [Brandon_Jiang]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(283, 0, 0, 282, 'fastdsl', 'FastDSL [BBF TR-355][Broadband_Forum]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(284, 0, 0, 283, 'docsCableScte55d1FwdOob', 'Cable SCTE 55-1 OOB Forward Channel [https://www.scte.org/documents/pdf/Standards/ANSI_SCTE-55-1-2009.pdf][Brian_Hedstrom]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(285, 0, 0, 284, 'docsCableScte55d1RetOob', 'Cable SCTE 55-1 OOB Return Channel [https://www.scte.org/documents/pdf/Standards/ANSI_SCTE-55-1-2009.pdf][Brian_Hedstrom]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(286, 0, 0, 285, 'docsCableScte55d2DsOob', 'Cable SCTE 55-2 OOB Downstream Channel [https://web.archive.org/web/20190822104256/http://www.scte.org/documents/pdf/Standards/ANSI_SCTE%2055-2%202008.pdf][Brian_Hedstrom]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(287, 0, 0, 286, 'docsCableScte55d2UsOob', 'Cable SCTE 55-2 OOB Upstream Channel [https://web.archive.org/web/20190822104256/http://www.scte.org/documents/pdf/Standards/ANSI_SCTE%2055-2%202008.pdf][Brian_Hedstrom]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(288, 0, 0, 287, 'docsCableNdf', 'Cable Narrowband Digital Forward [http://www.cablelabs.com/wp-content/uploads/specdocs/CM-SP-R-OOB-I04-160923.pdf][Brian_Hedstrom]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(289, 0, 0, 288, 'docsCableNdr', 'Cable Narrowband Digital Return [http://www.cablelabs.com/wp-content/uploads/specdocs/CM-SP-R-OOB-I04-160923.pdf][Brian_Hedstrom]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(290, 0, 0, 289, 'ptm', 'Packet Transfer Mode [ITU-T G.993.1, Annex H][ITU-T G.993.2][ITU-T G.9701][Broadband_Forum]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(291, 0, 0, 290, 'ghn', 'G.hn port [ITU-T G.9961][Broadband_Forum]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(292, 0, 0, 291, 'otnOtsi', 'Optical Tributary Signal [ITU-T G.959.1][Koteswara_Boyapati]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(293, 0, 0, 292, 'otnOtuc', 'OTN OTUCn [ITU-T G.709/Y.1331][Koteswara_Boyapati]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(294, 0, 0, 293, 'otnOduc', 'OTN ODUC [ITU-T G.709][Koteswara_Boyapati]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(295, 0, 0, 294, 'otnOtsig', 'OTN OTUC Signal [ITU-T G.709][Koteswara_Boyapati]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(296, 0, 0, 295, 'microwaveCarrierTermination', 'air interface of a single microwave carrier [RFC8561]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(297, 0, 0, 296, 'microwaveRadioLinkTerminal', 'radio link interface for one or several aggregated microwave carriers [RFC8561]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(298, 0, 0, 297, 'ieee8021axDrni', 'IEEE 802.1AX Distributed Resilient Network Interface [IEEE 802.1AX-Rev-d2-0][John_Messenger]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(299, 0, 0, 298, 'ax25', 'AX.25 network interfaces [AX.25 Link Access Protocol for Amateur Packet Radio version 2.2][Iain_Learmonth]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(300, 0, 0, 299, 'ieee19061nanocom', 'Nanoscale and Molecular Communication [IEEE 1906.1-2015][Stephen_F_Bush]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');
REPLACE INTO `glpi_networkporttypes` (`id`, `entities_id`, `is_recursive`, `value_decimal`, `name`, `comment`, `is_importable`, `instantiation_type`, `date_creation`, `date_mod`) VALUES(301, 0, 0, 300, 'cpri', 'Common Public Radio Interface [CPRI v7.0][Renwang_Liu]', 0, NULL, '2023-03-17 19:45:27', '2023-03-17 19:45:27');

--
-- Volcado de datos para la tabla `glpi_networks`
--

REPLACE INTO `glpi_networks` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'Network1', 'CommentNetwork1', '2023-03-19 19:17:17', '2023-03-19 19:17:17');

--
-- Volcado de datos para la tabla `glpi_notifications`
--

REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(1, 'Alert Tickets not closed', 0, 'Ticket', 'alertnotclosed', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(2, 'New Ticket', 0, 'Ticket', 'new', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(3, 'Update Ticket', 0, 'Ticket', 'update', NULL, 1, 0, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(4, 'Close Ticket', 0, 'Ticket', 'closed', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(5, 'Add Followup', 0, 'Ticket', 'add_followup', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(6, 'Add Task', 0, 'Ticket', 'add_task', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(7, 'Update Followup', 0, 'Ticket', 'update_followup', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(8, 'Update Task', 0, 'Ticket', 'update_task', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(9, 'Delete Followup', 0, 'Ticket', 'delete_followup', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(10, 'Delete Task', 0, 'Ticket', 'delete_task', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(11, 'Resolve ticket', 0, 'Ticket', 'solved', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(12, 'Ticket Validation', 0, 'Ticket', 'validation', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(13, 'New Reservation', 0, 'Reservation', 'new', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(14, 'Update Reservation', 0, 'Reservation', 'update', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(15, 'Delete Reservation', 0, 'Reservation', 'delete', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(16, 'Alert Reservation', 0, 'Reservation', 'alert', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(17, 'Contract Notice', 0, 'Contract', 'notice', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(18, 'Contract End', 0, 'Contract', 'end', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(19, 'MySQL Synchronization', 0, 'DBConnection', 'desynchronization', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(20, 'Cartridges', 0, 'CartridgeItem', 'alert', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(21, 'Consumables', 0, 'ConsumableItem', 'alert', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(22, 'Infocoms', 0, 'Infocom', 'alert', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(23, 'Software Licenses', 0, 'SoftwareLicense', 'alert', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(24, 'Ticket Recall', 0, 'Ticket', 'recall', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(25, 'Password Forget', 0, 'User', 'passwordforget', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(26, 'Ticket Satisfaction', 0, 'Ticket', 'satisfaction', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(27, 'Item not unique', 0, 'FieldUnicity', 'refuse', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(28, 'CronTask Watcher', 0, 'CronTask', 'alert', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(29, 'New Problem', 0, 'Problem', 'new', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(30, 'Update Problem', 0, 'Problem', 'update', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(31, 'Resolve Problem', 0, 'Problem', 'solved', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(32, 'Add Task', 0, 'Problem', 'add_task', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(33, 'Update Task', 0, 'Problem', 'update_task', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(34, 'Delete Task', 0, 'Problem', 'delete_task', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(35, 'Close Problem', 0, 'Problem', 'closed', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(36, 'Delete Problem', 0, 'Problem', 'delete', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(37, 'Ticket Validation Answer', 0, 'Ticket', 'validation_answer', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(38, 'Contract End Periodicity', 0, 'Contract', 'periodicity', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(39, 'Contract Notice Periodicity', 0, 'Contract', 'periodicitynotice', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(40, 'Planning recall', 0, 'PlanningRecall', 'planningrecall', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(41, 'Delete Ticket', 0, 'Ticket', 'delete', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(42, 'New Change', 0, 'Change', 'new', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(43, 'Update Change', 0, 'Change', 'update', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(44, 'Resolve Change', 0, 'Change', 'solved', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(45, 'Add Task', 0, 'Change', 'add_task', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(46, 'Update Task', 0, 'Change', 'update_task', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(47, 'Delete Task', 0, 'Change', 'delete_task', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(48, 'Close Change', 0, 'Change', 'closed', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(49, 'Delete Change', 0, 'Change', 'delete', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(50, 'Ticket Satisfaction Answer', 0, 'Ticket', 'replysatisfaction', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(51, 'Receiver errors', 0, 'MailCollector', 'error', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(52, 'New Project', 0, 'Project', 'new', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(53, 'Update Project', 0, 'Project', 'update', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(54, 'Delete Project', 0, 'Project', 'delete', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(55, 'New Project Task', 0, 'ProjectTask', 'new', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(56, 'Update Project Task', 0, 'ProjectTask', 'update', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(57, 'Delete Project Task', 0, 'ProjectTask', 'delete', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(58, 'Request Unlock Items', 0, 'ObjectLock', 'unlock', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(59, 'New user in requesters', 0, 'Ticket', 'requester_user', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(60, 'New group in requesters', 0, 'Ticket', 'requester_group', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(61, 'New user in observers', 0, 'Ticket', 'observer_user', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(62, 'New group in observers', 0, 'Ticket', 'observer_group', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(63, 'New user in assignees', 0, 'Ticket', 'assign_user', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(64, 'New group in assignees', 0, 'Ticket', 'assign_group', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(65, 'New supplier in assignees', 0, 'Ticket', 'assign_supplier', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(66, 'Saved searches', 0, 'SavedSearch_Alert', 'alert', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(67, 'Certificates', 0, 'Certificate', 'alert', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(68, 'Alert expired domains', 0, 'Domain', 'ExpiredDomains', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(69, 'Alert domains close expiries', 0, 'Domain', 'DomainsWhichExpire', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(70, 'Password expires alert', 0, 'User', 'passwordexpires', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(71, 'Check plugin updates', 0, 'Glpi\\Marketplace\\Controller', 'checkpluginsupdate', NULL, 1, 1, NULL, NULL, 1);
REPLACE INTO `glpi_notifications` (`id`, `name`, `entities_id`, `itemtype`, `event`, `comment`, `is_recursive`, `is_active`, `date_mod`, `date_creation`, `allow_response`) VALUES(72, 'New user mentionned', 0, 'Ticket', 'user_mention', NULL, 1, 1, NULL, NULL, 1);

--
-- Volcado de datos para la tabla `glpi_notifications_notificationtemplates`
--

REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(1, 1, 'mailing', 6);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(2, 2, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(3, 3, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(4, 4, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(5, 5, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(6, 6, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(7, 7, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(8, 8, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(9, 9, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(10, 10, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(11, 11, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(12, 12, 'mailing', 7);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(13, 13, 'mailing', 2);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(14, 14, 'mailing', 2);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(15, 15, 'mailing', 2);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(16, 16, 'mailing', 3);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(17, 17, 'mailing', 12);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(18, 18, 'mailing', 12);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(19, 19, 'mailing', 1);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(20, 20, 'mailing', 8);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(21, 21, 'mailing', 9);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(22, 22, 'mailing', 10);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(23, 23, 'mailing', 11);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(24, 24, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(25, 25, 'mailing', 13);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(26, 26, 'mailing', 14);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(27, 27, 'mailing', 15);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(28, 28, 'mailing', 16);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(29, 29, 'mailing', 17);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(30, 30, 'mailing', 17);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(31, 31, 'mailing', 17);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(32, 32, 'mailing', 17);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(33, 33, 'mailing', 17);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(34, 34, 'mailing', 17);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(35, 35, 'mailing', 17);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(36, 36, 'mailing', 17);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(37, 37, 'mailing', 7);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(38, 38, 'mailing', 12);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(39, 39, 'mailing', 12);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(40, 40, 'mailing', 18);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(41, 41, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(42, 42, 'mailing', 19);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(43, 43, 'mailing', 19);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(44, 44, 'mailing', 19);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(45, 45, 'mailing', 19);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(46, 46, 'mailing', 19);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(47, 47, 'mailing', 19);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(48, 48, 'mailing', 19);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(49, 49, 'mailing', 19);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(50, 50, 'mailing', 14);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(51, 51, 'mailing', 20);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(52, 52, 'mailing', 21);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(53, 53, 'mailing', 21);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(54, 54, 'mailing', 21);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(55, 55, 'mailing', 22);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(56, 56, 'mailing', 22);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(57, 57, 'mailing', 22);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(58, 58, 'mailing', 23);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(59, 59, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(60, 60, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(61, 61, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(62, 62, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(63, 63, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(64, 64, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(65, 65, 'mailing', 4);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(66, 66, 'mailing', 24);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(67, 67, 'mailing', 25);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(68, 68, 'mailing', 26);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(69, 69, 'mailing', 26);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(70, 70, 'mailing', 27);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(71, 71, 'mailing', 28);
REPLACE INTO `glpi_notifications_notificationtemplates` (`id`, `notifications_id`, `mode`, `notificationtemplates_id`) VALUES(72, 72, 'mailing', 4);

--
-- Volcado de datos para la tabla `glpi_notificationtargets`
--

REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(1, 3, 1, 13);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(2, 1, 1, 13);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(3, 3, 2, 2);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(4, 1, 1, 2);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(5, 1, 1, 3);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(6, 1, 1, 5);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(7, 1, 1, 4);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(8, 2, 1, 3);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(9, 4, 1, 3);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(10, 3, 1, 2);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(11, 3, 1, 3);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(12, 3, 1, 5);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(13, 3, 1, 4);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(14, 1, 1, 19);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(15, 14, 1, 12);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(16, 3, 1, 14);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(17, 1, 1, 14);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(18, 3, 1, 15);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(19, 1, 1, 15);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(20, 1, 1, 6);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(21, 3, 1, 6);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(22, 1, 1, 7);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(23, 3, 1, 7);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(24, 1, 1, 8);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(25, 3, 1, 8);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(26, 1, 1, 9);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(27, 3, 1, 9);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(28, 1, 1, 10);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(29, 3, 1, 10);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(30, 1, 1, 11);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(31, 3, 1, 11);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(32, 19, 1, 25);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(33, 3, 1, 26);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(34, 21, 1, 2);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(35, 21, 1, 3);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(36, 21, 1, 5);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(37, 21, 1, 4);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(38, 21, 1, 6);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(39, 21, 1, 7);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(40, 21, 1, 8);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(41, 21, 1, 9);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(42, 21, 1, 10);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(43, 21, 1, 11);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(46, 1, 1, 28);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(47, 3, 1, 29);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(48, 1, 1, 29);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(49, 21, 1, 29);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(50, 2, 1, 30);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(51, 4, 1, 30);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(52, 3, 1, 30);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(53, 1, 1, 30);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(54, 21, 1, 30);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(55, 3, 1, 31);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(56, 1, 1, 31);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(57, 21, 1, 31);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(58, 3, 1, 32);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(59, 1, 1, 32);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(60, 21, 1, 32);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(61, 3, 1, 33);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(62, 1, 1, 33);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(63, 21, 1, 33);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(64, 3, 1, 34);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(65, 1, 1, 34);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(66, 21, 1, 34);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(67, 3, 1, 35);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(68, 1, 1, 35);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(69, 21, 1, 35);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(70, 3, 1, 36);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(71, 1, 1, 36);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(72, 21, 1, 36);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(73, 14, 1, 37);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(74, 3, 1, 40);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(75, 1, 1, 41);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(76, 3, 1, 42);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(77, 1, 1, 42);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(78, 21, 1, 42);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(79, 2, 1, 43);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(80, 4, 1, 43);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(81, 3, 1, 43);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(82, 1, 1, 43);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(83, 21, 1, 43);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(84, 3, 1, 44);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(85, 1, 1, 44);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(86, 21, 1, 44);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(87, 3, 1, 45);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(88, 1, 1, 45);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(89, 21, 1, 45);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(90, 3, 1, 46);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(91, 1, 1, 46);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(92, 21, 1, 46);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(93, 3, 1, 47);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(94, 1, 1, 47);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(95, 21, 1, 47);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(96, 3, 1, 48);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(97, 1, 1, 48);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(98, 21, 1, 48);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(99, 3, 1, 49);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(100, 1, 1, 49);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(101, 21, 1, 49);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(102, 3, 1, 50);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(103, 2, 1, 50);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(104, 1, 1, 51);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(105, 27, 1, 52);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(106, 1, 1, 52);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(107, 28, 1, 52);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(108, 27, 1, 53);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(109, 1, 1, 53);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(110, 28, 1, 53);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(111, 27, 1, 54);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(112, 1, 1, 54);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(113, 28, 1, 54);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(114, 31, 1, 55);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(115, 1, 1, 55);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(116, 32, 1, 55);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(117, 31, 1, 56);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(118, 1, 1, 56);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(119, 32, 1, 56);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(120, 31, 1, 57);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(121, 1, 1, 57);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(122, 32, 1, 57);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(123, 19, 1, 58);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(124, 3, 1, 59);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(125, 13, 1, 60);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(126, 21, 1, 61);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(127, 20, 1, 62);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(128, 2, 1, 63);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(129, 9, 1, 64);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(130, 8, 1, 65);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(131, 19, 1, 66);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(132, 5, 1, 67);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(133, 23, 1, 67);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(134, 5, 1, 68);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(135, 23, 1, 68);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(136, 5, 1, 69);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(137, 23, 1, 69);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(138, 19, 1, 70);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(139, 1, 1, 71);
REPLACE INTO `glpi_notificationtargets` (`id`, `items_id`, `type`, `notifications_id`) VALUES(140, 39, 1, 72);

--
-- Volcado de datos para la tabla `glpi_notificationtemplates`
--

REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(1, 'MySQL Synchronization', 'DBConnection', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(2, 'Reservations', 'Reservation', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(3, 'Alert Reservation', 'Reservation', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(4, 'Tickets', 'Ticket', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(5, 'Tickets (Simple)', 'Ticket', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(6, 'Alert Tickets not closed', 'Ticket', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(7, 'Tickets Validation', 'Ticket', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(8, 'Cartridges', 'CartridgeItem', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(9, 'Consumables', 'ConsumableItem', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(10, 'Infocoms', 'Infocom', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(11, 'Licenses', 'SoftwareLicense', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(12, 'Contracts', 'Contract', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(13, 'Password Forget', 'User', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(14, 'Ticket Satisfaction', 'Ticket', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(15, 'Item not unique', 'FieldUnicity', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(16, 'CronTask', 'CronTask', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(17, 'Problems', 'Problem', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(18, 'Planning recall', 'PlanningRecall', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(19, 'Changes', 'Change', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(20, 'Receiver errors', 'MailCollector', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(21, 'Projects', 'Project', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(22, 'Project Tasks', 'ProjectTask', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(23, 'Unlock Item request', 'ObjectLock', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(24, 'Saved searches alerts', 'SavedSearch_Alert', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(25, 'Certificates', 'Certificate', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(26, 'Alert domains', 'Domain', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(27, 'Password expires alert', 'User', NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_notificationtemplates` (`id`, `name`, `itemtype`, `date_mod`, `comment`, `css`, `date_creation`) VALUES(28, 'Plugin updates', 'Glpi\\Marketplace\\Controller', NULL, NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_notificationtemplatetranslations`
--

REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(1, 1, '', '##lang.dbconnection.title##', '##lang.dbconnection.delay## : ##dbconnection.delay##', '&lt;p&gt;##lang.dbconnection.delay## : ##dbconnection.delay##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(2, 2, '', '##reservation.action##', '======================================================================\n##lang.reservation.user##: ##reservation.user##\n##lang.reservation.item.name##: ##reservation.itemtype## - ##reservation.item.name##\n##IFreservation.tech## ##lang.reservation.tech## ##reservation.tech## ##ENDIFreservation.tech##\n##lang.reservation.begin##: ##reservation.begin##\n##lang.reservation.end##: ##reservation.end##\n##lang.reservation.comment##: ##reservation.comment##\n======================================================================', '&lt;!-- description{ color: inherit; background: #ebebeb;border-style: solid;border-color: #8d8d8d; border-width: 0px 1px 1px 0px; } --&gt;\n&lt;p&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.reservation.user##:&lt;/span&gt;##reservation.user##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.reservation.item.name##:&lt;/span&gt;##reservation.itemtype## - ##reservation.item.name##&lt;br /&gt;##IFreservation.tech## ##lang.reservation.tech## ##reservation.tech####ENDIFreservation.tech##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.reservation.begin##:&lt;/span&gt; ##reservation.begin##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.reservation.end##:&lt;/span&gt;##reservation.end##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.reservation.comment##:&lt;/span&gt; ##reservation.comment##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(3, 3, '', '##reservation.action##  ##reservation.entity##', '##lang.reservation.entity## : ##reservation.entity##\n\n\n##FOREACHreservations##\n##lang.reservation.itemtype## : ##reservation.itemtype##\n\n ##lang.reservation.item## : ##reservation.item##\n\n ##reservation.url##\n\n ##ENDFOREACHreservations##', '&lt;p&gt;##lang.reservation.entity## : ##reservation.entity## &lt;br /&gt; &lt;br /&gt;\n##FOREACHreservations## &lt;br /&gt;##lang.reservation.itemtype## :  ##reservation.itemtype##&lt;br /&gt;\n ##lang.reservation.item## :  ##reservation.item##&lt;br /&gt; &lt;br /&gt;\n &lt;a href=\"##reservation.url##\"&gt; ##reservation.url##&lt;/a&gt;&lt;br /&gt;\n ##ENDFOREACHreservations##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(4, 4, '', '##ticket.action## ##ticket.title##', ' ##IFticket.storestatus=5##\n ##lang.ticket.url## : ##ticket.urlapprove##\n ##lang.ticket.autoclosewarning##\n ##lang.ticket.solvedate## : ##ticket.solvedate##\n ##lang.ticket.solution.type## : ##ticket.solution.type##\n ##lang.ticket.solution.description## : ##ticket.solution.description## ##ENDIFticket.storestatus##\n ##ELSEticket.storestatus## ##lang.ticket.url## : ##ticket.url## ##ENDELSEticket.storestatus##\n\n ##lang.ticket.description##\n\n ##lang.ticket.title## : ##ticket.title##\n ##lang.ticket.authors## : ##IFticket.authors## ##ticket.authors## ##ENDIFticket.authors## ##ELSEticket.authors##--##ENDELSEticket.authors##\n ##lang.ticket.creationdate## : ##ticket.creationdate##\n ##lang.ticket.closedate## : ##ticket.closedate##\n ##lang.ticket.requesttype## : ##ticket.requesttype##\n##lang.ticket.item.name## :\n\n##FOREACHitems##\n\n ##IFticket.itemtype##\n  ##ticket.itemtype## - ##ticket.item.name##\n  ##IFticket.item.model## ##lang.ticket.item.model## : ##ticket.item.model## ##ENDIFticket.item.model##\n  ##IFticket.item.serial## ##lang.ticket.item.serial## : ##ticket.item.serial## ##ENDIFticket.item.serial##\n  ##IFticket.item.otherserial## ##lang.ticket.item.otherserial## : ##ticket.item.otherserial## ##ENDIFticket.item.otherserial##\n ##ENDIFticket.itemtype##\n\n##ENDFOREACHitems##\n##IFticket.assigntousers## ##lang.ticket.assigntousers## : ##ticket.assigntousers## ##ENDIFticket.assigntousers##\n ##lang.ticket.status## : ##ticket.status##\n##IFticket.assigntogroups## ##lang.ticket.assigntogroups## : ##ticket.assigntogroups## ##ENDIFticket.assigntogroups##\n ##lang.ticket.urgency## : ##ticket.urgency##\n ##lang.ticket.impact## : ##ticket.impact##\n ##lang.ticket.priority## : ##ticket.priority##\n##IFticket.user.email## ##lang.ticket.user.email## : ##ticket.user.email ##ENDIFticket.user.email##\n##IFticket.category## ##lang.ticket.category## : ##ticket.category## ##ENDIFticket.category## ##ELSEticket.category## ##lang.ticket.nocategoryassigned## ##ENDELSEticket.category##\n ##lang.ticket.content## : ##ticket.content##\n ##IFticket.storestatus=6##\n\n ##lang.ticket.solvedate## : ##ticket.solvedate##\n ##lang.ticket.solution.type## : ##ticket.solution.type##\n ##lang.ticket.solution.description## : ##ticket.solution.description##\n ##ENDIFticket.storestatus##\n\n##FOREACHtimelineitems##\n[##timelineitems.date##]\n##lang.timelineitems.author## ##timelineitems.author##\n##lang.timelineitems.description## ##timelineitems.description##\n##lang.timelineitems.date## ##timelineitems.date##\n##lang.timelineitems.position## ##timelineitems.position##\n##lang.timelineitems.type## ##timelineitems.type##\n##lang.timelineitems.typename## ##timelineitems.typename##\n##ENDFOREACHtimelineitems##\n\n##lang.ticket.numberoffollowups## : ##ticket.numberoffollowups##\n##lang.ticket.numberoftasks## : ##ticket.numberoftasks##', '&lt;!-- description{ color: inherit; background: #ebebeb; border-style: solid;border-color: #8d8d8d; border-width: 0px 1px 1px 0px; }    --&gt;\n&lt;div&gt;##IFticket.storestatus=5##&lt;/div&gt;\n&lt;div&gt;##lang.ticket.url## : &lt;a href=\"##ticket.urlapprove##\"&gt;##ticket.urlapprove##&lt;/a&gt; &lt;strong&gt;&#160;&lt;/strong&gt;&lt;/div&gt;\n&lt;div&gt;&lt;strong&gt;##lang.ticket.autoclosewarning##&lt;/strong&gt;&lt;/div&gt;\n&lt;div&gt;&lt;span style=\"color: #888888;\"&gt;&lt;strong&gt;&lt;span style=\"text-decoration: underline;\"&gt;##lang.ticket.solvedate##&lt;/span&gt;&lt;/strong&gt;&lt;/span&gt; : ##ticket.solvedate##&lt;br /&gt;&lt;span style=\"text-decoration: underline; color: #888888;\"&gt;&lt;strong&gt;##lang.ticket.solution.type##&lt;/strong&gt;&lt;/span&gt; : ##ticket.solution.type##&lt;br /&gt;&lt;span style=\"text-decoration: underline; color: #888888;\"&gt;&lt;strong&gt;##lang.ticket.solution.description##&lt;/strong&gt;&lt;/span&gt; : ##ticket.solution.description## ##ENDIFticket.storestatus##&lt;/div&gt;\n&lt;div&gt;##ELSEticket.storestatus## ##lang.ticket.url## : &lt;a href=\"##ticket.url##\"&gt;##ticket.url##&lt;/a&gt; ##ENDELSEticket.storestatus##&lt;/div&gt;\n&lt;p class=\"description b\"&gt;&lt;strong&gt;##lang.ticket.description##&lt;/strong&gt;&lt;/p&gt;\n&lt;p&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.title##&lt;/span&gt;&#160;:##ticket.title## &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.authors##&lt;/span&gt;&#160;:##IFticket.authors## ##ticket.authors## ##ENDIFticket.authors##    ##ELSEticket.authors##--##ENDELSEticket.authors## &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.creationdate##&lt;/span&gt;&#160;:##ticket.creationdate## &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.closedate##&lt;/span&gt;&#160;:##ticket.closedate## &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.requesttype##&lt;/span&gt;&#160;:##ticket.requesttype##&lt;br /&gt;\n&lt;br /&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.item.name##&lt;/span&gt;&#160;:\n&lt;p&gt;##FOREACHitems##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;##IFticket.itemtype## ##ticket.itemtype##&#160;- ##ticket.item.name## ##IFticket.item.model## ##lang.ticket.item.model## : ##ticket.item.model## ##ENDIFticket.item.model## ##IFticket.item.serial## ##lang.ticket.item.serial## : ##ticket.item.serial## ##ENDIFticket.item.serial## ##IFticket.item.otherserial## ##lang.ticket.item.otherserial## : ##ticket.item.otherserial## ##ENDIFticket.item.otherserial## ##ENDIFticket.itemtype## &lt;/div&gt;&lt;br /&gt;\n&lt;p&gt;##ENDFOREACHitems##&lt;/p&gt;\n##IFticket.assigntousers## &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.assigntousers##&lt;/span&gt;&#160;: ##ticket.assigntousers## ##ENDIFticket.assigntousers##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.ticket.status## &lt;/span&gt;&#160;: ##ticket.status##&lt;br /&gt; ##IFticket.assigntogroups## &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.assigntogroups##&lt;/span&gt;&#160;: ##ticket.assigntogroups## ##ENDIFticket.assigntogroups##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.urgency##&lt;/span&gt;&#160;: ##ticket.urgency##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.impact##&lt;/span&gt;&#160;: ##ticket.impact##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.priority##&lt;/span&gt;&#160;: ##ticket.priority## &lt;br /&gt; ##IFticket.user.email##&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.user.email##&lt;/span&gt;&#160;: ##ticket.user.email ##ENDIFticket.user.email##    &lt;br /&gt; ##IFticket.category##&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.ticket.category## &lt;/span&gt;&#160;:##ticket.category## ##ENDIFticket.category## ##ELSEticket.category## ##lang.ticket.nocategoryassigned## ##ENDELSEticket.category##    &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.ticket.content##&lt;/span&gt;&#160;: ##ticket.content##&lt;/p&gt;\n&lt;br /&gt;##IFticket.storestatus=6##&lt;br /&gt;&lt;span style=\"text-decoration: underline;\"&gt;&lt;strong&gt;&lt;span style=\"color: #888888;\"&gt;##lang.ticket.solvedate##&lt;/span&gt;&lt;/strong&gt;&lt;/span&gt; : ##ticket.solvedate##&lt;br /&gt;&lt;span style=\"color: #888888;\"&gt;&lt;strong&gt;&lt;span style=\"text-decoration: underline;\"&gt;##lang.ticket.solution.type##&lt;/span&gt;&lt;/strong&gt;&lt;/span&gt; : ##ticket.solution.type##&lt;br /&gt;&lt;span style=\"text-decoration: underline; color: #888888;\"&gt;&lt;strong&gt;##lang.ticket.solution.description##&lt;/strong&gt;&lt;/span&gt; : ##ticket.solution.description##&lt;br /&gt;##ENDIFticket.storestatus##&lt;/p&gt;\n&lt;p&gt;##FOREACHtimelineitems##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;&lt;br /&gt;&lt;strong&gt; [##timelineitems.date##]&lt;/strong&gt;&lt;br /&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.timelineitems.author## &lt;/span&gt; &lt;span style=\"color: #000000; font-weight: bold; text-decoration: underline;\"&gt;##timelineitems.author##&lt;/span&gt;&lt;br /&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.timelineitems.description## &lt;/span&gt; &lt;span style=\"color: #000000; font-weight: bold; text-decoration: underline;\"&gt;##timelineitems.description##&lt;/span&gt;&lt;br /&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.timelineitems.date## &lt;/span&gt; &lt;span style=\"color: #000000; font-weight: bold; text-decoration: underline;\"&gt;##timelineitems.date##&lt;/span&gt;&lt;br /&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.timelineitems.position## &lt;/span&gt;&lt;span style=\"color: #000000; font-weight: bold; text-decoration: underline;\"&gt; ##timelineitems.position##&lt;/span&gt;&lt;/div&gt;\n&lt;div class=\"description b\"&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.timelineitems.type## &lt;/span&gt;&lt;span style=\"color: #000000; font-weight: bold; text-decoration: underline;\"&gt; ##timelineitems.type##&lt;/span&gt;&lt;/div&gt;\n&lt;div class=\"description b\"&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.timelineitems.typename## &lt;/span&gt; &lt;span style=\"color: #000000; font-weight: bold; text-decoration: underline;\"&gt;##timelineitems.typename##&lt;/span&gt;&lt;/div&gt;\n&lt;p&gt;##ENDFOREACHtimelineitems##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;##lang.ticket.numberoffollowups##&#160;: ##ticket.numberoffollowups##&lt;/div&gt;\n&lt;div class=\"description b\"&gt;##lang.ticket.numberoftasks##&#160;: ##ticket.numberoftasks##&lt;/div&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(5, 12, '', '##contract.action##  ##contract.entity##', '##lang.contract.entity## : ##contract.entity##\n\n##FOREACHcontracts##\n##lang.contract.name## : ##contract.name##\n##lang.contract.number## : ##contract.number##\n##lang.contract.time## : ##contract.time##\n##IFcontract.type####lang.contract.type## : ##contract.type####ENDIFcontract.type##\n##contract.url##\n##ENDFOREACHcontracts##', '&lt;p&gt;##lang.contract.entity## : ##contract.entity##&lt;br /&gt;\n&lt;br /&gt;##FOREACHcontracts##&lt;br /&gt;##lang.contract.name## :\n##contract.name##&lt;br /&gt;\n##lang.contract.number## : ##contract.number##&lt;br /&gt;\n##lang.contract.time## : ##contract.time##&lt;br /&gt;\n##IFcontract.type####lang.contract.type## : ##contract.type##\n##ENDIFcontract.type##&lt;br /&gt;\n&lt;a href=\"##contract.url##\"&gt;\n##contract.url##&lt;/a&gt;&lt;br /&gt;\n##ENDFOREACHcontracts##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(6, 5, '', '##ticket.action## ##ticket.title##', '##lang.ticket.url## : ##ticket.url##\n\n##lang.ticket.description##\n\n\n##lang.ticket.title##  :##ticket.title##\n\n##lang.ticket.authors##  :##IFticket.authors##\n##ticket.authors## ##ENDIFticket.authors##\n##ELSEticket.authors##--##ENDELSEticket.authors##\n\n##IFticket.category## ##lang.ticket.category##  :##ticket.category##\n##ENDIFticket.category## ##ELSEticket.category##\n##lang.ticket.nocategoryassigned## ##ENDELSEticket.category##\n\n##lang.ticket.content##  : ##ticket.content##\n##IFticket.itemtype##\n##lang.ticket.item.name##  : ##ticket.itemtype## - ##ticket.item.name##\n##ENDIFticket.itemtype##', '&lt;div&gt;##lang.ticket.url## : &lt;a href=\"##ticket.url##\"&gt;\n##ticket.url##&lt;/a&gt;&lt;/div&gt;\n&lt;div class=\"description b\"&gt;\n##lang.ticket.description##&lt;/div&gt;\n&lt;p&gt;&lt;span\nstyle=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;\n##lang.ticket.title##&lt;/span&gt;&#160;:##ticket.title##\n&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;\n##lang.ticket.authors##&lt;/span&gt;\n##IFticket.authors## ##ticket.authors##\n##ENDIFticket.authors##\n##ELSEticket.authors##--##ENDELSEticket.authors##\n&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;\n&lt;/span&gt;&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; &lt;/span&gt;\n##IFticket.category##&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;\n##lang.ticket.category## &lt;/span&gt;&#160;:##ticket.category##\n##ENDIFticket.category## ##ELSEticket.category##\n##lang.ticket.nocategoryassigned## ##ENDELSEticket.category##\n&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;\n##lang.ticket.content##&lt;/span&gt;&#160;:\n##ticket.content##&lt;br /&gt;##IFticket.itemtype##\n&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;\n##lang.ticket.item.name##&lt;/span&gt;&#160;:\n##ticket.itemtype## - ##ticket.item.name##\n##ENDIFticket.itemtype##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(7, 7, '', '##ticket.action## ##ticket.title##', '##FOREACHvalidations##\n\n##IFvalidation.storestatus=2##\n##validation.submission.title##\n##lang.validation.commentsubmission## : ##validation.commentsubmission##\n##ENDIFvalidation.storestatus##\n##ELSEvalidation.storestatus## ##validation.answer.title## ##ENDELSEvalidation.storestatus##\n\n##lang.ticket.url## : ##ticket.urlvalidation##\n\n##IFvalidation.status## ##lang.validation.status## : ##validation.status## ##ENDIFvalidation.status##\n##IFvalidation.commentvalidation##\n##lang.validation.commentvalidation## : ##validation.commentvalidation##\n##ENDIFvalidation.commentvalidation##\n##ENDFOREACHvalidations##', '&lt;div&gt;##FOREACHvalidations##&lt;/div&gt;\n&lt;p&gt;##IFvalidation.storestatus=2##&lt;/p&gt;\n&lt;div&gt;##validation.submission.title##&lt;/div&gt;\n&lt;div&gt;##lang.validation.commentsubmission## : ##validation.commentsubmission##&lt;/div&gt;\n&lt;div&gt;##ENDIFvalidation.storestatus##&lt;/div&gt;\n&lt;div&gt;##ELSEvalidation.storestatus## ##validation.answer.title## ##ENDELSEvalidation.storestatus##&lt;/div&gt;\n&lt;div&gt;&lt;/div&gt;\n&lt;div&gt;\n&lt;div&gt;##lang.ticket.url## : &lt;a href=\"##ticket.urlvalidation##\"&gt; ##ticket.urlvalidation## &lt;/a&gt;&lt;/div&gt;\n&lt;/div&gt;\n&lt;p&gt;##IFvalidation.status## ##lang.validation.status## : ##validation.status## ##ENDIFvalidation.status##\n&lt;br /&gt; ##IFvalidation.commentvalidation##&lt;br /&gt; ##lang.validation.commentvalidation## :\n&#160; ##validation.commentvalidation##&lt;br /&gt; ##ENDIFvalidation.commentvalidation##\n&lt;br /&gt;##ENDFOREACHvalidations##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(8, 6, '', '##ticket.action## ##ticket.entity##', '##FOREACHtickets##\n##lang.ticket.authors##: ##ticket.authors##\n##lang.ticket.title##: ##ticket.title##\n##lang.ticket.priority##: ##ticket.priority##\n##lang.ticket.status##: ##ticket.status##\n##lang.ticket.attribution##: ##IFticket.assigntousers####ticket.assigntousers##\n##ENDIFticket.assigntousers####IFticket.assigntogroups##\n##ticket.assigntogroups## ##ENDIFticket.assigntogroups####IFticket.assigntosupplier##\n##ticket.assigntosupplier## ##ENDIFticket.assigntosupplier##\n##lang.ticket.creationdate##: ##ticket.creationdate##\n##lang.ticket.content##: ##ticket.content## ##ENDFOREACHtickets##', '&lt;table class=\"tab_cadre\" border=\"1\" cellspacing=\"2\" cellpadding=\"3\"&gt;\n&lt;tbody&gt;\n&lt;tr&gt;\n&lt;td style=\"text-align: left;\" width=\"auto\" bgcolor=\"#cccccc\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##lang.ticket.authors##&lt;/span&gt;&lt;/td&gt;\n&lt;td style=\"text-align: left;\" width=\"auto\" bgcolor=\"#cccccc\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##lang.ticket.title##&lt;/span&gt;&lt;/td&gt;\n&lt;td style=\"text-align: left;\" width=\"auto\" bgcolor=\"#cccccc\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##lang.ticket.priority##&lt;/span&gt;&lt;/td&gt;\n&lt;td style=\"text-align: left;\" width=\"auto\" bgcolor=\"#cccccc\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##lang.ticket.status##&lt;/span&gt;&lt;/td&gt;\n&lt;td style=\"text-align: left;\" width=\"auto\" bgcolor=\"#cccccc\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##lang.ticket.attribution##&lt;/span&gt;&lt;/td&gt;\n&lt;td style=\"text-align: left;\" width=\"auto\" bgcolor=\"#cccccc\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##lang.ticket.creationdate##&lt;/span&gt;&lt;/td&gt;\n&lt;td style=\"text-align: left;\" width=\"auto\" bgcolor=\"#cccccc\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##lang.ticket.content##&lt;/span&gt;##FOREACHtickets##&lt;/td&gt;\n&lt;/tr&gt;\n&lt;tr&gt;\n&lt;td width=\"auto\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##ticket.authors##&lt;/span&gt;&lt;/td&gt;\n&lt;td width=\"auto\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;&lt;a href=\"##ticket.url##\"&gt;##ticket.title##&lt;/a&gt;&lt;/span&gt;&lt;/td&gt;\n&lt;td width=\"auto\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##ticket.priority##&lt;/span&gt;&lt;/td&gt;\n&lt;td width=\"auto\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##ticket.status##&lt;/span&gt;&lt;/td&gt;\n&lt;td width=\"auto\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##IFticket.assigntousers####ticket.assigntousers##&lt;br /&gt;##ENDIFticket.assigntousers####IFticket.assigntogroups##&lt;br /&gt;##ticket.assigntogroups## ##ENDIFticket.assigntogroups####IFticket.assigntosupplier##&lt;br /&gt;##ticket.assigntosupplier## ##ENDIFticket.assigntosupplier##&lt;/span&gt;&lt;/td&gt;\n&lt;td width=\"auto\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##ticket.creationdate##&lt;/span&gt;&lt;/td&gt;\n&lt;td width=\"auto\"&gt;&lt;span style=\"font-size: 11px; text-align: left;\"&gt;##ticket.content##&lt;/span&gt;##ENDFOREACHtickets##&lt;/td&gt;\n&lt;/tr&gt;\n&lt;/tbody&gt;\n&lt;/table&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(9, 9, '', '##consumable.action##  ##consumable.entity##', '##lang.consumable.entity## : ##consumable.entity##\n\n\n##FOREACHconsumables##\n##lang.consumable.item## : ##consumable.item##\n\n\n##lang.consumable.reference## : ##consumable.reference##\n\n##lang.consumable.remaining## : ##consumable.remaining##\n##lang.consumable.stock_target## : ##consumable.stock_target##\n##lang.consumable.to_order## : ##consumable.to_order##\n\n##consumable.url##\n\n##ENDFOREACHconsumables##', '&lt;p&gt;\n##lang.consumable.entity## : ##consumable.entity##\n&lt;br /&gt; &lt;br /&gt;##FOREACHconsumables##\n&lt;br /&gt;##lang.consumable.item## : ##consumable.item##&lt;br /&gt;\n&lt;br /&gt;##lang.consumable.reference## : ##consumable.reference##&lt;br /&gt;\n##lang.consumable.remaining## : ##consumable.remaining##&lt;br /&gt;\n##lang.consumable.stock_target## : ##consumable.stock_target##&lt;br /&gt;\n##lang.consumable.to_order## : ##consumable.to_order##&lt;br /&gt;\n&lt;a href=\"##consumable.url##\"&gt; ##consumable.url##&lt;/a&gt;&lt;br /&gt;\n   ##ENDFOREACHconsumables##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(10, 8, '', '##cartridge.action##  ##cartridge.entity##', '##lang.cartridge.entity## : ##cartridge.entity##\n\n\n##FOREACHcartridges##\n##lang.cartridge.item## : ##cartridge.item##\n\n\n##lang.cartridge.reference## : ##cartridge.reference##\n\n##lang.cartridge.remaining## : ##cartridge.remaining##\n##lang.cartridge.stock_target## : ##cartridge.stock_target##\n##lang.cartridge.to_order## : ##cartridge.to_order##\n\n##cartridge.url##\n ##ENDFOREACHcartridges##', '&lt;p&gt;##lang.cartridge.entity## : ##cartridge.entity##\n&lt;br /&gt; &lt;br /&gt;##FOREACHcartridges##\n&lt;br /&gt;##lang.cartridge.item## :\n##cartridge.item##&lt;br /&gt; &lt;br /&gt;\n##lang.cartridge.reference## :\n##cartridge.reference##&lt;br /&gt;\n##lang.cartridge.remaining## :\n##cartridge.remaining##&lt;br /&gt;\n##lang.cartridge.stock_target## :\n##cartridge.stock_target##&lt;br /&gt;\n##lang.cartridge.to_order## :\n##cartridge.to_order##&lt;br /&gt;\n&lt;a href=\"##cartridge.url##\"&gt;\n##cartridge.url##&lt;/a&gt;&lt;br /&gt;\n##ENDFOREACHcartridges##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(11, 10, '', '##infocom.action##  ##infocom.entity##', '##lang.infocom.entity## : ##infocom.entity##\n\n\n##FOREACHinfocoms##\n\n##lang.infocom.itemtype## : ##infocom.itemtype##\n\n##lang.infocom.item## : ##infocom.item##\n\n\n##lang.infocom.expirationdate## : ##infocom.expirationdate##\n\n##infocom.url##\n ##ENDFOREACHinfocoms##', '&lt;p&gt;##lang.infocom.entity## : ##infocom.entity##\n&lt;br /&gt; &lt;br /&gt;##FOREACHinfocoms##\n&lt;br /&gt;##lang.infocom.itemtype## : ##infocom.itemtype##&lt;br /&gt;\n##lang.infocom.item## : ##infocom.item##&lt;br /&gt; &lt;br /&gt;\n##lang.infocom.expirationdate## : ##infocom.expirationdate##\n&lt;br /&gt; &lt;a href=\"##infocom.url##\"&gt;\n##infocom.url##&lt;/a&gt;&lt;br /&gt;\n##ENDFOREACHinfocoms##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(12, 11, '', '##license.action##  ##license.entity##', '##lang.license.entity## : ##license.entity##\n\n##FOREACHlicenses##\n\n##lang.license.item## : ##license.item##\n\n##lang.license.serial## : ##license.serial##\n\n##lang.license.expirationdate## : ##license.expirationdate##\n\n##license.url##\n ##ENDFOREACHlicenses##', '&lt;p&gt;\n##lang.license.entity## : ##license.entity##&lt;br /&gt;\n##FOREACHlicenses##\n&lt;br /&gt;##lang.license.item## : ##license.item##&lt;br /&gt;\n##lang.license.serial## : ##license.serial##&lt;br /&gt;\n##lang.license.expirationdate## : ##license.expirationdate##\n&lt;br /&gt; &lt;a href=\"##license.url##\"&gt; ##license.url##\n&lt;/a&gt;&lt;br /&gt; ##ENDFOREACHlicenses##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(13, 13, '', '##user.action##', '##user.realname## ##user.firstname##\n\n##lang.passwordforget.information##\n\n##lang.passwordforget.link## ##user.passwordforgeturl##', '&lt;p&gt;&lt;strong&gt;##user.realname## ##user.firstname##&lt;/strong&gt;&lt;/p&gt;\n&lt;p&gt;##lang.passwordforget.information##&lt;/p&gt;\n&lt;p&gt;##lang.passwordforget.link## &lt;a title=\"##user.passwordforgeturl##\" href=\"##user.passwordforgeturl##\"&gt;##user.passwordforgeturl##&lt;/a&gt;&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(14, 14, '', '##ticket.action## ##ticket.title##', '##lang.ticket.title## : ##ticket.title##\n\n##lang.ticket.closedate## : ##ticket.closedate##\n\n##lang.satisfaction.text## ##ticket.urlsatisfaction##', '&lt;p&gt;##lang.ticket.title## : ##ticket.title##&lt;/p&gt;\n&lt;p&gt;##lang.ticket.closedate## : ##ticket.closedate##&lt;/p&gt;\n&lt;p&gt;##lang.satisfaction.text## &lt;a href=\"##ticket.urlsatisfaction##\"&gt;##ticket.urlsatisfaction##&lt;/a&gt;&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(15, 15, '', '##lang.unicity.action##', '##lang.unicity.entity## : ##unicity.entity##\n\n##lang.unicity.itemtype## : ##unicity.itemtype##\n\n##lang.unicity.message## : ##unicity.message##\n\n##lang.unicity.action_user## : ##unicity.action_user##\n\n##lang.unicity.action_type## : ##unicity.action_type##\n\n##lang.unicity.date## : ##unicity.date##', '&lt;p&gt;##lang.unicity.entity## : ##unicity.entity##&lt;/p&gt;\n&lt;p&gt;##lang.unicity.itemtype## : ##unicity.itemtype##&lt;/p&gt;\n&lt;p&gt;##lang.unicity.message## : ##unicity.message##&lt;/p&gt;\n&lt;p&gt;##lang.unicity.action_user## : ##unicity.action_user##&lt;/p&gt;\n&lt;p&gt;##lang.unicity.action_type## : ##unicity.action_type##&lt;/p&gt;\n&lt;p&gt;##lang.unicity.date## : ##unicity.date##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(16, 16, '', '##crontask.action##', '##lang.crontask.warning##\n\n##FOREACHcrontasks##\n ##crontask.name## : ##crontask.description##\n\n##ENDFOREACHcrontasks##', '&lt;p&gt;##lang.crontask.warning##&lt;/p&gt;\n&lt;p&gt;##FOREACHcrontasks## &lt;br /&gt;&lt;a href=\"##crontask.url##\"&gt;##crontask.name##&lt;/a&gt; : ##crontask.description##&lt;br /&gt; &lt;br /&gt;##ENDFOREACHcrontasks##&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(17, 17, '', '##problem.action## ##problem.title##', '##IFproblem.storestatus=5##\n ##lang.problem.url## : ##problem.urlapprove##\n ##lang.problem.solvedate## : ##problem.solvedate##\n ##lang.problem.solution.type## : ##problem.solution.type##\n ##lang.problem.solution.description## : ##problem.solution.description## ##ENDIFproblem.storestatus##\n ##ELSEproblem.storestatus## ##lang.problem.url## : ##problem.url## ##ENDELSEproblem.storestatus##\n\n ##lang.problem.description##\n\n ##lang.problem.title##  :##problem.title##\n ##lang.problem.authors##  :##IFproblem.authors## ##problem.authors## ##ENDIFproblem.authors## ##ELSEproblem.authors##--##ENDELSEproblem.authors##\n ##lang.problem.creationdate##  :##problem.creationdate##\n ##IFproblem.assigntousers## ##lang.problem.assigntousers##  : ##problem.assigntousers## ##ENDIFproblem.assigntousers##\n ##lang.problem.status##  : ##problem.status##\n ##IFproblem.assigntogroups## ##lang.problem.assigntogroups##  : ##problem.assigntogroups## ##ENDIFproblem.assigntogroups##\n ##lang.problem.urgency##  : ##problem.urgency##\n ##lang.problem.impact##  : ##problem.impact##\n ##lang.problem.priority## : ##problem.priority##\n##IFproblem.category## ##lang.problem.category##  :##problem.category## ##ENDIFproblem.category## ##ELSEproblem.category## ##lang.problem.nocategoryassigned## ##ENDELSEproblem.category##\n ##lang.problem.content##  : ##problem.content##\n\n##IFproblem.storestatus=6##\n ##lang.problem.solvedate## : ##problem.solvedate##\n ##lang.problem.solution.type## : ##problem.solution.type##\n ##lang.problem.solution.description## : ##problem.solution.description##\n##ENDIFproblem.storestatus##\n ##lang.problem.numberoffollowups## : ##problem.numberoffollowups##\n\n##FOREACHfollowups##\n\n [##followup.date##] ##lang.followup.isprivate## : ##followup.isprivate##\n ##lang.followup.author## ##followup.author##\n ##lang.followup.description## ##followup.description##\n ##lang.followup.date## ##followup.date##\n ##lang.followup.requesttype## ##followup.requesttype##\n\n##ENDFOREACHfollowups##\n ##lang.problem.numberoftickets## : ##problem.numberoftickets##\n\n##FOREACHtickets##\n [##ticket.date##] ##lang.problem.title## : ##ticket.title##\n ##lang.problem.content## ##ticket.content##\n\n##ENDFOREACHtickets##\n ##lang.problem.numberoftasks## : ##problem.numberoftasks##\n\n##FOREACHtasks##\n [##task.date##]\n ##lang.task.author## ##task.author##\n ##lang.task.description## ##task.description##\n ##lang.task.time## ##task.time##\n ##lang.task.category## ##task.category##\n\n##ENDFOREACHtasks##\n', '&lt;p&gt;##IFproblem.storestatus=5##&lt;/p&gt;\n&lt;div&gt;##lang.problem.url## : &lt;a href=\"##problem.urlapprove##\"&gt;##problem.urlapprove##&lt;/a&gt;&lt;/div&gt;\n&lt;div&gt;&lt;span style=\"color: #888888;\"&gt;&lt;strong&gt;&lt;span style=\"text-decoration: underline;\"&gt;##lang.problem.solvedate##&lt;/span&gt;&lt;/strong&gt;&lt;/span&gt; : ##problem.solvedate##&lt;br /&gt;&lt;span style=\"text-decoration: underline; color: #888888;\"&gt;&lt;strong&gt;##lang.problem.solution.type##&lt;/strong&gt;&lt;/span&gt; : ##problem.solution.type##&lt;br /&gt;&lt;span style=\"text-decoration: underline; color: #888888;\"&gt;&lt;strong&gt;##lang.problem.solution.description##&lt;/strong&gt;&lt;/span&gt; : ##problem.solution.description## ##ENDIFproblem.storestatus##&lt;/div&gt;\n&lt;div&gt;##ELSEproblem.storestatus## ##lang.problem.url## : &lt;a href=\"##problem.url##\"&gt;##problem.url##&lt;/a&gt; ##ENDELSEproblem.storestatus##&lt;/div&gt;\n&lt;p class=\"description b\"&gt;&lt;strong&gt;##lang.problem.description##&lt;/strong&gt;&lt;/p&gt;\n&lt;p&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.problem.title##&lt;/span&gt;&#160;:##problem.title## &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.problem.authors##&lt;/span&gt;&#160;:##IFproblem.authors## ##problem.authors## ##ENDIFproblem.authors##    ##ELSEproblem.authors##--##ENDELSEproblem.authors## &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.problem.creationdate##&lt;/span&gt;&#160;:##problem.creationdate## &lt;br /&gt; ##IFproblem.assigntousers## &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.problem.assigntousers##&lt;/span&gt;&#160;: ##problem.assigntousers## ##ENDIFproblem.assigntousers##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.problem.status## &lt;/span&gt;&#160;: ##problem.status##&lt;br /&gt; ##IFproblem.assigntogroups## &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.problem.assigntogroups##&lt;/span&gt;&#160;: ##problem.assigntogroups## ##ENDIFproblem.assigntogroups##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.problem.urgency##&lt;/span&gt;&#160;: ##problem.urgency##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.problem.impact##&lt;/span&gt;&#160;: ##problem.impact##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.problem.priority##&lt;/span&gt; : ##problem.priority## &lt;br /&gt;##IFproblem.category##&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.problem.category## &lt;/span&gt;&#160;:##problem.category##  ##ENDIFproblem.category## ##ELSEproblem.category##  ##lang.problem.nocategoryassigned## ##ENDELSEproblem.category##    &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.problem.content##&lt;/span&gt;&#160;: ##problem.content##&lt;/p&gt;\n&lt;p&gt;##IFproblem.storestatus=6##&lt;br /&gt;&lt;span style=\"text-decoration: underline;\"&gt;&lt;strong&gt;&lt;span style=\"color: #888888;\"&gt;##lang.problem.solvedate##&lt;/span&gt;&lt;/strong&gt;&lt;/span&gt; : ##problem.solvedate##&lt;br /&gt;&lt;span style=\"color: #888888;\"&gt;&lt;strong&gt;&lt;span style=\"text-decoration: underline;\"&gt;##lang.problem.solution.type##&lt;/span&gt;&lt;/strong&gt;&lt;/span&gt; : ##problem.solution.type##&lt;br /&gt;&lt;span style=\"text-decoration: underline; color: #888888;\"&gt;&lt;strong&gt;##lang.problem.solution.description##&lt;/strong&gt;&lt;/span&gt; : ##problem.solution.description##&lt;br /&gt;##ENDIFproblem.storestatus##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;##lang.problem.numberoffollowups##&#160;: ##problem.numberoffollowups##&lt;/div&gt;\n&lt;p&gt;##FOREACHfollowups##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;&lt;br /&gt; &lt;strong&gt; [##followup.date##] &lt;em&gt;##lang.followup.isprivate## : ##followup.isprivate## &lt;/em&gt;&lt;/strong&gt;&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.followup.author## &lt;/span&gt; ##followup.author##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.followup.description## &lt;/span&gt; ##followup.description##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.followup.date## &lt;/span&gt; ##followup.date##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.followup.requesttype## &lt;/span&gt; ##followup.requesttype##&lt;/div&gt;\n&lt;p&gt;##ENDFOREACHfollowups##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;##lang.problem.numberoftickets##&#160;: ##problem.numberoftickets##&lt;/div&gt;\n&lt;p&gt;##FOREACHtickets##&lt;/p&gt;\n&lt;div&gt;&lt;strong&gt; [##ticket.date##] &lt;em&gt;##lang.problem.title## : &lt;a href=\"##ticket.url##\"&gt;##ticket.title## &lt;/a&gt;&lt;/em&gt;&lt;/strong&gt;&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; &lt;/span&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.problem.content## &lt;/span&gt; ##ticket.content##\n&lt;p&gt;##ENDFOREACHtickets##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;##lang.problem.numberoftasks##&#160;: ##problem.numberoftasks##&lt;/div&gt;\n&lt;p&gt;##FOREACHtasks##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;&lt;strong&gt;[##task.date##] &lt;/strong&gt;&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.task.author##&lt;/span&gt; ##task.author##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.task.description##&lt;/span&gt; ##task.description##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.task.time##&lt;/span&gt; ##task.time##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.task.category##&lt;/span&gt; ##task.category##&lt;/div&gt;\n&lt;p&gt;##ENDFOREACHtasks##&lt;/p&gt;\n&lt;/div&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(18, 18, '', '##recall.action##: ##recall.item.name##', '##recall.action##: ##recall.item.name##\n\n##recall.item.content##\n\n##lang.recall.planning.begin##: ##recall.planning.begin##\n##lang.recall.planning.end##: ##recall.planning.end##\n##lang.recall.planning.state##: ##recall.planning.state##\n##lang.recall.item.private##: ##recall.item.private##', '&lt;p&gt;##recall.action##: &lt;a href=\"##recall.item.url##\"&gt;##recall.item.name##&lt;/a&gt;&lt;/p&gt;\n&lt;p&gt;##recall.item.content##&lt;/p&gt;\n&lt;p&gt;##lang.recall.planning.begin##: ##recall.planning.begin##&lt;br /&gt;##lang.recall.planning.end##: ##recall.planning.end##&lt;br /&gt;##lang.recall.planning.state##: ##recall.planning.state##&lt;br /&gt;##lang.recall.item.private##: ##recall.item.private##&lt;br /&gt;&lt;br /&gt;&lt;/p&gt;\n&lt;p&gt;&lt;br /&gt;&lt;br /&gt;&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(19, 19, '', '##change.action## ##change.title##', '##IFchange.storestatus=5##\n ##lang.change.url## : ##change.urlapprove##\n ##lang.change.solvedate## : ##change.solvedate##\n ##lang.change.solution.type## : ##change.solution.type##\n ##lang.change.solution.description## : ##change.solution.description## ##ENDIFchange.storestatus##\n ##ELSEchange.storestatus## ##lang.change.url## : ##change.url## ##ENDELSEchange.storestatus##\n\n ##lang.change.description##\n\n ##lang.change.title##  :##change.title##\n ##lang.change.authors##  :##IFchange.authors## ##change.authors## ##ENDIFchange.authors## ##ELSEchange.authors##--##ENDELSEchange.authors##\n ##lang.change.creationdate##  :##change.creationdate##\n ##IFchange.assigntousers## ##lang.change.assigntousers##  : ##change.assigntousers## ##ENDIFchange.assigntousers##\n ##lang.change.status##  : ##change.status##\n ##IFchange.assigntogroups## ##lang.change.assigntogroups##  : ##change.assigntogroups## ##ENDIFchange.assigntogroups##\n ##lang.change.urgency##  : ##change.urgency##\n ##lang.change.impact##  : ##change.impact##\n ##lang.change.priority## : ##change.priority##\n##IFchange.category## ##lang.change.category##  :##change.category## ##ENDIFchange.category## ##ELSEchange.category## ##lang.change.nocategoryassigned## ##ENDELSEchange.category##\n ##lang.change.content##  : ##change.content##\n\n##IFchange.storestatus=6##\n ##lang.change.solvedate## : ##change.solvedate##\n ##lang.change.solution.type## : ##change.solution.type##\n ##lang.change.solution.description## : ##change.solution.description##\n##ENDIFchange.storestatus##\n ##lang.change.numberoffollowups## : ##change.numberoffollowups##\n\n##FOREACHfollowups##\n\n [##followup.date##] ##lang.followup.isprivate## : ##followup.isprivate##\n ##lang.followup.author## ##followup.author##\n ##lang.followup.description## ##followup.description##\n ##lang.followup.date## ##followup.date##\n ##lang.followup.requesttype## ##followup.requesttype##\n\n##ENDFOREACHfollowups##\n ##lang.change.numberofproblems## : ##change.numberofproblems##\n\n##FOREACHproblems##\n [##problem.date##] ##lang.change.title## : ##problem.title##\n ##lang.change.content## ##problem.content##\n\n##ENDFOREACHproblems##\n ##lang.change.numberoftasks## : ##change.numberoftasks##\n\n##FOREACHtasks##\n [##task.date##]\n ##lang.task.author## ##task.author##\n ##lang.task.description## ##task.description##\n ##lang.task.time## ##task.time##\n ##lang.task.category## ##task.category##\n\n##ENDFOREACHtasks##\n', '&lt;p&gt;##IFchange.storestatus=5##&lt;/p&gt;\n&lt;div&gt;##lang.change.url## : &lt;a href=\"##change.urlapprove##\"&gt;##change.urlapprove##&lt;/a&gt;&lt;/div&gt;\n&lt;div&gt;&lt;span style=\"color: #888888;\"&gt;&lt;strong&gt;&lt;span style=\"text-decoration: underline;\"&gt;##lang.change.solvedate##&lt;/span&gt;&lt;/strong&gt;&lt;/span&gt; : ##change.solvedate##&lt;br /&gt;&lt;span style=\"text-decoration: underline; color: #888888;\"&gt;&lt;strong&gt;##lang.change.solution.type##&lt;/strong&gt;&lt;/span&gt; : ##change.solution.type##&lt;br /&gt;&lt;span style=\"text-decoration: underline; color: #888888;\"&gt;&lt;strong&gt;##lang.change.solution.description##&lt;/strong&gt;&lt;/span&gt; : ##change.solution.description## ##ENDIFchange.storestatus##&lt;/div&gt;\n&lt;div&gt;##ELSEchange.storestatus## ##lang.change.url## : &lt;a href=\"##change.url##\"&gt;##change.url##&lt;/a&gt; ##ENDELSEchange.storestatus##&lt;/div&gt;\n&lt;p class=\"description b\"&gt;&lt;strong&gt;##lang.change.description##&lt;/strong&gt;&lt;/p&gt;\n&lt;p&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.change.title##&lt;/span&gt;&#160;:##change.title## &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.change.authors##&lt;/span&gt;&#160;:##IFchange.authors## ##change.authors## ##ENDIFchange.authors##    ##ELSEchange.authors##--##ENDELSEchange.authors## &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.change.creationdate##&lt;/span&gt;&#160;:##change.creationdate## &lt;br /&gt; ##IFchange.assigntousers## &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.change.assigntousers##&lt;/span&gt;&#160;: ##change.assigntousers## ##ENDIFchange.assigntousers##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.change.status## &lt;/span&gt;&#160;: ##change.status##&lt;br /&gt; ##IFchange.assigntogroups## &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.change.assigntogroups##&lt;/span&gt;&#160;: ##change.assigntogroups## ##ENDIFchange.assigntogroups##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.change.urgency##&lt;/span&gt;&#160;: ##change.urgency##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.change.impact##&lt;/span&gt;&#160;: ##change.impact##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.change.priority##&lt;/span&gt; : ##change.priority## &lt;br /&gt;##IFchange.category##&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.change.category## &lt;/span&gt;&#160;:##change.category##  ##ENDIFchange.category## ##ELSEchange.category##  ##lang.change.nocategoryassigned## ##ENDELSEchange.category##    &lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.change.content##&lt;/span&gt;&#160;: ##change.content##&lt;/p&gt;\n&lt;p&gt;##IFchange.storestatus=6##&lt;br /&gt;&lt;span style=\"text-decoration: underline;\"&gt;&lt;strong&gt;&lt;span style=\"color: #888888;\"&gt;##lang.change.solvedate##&lt;/span&gt;&lt;/strong&gt;&lt;/span&gt; : ##change.solvedate##&lt;br /&gt;&lt;span style=\"color: #888888;\"&gt;&lt;strong&gt;&lt;span style=\"text-decoration: underline;\"&gt;##lang.change.solution.type##&lt;/span&gt;&lt;/strong&gt;&lt;/span&gt; : ##change.solution.type##&lt;br /&gt;&lt;span style=\"text-decoration: underline; color: #888888;\"&gt;&lt;strong&gt;##lang.change.solution.description##&lt;/strong&gt;&lt;/span&gt; : ##change.solution.description##&lt;br /&gt;##ENDIFchange.storestatus##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;##lang.change.numberoffollowups##&#160;: ##change.numberoffollowups##&lt;/div&gt;\n&lt;p&gt;##FOREACHfollowups##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;&lt;br /&gt; &lt;strong&gt; [##followup.date##] &lt;em&gt;##lang.followup.isprivate## : ##followup.isprivate## &lt;/em&gt;&lt;/strong&gt;&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.followup.author## &lt;/span&gt; ##followup.author##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.followup.description## &lt;/span&gt; ##followup.description##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.followup.date## &lt;/span&gt; ##followup.date##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.followup.requesttype## &lt;/span&gt; ##followup.requesttype##&lt;/div&gt;\n&lt;p&gt;##ENDFOREACHfollowups##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;##lang.change.numberofproblems##&#160;: ##change.numberofproblems##&lt;/div&gt;\n&lt;p&gt;##FOREACHproblems##&lt;/p&gt;\n&lt;div&gt;&lt;strong&gt; [##problem.date##] &lt;em&gt;##lang.change.title## : &lt;a href=\"##problem.url##\"&gt;##problem.title## &lt;/a&gt;&lt;/em&gt;&lt;/strong&gt;&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; &lt;/span&gt;&lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt;##lang.change.content## &lt;/span&gt; ##problem.content##\n&lt;p&gt;##ENDFOREACHproblems##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;##lang.change.numberoftasks##&#160;: ##change.numberoftasks##&lt;/div&gt;\n&lt;p&gt;##FOREACHtasks##&lt;/p&gt;\n&lt;div class=\"description b\"&gt;&lt;strong&gt;[##task.date##] &lt;/strong&gt;&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.task.author##&lt;/span&gt; ##task.author##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.task.description##&lt;/span&gt; ##task.description##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.task.time##&lt;/span&gt; ##task.time##&lt;br /&gt; &lt;span style=\"color: #8b8c8f; font-weight: bold; text-decoration: underline;\"&gt; ##lang.task.category##&lt;/span&gt; ##task.category##&lt;/div&gt;\n&lt;p&gt;##ENDFOREACHtasks##&lt;/p&gt;\n&lt;/div&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(20, 20, '', '##mailcollector.action##', '##FOREACHmailcollectors##\n##lang.mailcollector.name## : ##mailcollector.name##\n##lang.mailcollector.errors## : ##mailcollector.errors##\n##mailcollector.url##\n##ENDFOREACHmailcollectors##', '&lt;p&gt;##FOREACHmailcollectors##&lt;br /&gt;##lang.mailcollector.name## : ##mailcollector.name##&lt;br /&gt; ##lang.mailcollector.errors## : ##mailcollector.errors##&lt;br /&gt;&lt;a href=\"##mailcollector.url##\"&gt;##mailcollector.url##&lt;/a&gt;&lt;br /&gt; ##ENDFOREACHmailcollectors##&lt;/p&gt;\n&lt;p&gt;&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(21, 21, '', '##project.action## ##project.name## ##project.code##', '##lang.project.url## : ##project.url##\n\n##lang.project.description##\n\n##lang.project.name## : ##project.name##\n##lang.project.code## : ##project.code##\n##lang.project.manager## : ##project.manager##\n##lang.project.managergroup## : ##project.managergroup##\n##lang.project.creationdate## : ##project.creationdate##\n##lang.project.priority## : ##project.priority##\n##lang.project.state## : ##project.state##\n##lang.project.type## : ##project.type##\n##lang.project.description## : ##project.description##\n\n##lang.project.numberoftasks## : ##project.numberoftasks##\n\n\n\n##FOREACHtasks##\n\n[##task.creationdate##]\n##lang.task.name## : ##task.name##\n##lang.task.state## : ##task.state##\n##lang.task.type## : ##task.type##\n##lang.task.percent## : ##task.percent##\n##lang.task.description## : ##task.description##\n\n##ENDFOREACHtasks##', '&lt;p&gt;##lang.project.url## : &lt;a href=\"##project.url##\"&gt;##project.url##&lt;/a&gt;&lt;/p&gt;\n&lt;p&gt;&lt;strong&gt;##lang.project.description##&lt;/strong&gt;&lt;/p&gt;\n&lt;p&gt;##lang.project.name## : ##project.name##&lt;br /&gt;##lang.project.code## : ##project.code##&lt;br /&gt; ##lang.project.manager## : ##project.manager##&lt;br /&gt;##lang.project.managergroup## : ##project.managergroup##&lt;br /&gt; ##lang.project.creationdate## : ##project.creationdate##&lt;br /&gt;##lang.project.priority## : ##project.priority## &lt;br /&gt;##lang.project.state## : ##project.state##&lt;br /&gt;##lang.project.type## : ##project.type##&lt;br /&gt;##lang.project.description## : ##project.description##&lt;/p&gt;\n&lt;p&gt;##lang.project.numberoftasks## : ##project.numberoftasks##&lt;/p&gt;\n&lt;div&gt;\n&lt;p&gt;##FOREACHtasks##&lt;/p&gt;\n&lt;div&gt;&lt;strong&gt;[##task.creationdate##] &lt;/strong&gt;&lt;br /&gt; ##lang.task.name## : ##task.name##&lt;br /&gt;##lang.task.state## : ##task.state##&lt;br /&gt;##lang.task.type## : ##task.type##&lt;br /&gt;##lang.task.percent## : ##task.percent##&lt;br /&gt;##lang.task.description## : ##task.description##&lt;/div&gt;\n&lt;p&gt;##ENDFOREACHtasks##&lt;/p&gt;\n&lt;/div&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(22, 22, '', '##projecttask.action## ##projecttask.name##', '##lang.projecttask.url## : ##projecttask.url##\n\n##lang.projecttask.description##\n\n##lang.projecttask.name## : ##projecttask.name##\n##lang.projecttask.project## : ##projecttask.project##\n##lang.projecttask.creationdate## : ##projecttask.creationdate##\n##lang.projecttask.state## : ##projecttask.state##\n##lang.projecttask.type## : ##projecttask.type##\n##lang.projecttask.description## : ##projecttask.description##\n\n##lang.projecttask.numberoftasks## : ##projecttask.numberoftasks##\n\n\n\n##FOREACHtasks##\n\n[##task.creationdate##]\n##lang.task.name## : ##task.name##\n##lang.task.state## : ##task.state##\n##lang.task.type## : ##task.type##\n##lang.task.percent## : ##task.percent##\n##lang.task.description## : ##task.description##\n\n##ENDFOREACHtasks##', '&lt;p&gt;##lang.projecttask.url## : &lt;a href=\"##projecttask.url##\"&gt;##projecttask.url##&lt;/a&gt;&lt;/p&gt;\n&lt;p&gt;&lt;strong&gt;##lang.projecttask.description##&lt;/strong&gt;&lt;/p&gt;\n&lt;p&gt;##lang.projecttask.name## : ##projecttask.name##&lt;br /&gt;##lang.projecttask.project## : &lt;a href=\"##projecttask.projecturl##\"&gt;##projecttask.project##&lt;/a&gt;&lt;br /&gt;##lang.projecttask.creationdate## : ##projecttask.creationdate##&lt;br /&gt;##lang.projecttask.state## : ##projecttask.state##&lt;br /&gt;##lang.projecttask.type## : ##projecttask.type##&lt;br /&gt;##lang.projecttask.description## : ##projecttask.description##&lt;/p&gt;\n&lt;p&gt;##lang.projecttask.numberoftasks## : ##projecttask.numberoftasks##&lt;/p&gt;\n&lt;div&gt;\n&lt;p&gt;##FOREACHtasks##&lt;/p&gt;\n&lt;div&gt;&lt;strong&gt;[##task.creationdate##] &lt;/strong&gt;&lt;br /&gt;##lang.task.name## : ##task.name##&lt;br /&gt;##lang.task.state## : ##task.state##&lt;br /&gt;##lang.task.type## : ##task.type##&lt;br /&gt;##lang.task.percent## : ##task.percent##&lt;br /&gt;##lang.task.description## : ##task.description##&lt;/div&gt;\n&lt;p&gt;##ENDFOREACHtasks##&lt;/p&gt;\n&lt;/div&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(23, 23, '', '##objectlock.action##', '##objectlock.type## ###objectlock.id## - ##objectlock.name##\n\n      ##lang.objectlock.url##\n      ##objectlock.url##\n\n      ##lang.objectlock.date_mod##\n      ##objectlock.date_mod##\n\n      Hello ##objectlock.lockedby.firstname##,\n      Could go to this item and unlock it for me?\n      Thank you,\n      Regards,\n      ##objectlock.requester.firstname##', '&lt;table&gt;\n      &lt;tbody&gt;\n      &lt;tr&gt;&lt;th colspan=\"2\"&gt;&lt;a href=\"##objectlock.url##\"&gt;##objectlock.type## ###objectlock.id## - ##objectlock.name##&lt;/a&gt;&lt;/th&gt;&lt;/tr&gt;\n      &lt;tr&gt;\n      &lt;td&gt;##lang.objectlock.url##&lt;/td&gt;\n      &lt;td&gt;##objectlock.url##&lt;/td&gt;\n      &lt;/tr&gt;\n      &lt;tr&gt;\n      &lt;td&gt;##lang.objectlock.date_mod##&lt;/td&gt;\n      &lt;td&gt;##objectlock.date_mod##&lt;/td&gt;\n      &lt;/tr&gt;\n      &lt;/tbody&gt;\n      &lt;/table&gt;\n      &lt;p&gt;&lt;span style=\"font-size: small;\"&gt;Hello ##objectlock.lockedby.firstname##,&lt;br /&gt;Could go to this item and unlock it for me?&lt;br /&gt;Thank you,&lt;br /&gt;Regards,&lt;br /&gt;##objectlock.requester.firstname## ##objectlock.requester.lastname##&lt;/span&gt;&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(24, 24, '', '##savedsearch.action## ##savedsearch.name##', '##savedsearch.type## ###savedsearch.id## - ##savedsearch.name##\n\n      ##savedsearch.message##\n\n      ##lang.savedsearch.url##\n      ##savedsearch.url##\n\n      Regards,', '&lt;table&gt;\n      &lt;tbody&gt;\n      &lt;tr&gt;&lt;th colspan=\"2\"&gt;&lt;a href=\"##savedsearch.url##\"&gt;##savedsearch.type## ###savedsearch.id## - ##savedsearch.name##&lt;/a&gt;&lt;/th&gt;&lt;/tr&gt;\n      &lt;tr&gt;&lt;td colspan=\"2\"&gt;&lt;a href=\"##savedsearch.url##\"&gt;##savedsearch.message##&lt;/a&gt;&lt;/td&gt;&lt;/tr&gt;\n      &lt;tr&gt;\n      &lt;td&gt;##lang.savedsearch.url##&lt;/td&gt;\n      &lt;td&gt;##savedsearch.url##&lt;/td&gt;\n      &lt;/tr&gt;\n      &lt;/tbody&gt;\n      &lt;/table&gt;\n      &lt;p&gt;&lt;span style=\"font-size: small;\"&gt;Hello &lt;br /&gt;Regards,&lt;/span&gt;&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(25, 25, '', '##certificate.action##  ##certificate.name##', '##lang.certificate.entity## : ##certificate.entity##\n\n##lang.certificate.serial## : ##certificate.serial##\n\n##lang.certificate.expirationdate## : ##certificate.expirationdate##\n\n##certificate.url##', '&lt;p&gt;\n##lang.certificate.entity## : ##certificate.entity##&lt;br /&gt;\n&lt;br /&gt;##lang.certificate.name## : ##certificate.name##&lt;br /&gt;\n##lang.certificate.serial## : ##certificate.serial##&lt;br /&gt;\n##lang.certificate.expirationdate## : ##certificate.expirationdate##\n&lt;br /&gt; &lt;a href=\"##certificate.url##\"&gt; ##certificate.url##\n&lt;/a&gt;&lt;br /&gt;\n&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(26, 26, '', '##domain.action## : ##domain.name##', '##lang.domain.entity## :##domain.entity##\n   ##lang.domain.name## : ##domain.name## - ##lang.domain.dateexpiration## : ##domain.dateexpiration##', '&lt;p&gt;##lang.domain.entity## :##domain.entity##&lt;br /&gt; &lt;br /&gt;\n                        ##lang.domain.name##  : ##domain.name## - ##lang.domain.dateexpiration## :  ##domain.dateexpiration##&lt;br /&gt;\n                        &lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(27, 27, '', '##user.action##', '##user.realname## ##user.firstname##,\n\n##IFuser.password.has_expired=1##\n##lang.password.has_expired.information##\n##ENDIFuser.password.has_expired##\n##ELSEuser.password.has_expired##\n##lang.password.expires_soon.information##\n##ENDELSEuser.password.has_expired##\n##lang.user.password.expiration.date##: ##user.password.expiration.date##\n##IFuser.account.lock.date##\n##lang.user.account.lock.date##: ##user.account.lock.date##\n##ENDIFuser.account.lock.date##\n\n##password.update.link## ##user.password.update.url##', '&lt;p&gt;&lt;strong&gt;##user.realname## ##user.firstname##&lt;/strong&gt;&lt;/p&gt;\n\n##IFuser.password.has_expired=1##\n&lt;p&gt;##lang.password.has_expired.information##&lt;/p&gt;\n##ENDIFuser.password.has_expired##\n##ELSEuser.password.has_expired##\n&lt;p&gt;##lang.password.expires_soon.information##&lt;/p&gt;\n##ENDELSEuser.password.has_expired##\n&lt;p&gt;##lang.user.password.expiration.date##: ##user.password.expiration.date##&lt;/p&gt;\n##IFuser.account.lock.date##\n&lt;p&gt;##lang.user.account.lock.date##: ##user.account.lock.date##&lt;/p&gt;\n##ENDIFuser.account.lock.date##\n\n&lt;p&gt;##lang.password.update.link## &lt;a href=\"##user.password.update.url##\"&gt;##user.password.update.url##&lt;/a&gt;&lt;/p&gt;');
REPLACE INTO `glpi_notificationtemplatetranslations` (`id`, `notificationtemplates_id`, `language`, `subject`, `content_text`, `content_html`) VALUES(28, 28, '', '##lang.plugins_updates_available##', '##lang.plugins_updates_available##\n\n##FOREACHplugins##\n##plugin.name## :##plugin.old_version## -&gt; ##plugin.version##\n##ENDFOREACHplugins##\n\n##lang.marketplace.url## : ##marketplace.url##', '&lt;p&gt;##lang.plugins_updates_available##&lt;/p&gt;\n&lt;ul&gt;##FOREACHplugins##\n&lt;li&gt;##plugin.name## :##plugin.old_version## -&gt; ##plugin.version##&lt;/li&gt;\n##ENDFOREACHplugins##&lt;/ul&gt;\n&lt;p&gt;##lang.marketplace.url## : &lt;a title=\"##lang.marketplace.url##\" href=\"##marketplace.url##\" target=\"_blank\" rel=\"noopener\"&gt;##marketplace.url##&lt;/a&gt;&lt;/p&gt;');

--
-- Volcado de datos para la tabla `glpi_operatingsystemarchitectures`
--

REPLACE INTO `glpi_operatingsystemarchitectures` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'Arch1', '', '2023-03-19 19:42:18', '2023-03-19 19:42:18');

--
-- Volcado de datos para la tabla `glpi_operatingsystemeditions`
--

REPLACE INTO `glpi_operatingsystemeditions` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'Edition1', '', '2023-03-19 19:42:58', '2023-03-19 19:42:58');

--
-- Volcado de datos para la tabla `glpi_operatingsystemkernelversions`
--

REPLACE INTO `glpi_operatingsystemkernelversions` (`id`, `operatingsystemkernels_id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 0, 'Kernel1', '', '2023-03-19 19:42:25', '2023-03-19 19:42:25');

--
-- Volcado de datos para la tabla `glpi_operatingsystems`
--

REPLACE INTO `glpi_operatingsystems` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'Windows11', 'ccc', '2023-03-19 19:42:10', '2023-03-19 19:42:10');

--
-- Volcado de datos para la tabla `glpi_operatingsystemservicepacks`
--

REPLACE INTO `glpi_operatingsystemservicepacks` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'SvcPack1', 'Comment', '2023-03-19 19:42:47', '2023-03-19 19:42:47');

--
-- Volcado de datos para la tabla `glpi_operatingsystemversions`
--

REPLACE INTO `glpi_operatingsystemversions` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, '1', '', '2023-03-19 19:42:33', '2023-03-19 19:42:33');

--
-- Volcado de datos para la tabla `glpi_passivedcequipmentmodels`
--

REPLACE INTO `glpi_passivedcequipmentmodels` (`id`, `name`, `comment`, `product_number`, `weight`, `required_units`, `depth`, `power_connections`, `power_consumption`, `is_half_rack`, `picture_front`, `picture_rear`, `pictures`, `date_mod`, `date_creation`) VALUES(1, 'PassiveDcModel1', '23123', '123123', 1, 1, 1, 1, 1, 1, NULL, NULL, NULL, '2023-03-19 19:38:51', '2023-03-19 19:38:51');

--
-- Volcado de datos para la tabla `glpi_passivedcequipments`
--

REPLACE INTO `glpi_passivedcequipments` (`id`, `name`, `entities_id`, `is_recursive`, `locations_id`, `serial`, `otherserial`, `passivedcequipmentmodels_id`, `passivedcequipmenttypes_id`, `users_id_tech`, `groups_id_tech`, `is_template`, `template_name`, `is_deleted`, `states_id`, `comment`, `manufacturers_id`, `date_mod`, `date_creation`) VALUES(1, 'PassiveDc1', 0, 0, 1, '23123213', '123123123', 1, 1, 0, 0, 0, NULL, 0, 2, '123123123', 2, '2023-03-19 19:38:56', '2023-03-19 19:38:56');

--
-- Volcado de datos para la tabla `glpi_passivedcequipmenttypes`
--

REPLACE INTO `glpi_passivedcequipmenttypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'PassiveDcType1', 'Comment', '2023-03-19 19:38:31', '2023-03-19 19:38:31');

--
-- Volcado de datos para la tabla `glpi_pdumodels`
--

REPLACE INTO `glpi_pdumodels` (`id`, `name`, `comment`, `product_number`, `weight`, `required_units`, `depth`, `power_connections`, `max_power`, `is_half_rack`, `picture_front`, `picture_rear`, `pictures`, `is_rackable`, `date_mod`, `date_creation`) VALUES(1, 'PduModel1', 'Comment', 'Perwer', 0, 1, 1, 0, 0, 0, NULL, NULL, NULL, 0, '2023-03-19 19:38:01', '2023-03-19 19:38:01');

--
-- Volcado de datos para la tabla `glpi_pdus`
--

REPLACE INTO `glpi_pdus` (`id`, `name`, `entities_id`, `is_recursive`, `locations_id`, `serial`, `otherserial`, `pdumodels_id`, `users_id_tech`, `groups_id_tech`, `is_template`, `template_name`, `is_deleted`, `states_id`, `comment`, `manufacturers_id`, `pdutypes_id`, `date_mod`, `date_creation`) VALUES(1, 'Pdu1', 0, 0, 1, '12312323', '12323132313231', 1, 0, 0, 0, NULL, 0, 2, 'Comment', 4, 1, '2023-03-19 19:38:06', '2023-03-19 19:38:06');

--
-- Volcado de datos para la tabla `glpi_pdutypes`
--

REPLACE INTO `glpi_pdutypes` (`id`, `entities_id`, `is_recursive`, `name`, `comment`, `date_creation`, `date_mod`) VALUES(1, 0, 0, 'PduType1', '', '2023-03-19 19:37:48', '2023-03-19 19:37:48');

--
-- Volcado de datos para la tabla `glpi_peripheralmodels`
--

REPLACE INTO `glpi_peripheralmodels` (`id`, `name`, `comment`, `product_number`, `weight`, `required_units`, `depth`, `power_connections`, `power_consumption`, `is_half_rack`, `picture_front`, `picture_rear`, `pictures`, `date_mod`, `date_creation`) VALUES(1, 'Model1', 'comment', '2323', 0, 1, 1, 0, 0, 0, NULL, NULL, NULL, '2023-03-19 19:27:47', '2023-03-19 19:27:47');

--
-- Volcado de datos para la tabla `glpi_peripherals`
--

REPLACE INTO `glpi_peripherals` (`id`, `entities_id`, `name`, `date_mod`, `contact`, `contact_num`, `users_id_tech`, `groups_id_tech`, `comment`, `serial`, `otherserial`, `locations_id`, `peripheraltypes_id`, `peripheralmodels_id`, `brand`, `manufacturers_id`, `is_global`, `is_deleted`, `is_template`, `template_name`, `users_id`, `groups_id`, `states_id`, `ticket_tco`, `is_dynamic`, `autoupdatesystems_id`, `uuid`, `date_creation`, `is_recursive`) VALUES(1, 0, 'Device1', '2023-03-19 19:28:09', 'alternateusername', 'Alternate1', 0, 0, 'comments1', '23232323', '23231323', 1, 1, 1, 'brand1', 2, 0, 0, 0, NULL, 0, 0, 1, '0.0000', 0, 1, 'uuid', '2023-03-19 19:28:09', 0);

--
-- Volcado de datos para la tabla `glpi_peripheraltypes`
--

REPLACE INTO `glpi_peripheraltypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'DeviceType1', 'qweqwe', '2023-03-19 19:27:28', '2023-03-19 19:27:28');

--
-- Volcado de datos para la tabla `glpi_phonemodels`
--

REPLACE INTO `glpi_phonemodels` (`id`, `name`, `comment`, `product_number`, `date_mod`, `date_creation`, `picture_front`, `picture_rear`, `pictures`) VALUES(1, 'PhoneModel1', 'comment', '12323', '2023-03-19 19:34:41', '2023-03-19 19:34:41', NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_phonepowersupplies`
--

REPLACE INTO `glpi_phonepowersupplies` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'PhonePowerSupply1', 'comment', '2023-03-19 19:35:12', '2023-03-19 19:35:12');

--
-- Volcado de datos para la tabla `glpi_phones`
--

REPLACE INTO `glpi_phones` (`id`, `entities_id`, `name`, `date_mod`, `contact`, `contact_num`, `users_id_tech`, `groups_id_tech`, `comment`, `serial`, `otherserial`, `locations_id`, `phonetypes_id`, `phonemodels_id`, `brand`, `phonepowersupplies_id`, `number_line`, `have_headset`, `have_hp`, `manufacturers_id`, `is_global`, `is_deleted`, `is_template`, `template_name`, `users_id`, `groups_id`, `states_id`, `ticket_tco`, `is_dynamic`, `autoupdatesystems_id`, `uuid`, `date_creation`, `is_recursive`, `last_inventory_update`) VALUES(1, 0, 'Phone1', '2023-03-19 19:35:19', 'Alternate', 'Alternate1', 0, 0, 'comment', '23232313', '1232313', 1, 1, 1, 'brand', 1, '5', 1, 1, 2, 0, 0, 0, NULL, 0, 0, 2, '0.0000', 0, 1, 'uuid', '2023-03-19 19:35:19', 0, NULL);

--
-- Volcado de datos para la tabla `glpi_phonetypes`
--

REPLACE INTO `glpi_phonetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'PhoneType1', 'Comment', '2023-03-19 19:34:27', '2023-03-19 19:34:27');

--
-- Volcado de datos para la tabla `glpi_printermodels`
--

REPLACE INTO `glpi_printermodels` (`id`, `name`, `comment`, `product_number`, `date_mod`, `date_creation`, `picture_front`, `picture_rear`, `pictures`) VALUES(1, 'PrinterModel1', 'Comment', '213123213', '2023-03-19 19:31:19', '2023-03-19 19:31:19', NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_printers`
--

REPLACE INTO `glpi_printers` (`id`, `entities_id`, `is_recursive`, `name`, `date_mod`, `contact`, `contact_num`, `users_id_tech`, `groups_id_tech`, `serial`, `otherserial`, `have_serial`, `have_parallel`, `have_usb`, `have_wifi`, `have_ethernet`, `comment`, `memory_size`, `locations_id`, `networks_id`, `printertypes_id`, `printermodels_id`, `manufacturers_id`, `is_global`, `is_deleted`, `is_template`, `template_name`, `init_pages_counter`, `last_pages_counter`, `users_id`, `groups_id`, `states_id`, `ticket_tco`, `is_dynamic`, `uuid`, `date_creation`, `sysdescr`, `last_inventory_update`, `snmpcredentials_id`, `autoupdatesystems_id`) VALUES(1, 0, 0, 'printer1', '2023-03-19 19:31:53', 'Alternate', 'Alternate1', 0, 0, '1213131213', '233131312', 1, 1, 1, 0, 1, 'comment', '2', 1, 1, 1, 1, 2, 0, 0, 0, NULL, 2, 2, 0, 0, 2, '0.0000', 0, 'uuid', '2023-03-19 19:31:53', 'Sysdescr', NULL, 1, 1);

--
-- Volcado de datos para la tabla `glpi_printertypes`
--

REPLACE INTO `glpi_printertypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'PrinterType1', 'Comment1', '2023-03-19 19:31:02', '2023-03-19 19:31:02');

--
-- Volcado de datos para la tabla `glpi_problemtemplatemandatoryfields`
--

REPLACE INTO `glpi_problemtemplatemandatoryfields` (`id`, `problemtemplates_id`, `num`) VALUES(1, 1, 21);

--
-- Volcado de datos para la tabla `glpi_problemtemplates`
--

REPLACE INTO `glpi_problemtemplates` (`id`, `name`, `entities_id`, `is_recursive`, `comment`) VALUES(1, 'Default', 0, 1, NULL);

--
-- Volcado de datos para la tabla `glpi_profilerights`
--

REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(1, 1, 'computer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(2, 1, 'monitor', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(3, 1, 'software', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(4, 1, 'networking', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(5, 1, 'internet', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(6, 1, 'printer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(7, 1, 'peripheral', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(8, 1, 'cartridge', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(9, 1, 'consumable', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(10, 1, 'phone', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(11, 6, 'queuednotification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(12, 1, 'contact_enterprise', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(13, 1, 'document', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(14, 1, 'contract', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(15, 1, 'infocom', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(16, 1, 'knowbase', 2048);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(17, 1, 'reservation', 1024);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(18, 1, 'reports', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(19, 1, 'dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(20, 1, 'device', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(21, 1, 'typedoc', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(22, 1, 'link', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(23, 1, 'config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(24, 1, 'rule_ticket', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(25, 1, 'rule_import', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(26, 1, 'rule_location', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(27, 1, 'rule_ldap', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(28, 1, 'rule_softwarecategories', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(29, 1, 'search_config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(30, 5, 'location', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(31, 7, 'domain', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(32, 1, 'profile', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(33, 1, 'user', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(34, 1, 'group', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(35, 1, 'entity', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(36, 1, 'transfer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(37, 1, 'logs', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(38, 1, 'reminder_public', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(39, 1, 'rssfeed_public', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(40, 1, 'bookmark_public', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(41, 1, 'backup', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(42, 1, 'ticket', 5);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(43, 1, 'followup', 5);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(44, 1, 'task', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(45, 1, 'planning', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(46, 2, 'state', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(47, 2, 'taskcategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(48, 1, 'statistic', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(49, 1, 'password_update', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(50, 1, 'show_group_hardware', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(51, 1, 'rule_dictionnary_software', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(52, 1, 'rule_dictionnary_dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(53, 1, 'budget', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(54, 1, 'notification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(55, 1, 'rule_mailcollector', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(56, 7, 'solutiontemplate', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(57, 7, 'itilfollowuptemplate', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(58, 1, 'calendar', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(59, 1, 'slm', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(60, 1, 'rule_dictionnary_printer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(61, 1, 'problem', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(62, 2, 'cable_management', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(63, 4, 'knowbasecategory', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(64, 5, 'itilcategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(65, 1, 'itiltemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(66, 1, 'ticketrecurrent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(67, 1, 'ticketcost', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(68, 6, 'changevalidation', 20);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(69, 1, 'ticketvalidation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(70, 2, 'computer', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(71, 2, 'monitor', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(72, 2, 'software', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(73, 2, 'networking', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(74, 2, 'internet', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(75, 2, 'printer', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(76, 2, 'peripheral', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(77, 2, 'cartridge', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(78, 2, 'consumable', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(79, 2, 'phone', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(80, 5, 'queuednotification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(81, 2, 'contact_enterprise', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(82, 2, 'document', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(83, 2, 'contract', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(84, 2, 'infocom', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(85, 2, 'knowbase', 10241);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(86, 2, 'reservation', 1025);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(87, 2, 'reports', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(88, 2, 'dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(89, 2, 'device', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(90, 2, 'typedoc', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(91, 2, 'link', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(92, 2, 'config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(93, 2, 'rule_ticket', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(94, 2, 'rule_import', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(95, 2, 'rule_location', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(96, 2, 'rule_ldap', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(97, 2, 'rule_softwarecategories', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(98, 2, 'search_config', 1024);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(99, 4, 'location', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(100, 6, 'domain', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(101, 2, 'profile', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(102, 2, 'user', 2049);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(103, 2, 'group', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(104, 2, 'entity', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(105, 2, 'transfer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(106, 2, 'logs', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(107, 2, 'reminder_public', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(108, 2, 'rssfeed_public', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(109, 2, 'bookmark_public', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(110, 2, 'backup', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(111, 2, 'ticket', 168989);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(112, 2, 'followup', 5);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(113, 2, 'task', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(114, 6, 'projecttask', 1025);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(115, 7, 'projecttask', 1025);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(116, 2, 'planning', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(117, 1, 'state', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(118, 1, 'taskcategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(119, 2, 'statistic', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(120, 2, 'password_update', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(121, 2, 'show_group_hardware', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(122, 2, 'rule_dictionnary_software', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(123, 2, 'rule_dictionnary_dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(124, 2, 'budget', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(125, 2, 'notification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(126, 2, 'rule_mailcollector', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(127, 5, 'solutiontemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(128, 5, 'itilfollowuptemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(129, 6, 'solutiontemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(130, 6, 'itilfollowuptemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(131, 2, 'calendar', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(132, 2, 'slm', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(133, 2, 'rule_dictionnary_printer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(134, 2, 'problem', 1057);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(135, 1, 'cable_management', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(136, 3, 'knowbasecategory', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(137, 4, 'itilcategory', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(138, 2, 'itiltemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(139, 2, 'ticketrecurrent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(140, 2, 'ticketcost', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(141, 4, 'changevalidation', 1044);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(142, 5, 'changevalidation', 20);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(143, 2, 'ticketvalidation', 15376);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(144, 3, 'computer', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(145, 3, 'monitor', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(146, 3, 'software', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(147, 3, 'networking', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(148, 3, 'internet', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(149, 3, 'printer', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(150, 3, 'peripheral', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(151, 3, 'cartridge', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(152, 3, 'consumable', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(153, 3, 'phone', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(154, 4, 'queuednotification', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(155, 3, 'contact_enterprise', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(156, 3, 'document', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(157, 3, 'contract', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(158, 3, 'infocom', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(159, 3, 'knowbase', 14359);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(160, 3, 'reservation', 1055);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(161, 3, 'reports', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(162, 3, 'dropdown', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(163, 3, 'device', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(164, 3, 'typedoc', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(165, 3, 'link', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(166, 3, 'config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(167, 3, 'rule_ticket', 1047);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(168, 3, 'rule_import', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(169, 3, 'rule_location', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(170, 3, 'rule_ldap', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(171, 3, 'rule_softwarecategories', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(172, 3, 'search_config', 3072);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(173, 3, 'location', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(174, 5, 'domain', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(175, 3, 'profile', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(176, 3, 'user', 7199);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(177, 3, 'group', 119);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(178, 3, 'entity', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(179, 3, 'transfer', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(180, 3, 'logs', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(181, 3, 'reminder_public', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(182, 3, 'rssfeed_public', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(183, 3, 'bookmark_public', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(184, 3, 'backup', 1024);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(185, 3, 'ticket', 261151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(186, 3, 'followup', 31767);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(187, 3, 'task', 13329);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(188, 3, 'projecttask', 1121);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(189, 4, 'projecttask', 1121);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(190, 5, 'projecttask', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(191, 3, 'planning', 3073);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(192, 7, 'taskcategory', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(193, 7, 'cable_management', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(194, 3, 'statistic', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(195, 3, 'password_update', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(196, 3, 'show_group_hardware', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(197, 3, 'rule_dictionnary_software', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(198, 3, 'rule_dictionnary_dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(199, 3, 'budget', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(200, 3, 'notification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(201, 3, 'rule_mailcollector', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(202, 3, 'solutiontemplate', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(203, 3, 'itilfollowuptemplate', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(204, 4, 'solutiontemplate', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(205, 4, 'itilfollowuptemplate', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(206, 3, 'calendar', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(207, 3, 'slm', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(208, 3, 'rule_dictionnary_printer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(209, 3, 'problem', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(210, 2, 'knowbasecategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(211, 3, 'itilcategory', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(212, 3, 'itiltemplate', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(213, 3, 'ticketrecurrent', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(214, 3, 'ticketcost', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(215, 2, 'changevalidation', 1044);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(216, 3, 'changevalidation', 1044);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(217, 3, 'ticketvalidation', 15376);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(218, 4, 'computer', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(219, 4, 'monitor', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(220, 4, 'software', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(221, 4, 'networking', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(222, 4, 'internet', 159);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(223, 4, 'printer', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(224, 4, 'peripheral', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(225, 4, 'cartridge', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(226, 4, 'consumable', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(227, 4, 'phone', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(228, 4, 'contact_enterprise', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(229, 4, 'document', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(230, 4, 'contract', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(231, 4, 'infocom', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(232, 4, 'knowbase', 15383);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(233, 4, 'reservation', 1055);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(234, 4, 'reports', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(235, 4, 'dropdown', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(236, 4, 'device', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(237, 4, 'typedoc', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(238, 4, 'link', 159);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(239, 4, 'config', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(240, 4, 'rule_ticket', 1047);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(241, 4, 'rule_import', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(242, 4, 'rule_location', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(243, 4, 'rule_ldap', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(244, 4, 'rule_softwarecategories', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(245, 4, 'search_config', 3072);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(246, 2, 'location', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(247, 4, 'domain', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(248, 4, 'profile', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(249, 4, 'user', 7327);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(250, 4, 'group', 119);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(251, 4, 'entity', 3327);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(252, 4, 'transfer', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(253, 4, 'logs', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(254, 4, 'reminder_public', 159);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(255, 4, 'rssfeed_public', 159);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(256, 4, 'bookmark_public', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(257, 4, 'backup', 1045);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(258, 4, 'ticket', 261151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(259, 4, 'followup', 31767);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(260, 4, 'task', 13329);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(261, 7, 'project', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(262, 1, 'projecttask', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(263, 2, 'projecttask', 1025);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(264, 4, 'planning', 3073);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(265, 6, 'taskcategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(266, 6, 'cable_management', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(267, 4, 'statistic', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(268, 4, 'password_update', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(269, 4, 'show_group_hardware', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(270, 4, 'rule_dictionnary_software', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(271, 4, 'rule_dictionnary_dropdown', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(272, 4, 'budget', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(273, 4, 'notification', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(274, 4, 'rule_mailcollector', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(275, 1, 'solutiontemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(276, 1, 'itilfollowuptemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(277, 2, 'solutiontemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(278, 2, 'itilfollowuptemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(279, 4, 'calendar', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(280, 4, 'slm', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(281, 4, 'rule_dictionnary_printer', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(282, 4, 'problem', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(283, 1, 'knowbasecategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(284, 2, 'itilcategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(285, 4, 'itiltemplate', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(286, 4, 'ticketrecurrent', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(287, 4, 'ticketcost', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(288, 7, 'change', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(289, 1, 'changevalidation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(290, 4, 'ticketvalidation', 15376);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(291, 5, 'computer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(292, 5, 'monitor', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(293, 5, 'software', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(294, 5, 'networking', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(295, 5, 'internet', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(296, 5, 'printer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(297, 5, 'peripheral', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(298, 5, 'cartridge', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(299, 5, 'consumable', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(300, 5, 'phone', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(301, 3, 'queuednotification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(302, 5, 'contact_enterprise', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(303, 5, 'document', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(304, 5, 'contract', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(305, 5, 'infocom', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(306, 5, 'knowbase', 10240);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(307, 5, 'reservation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(308, 5, 'reports', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(309, 5, 'dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(310, 5, 'device', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(311, 5, 'typedoc', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(312, 5, 'link', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(313, 5, 'config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(314, 5, 'rule_ticket', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(315, 5, 'rule_import', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(316, 5, 'rule_location', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(317, 5, 'rule_ldap', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(318, 5, 'rule_softwarecategories', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(319, 5, 'search_config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(320, 1, 'location', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(321, 3, 'domain', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(322, 5, 'profile', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(323, 5, 'user', 1025);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(324, 5, 'group', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(325, 5, 'entity', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(326, 5, 'transfer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(327, 5, 'logs', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(328, 5, 'reminder_public', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(329, 5, 'rssfeed_public', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(330, 5, 'bookmark_public', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(331, 5, 'backup', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(332, 5, 'ticket', 140295);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(333, 5, 'followup', 12295);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(334, 5, 'task', 8193);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(335, 4, 'project', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(336, 5, 'project', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(337, 6, 'project', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(338, 5, 'planning', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(339, 5, 'taskcategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(340, 5, 'cable_management', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(341, 5, 'statistic', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(342, 5, 'password_update', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(343, 5, 'show_group_hardware', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(344, 5, 'rule_dictionnary_software', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(345, 5, 'rule_dictionnary_dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(346, 5, 'budget', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(347, 5, 'notification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(348, 5, 'rule_mailcollector', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(349, 6, 'state', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(350, 7, 'state', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(351, 5, 'calendar', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(352, 5, 'slm', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(353, 5, 'rule_dictionnary_printer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(354, 5, 'problem', 1024);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(355, 7, 'knowbasecategory', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(356, 1, 'itilcategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(357, 5, 'itiltemplate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(358, 5, 'ticketrecurrent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(359, 5, 'ticketcost', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(360, 5, 'change', 1054);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(361, 6, 'change', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(362, 5, 'ticketvalidation', 3088);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(363, 6, 'computer', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(364, 6, 'monitor', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(365, 6, 'software', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(366, 6, 'networking', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(367, 6, 'internet', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(368, 6, 'printer', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(369, 6, 'peripheral', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(370, 6, 'cartridge', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(371, 6, 'consumable', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(372, 6, 'phone', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(373, 2, 'queuednotification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(374, 6, 'contact_enterprise', 96);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(375, 6, 'document', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(376, 6, 'contract', 96);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(377, 6, 'infocom', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(378, 6, 'knowbase', 14359);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(379, 6, 'reservation', 1055);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(380, 6, 'reports', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(381, 6, 'dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(382, 6, 'device', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(383, 6, 'typedoc', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(384, 6, 'link', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(385, 6, 'config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(386, 6, 'rule_ticket', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(387, 6, 'rule_import', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(388, 6, 'rule_location', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(389, 6, 'rule_ldap', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(390, 6, 'rule_softwarecategories', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(391, 6, 'search_config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(392, 2, 'domain', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(393, 6, 'profile', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(394, 6, 'user', 1055);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(395, 6, 'group', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(396, 6, 'entity', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(397, 6, 'transfer', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(398, 6, 'logs', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(399, 6, 'reminder_public', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(400, 6, 'rssfeed_public', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(401, 6, 'bookmark_public', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(402, 6, 'backup', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(403, 6, 'ticket', 166919);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(404, 6, 'followup', 13319);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(405, 6, 'task', 13329);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(406, 1, 'project', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(407, 2, 'project', 1025);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(408, 3, 'project', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(409, 6, 'planning', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(410, 4, 'taskcategory', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(411, 4, 'cable_management', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(412, 6, 'statistic', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(413, 6, 'password_update', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(414, 6, 'show_group_hardware', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(415, 6, 'rule_dictionnary_software', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(416, 6, 'rule_dictionnary_dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(417, 6, 'budget', 96);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(418, 6, 'notification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(419, 6, 'rule_mailcollector', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(420, 4, 'state', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(421, 5, 'state', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(422, 6, 'calendar', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(423, 6, 'slm', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(424, 6, 'rule_dictionnary_printer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(425, 6, 'problem', 1121);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(426, 6, 'knowbasecategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(427, 7, 'itilcategory', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(428, 7, 'location', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(429, 6, 'itiltemplate', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(430, 6, 'ticketrecurrent', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(431, 6, 'ticketcost', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(432, 3, 'change', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(433, 4, 'change', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(434, 6, 'ticketvalidation', 3088);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(435, 7, 'computer', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(436, 7, 'monitor', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(437, 7, 'software', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(438, 7, 'networking', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(439, 7, 'internet', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(440, 7, 'printer', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(441, 7, 'peripheral', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(442, 7, 'cartridge', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(443, 7, 'consumable', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(444, 7, 'phone', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(445, 1, 'queuednotification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(446, 7, 'contact_enterprise', 96);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(447, 7, 'document', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(448, 7, 'contract', 96);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(449, 7, 'infocom', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(450, 7, 'knowbase', 14359);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(451, 7, 'reservation', 1055);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(452, 7, 'reports', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(453, 7, 'dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(454, 7, 'device', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(455, 7, 'typedoc', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(456, 7, 'link', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(457, 7, 'config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(458, 7, 'rule_ticket', 1047);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(459, 7, 'rule_import', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(460, 7, 'rule_location', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(461, 7, 'rule_ldap', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(462, 7, 'rule_softwarecategories', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(463, 7, 'search_config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(464, 1, 'domain', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(465, 7, 'profile', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(466, 7, 'user', 1055);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(467, 7, 'group', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(468, 7, 'entity', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(469, 7, 'transfer', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(470, 7, 'logs', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(471, 7, 'reminder_public', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(472, 7, 'rssfeed_public', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(473, 7, 'bookmark_public', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(474, 7, 'backup', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(475, 7, 'ticket', 261151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(476, 7, 'followup', 31767);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(477, 7, 'task', 13329);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(478, 7, 'queuednotification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(479, 7, 'planning', 3073);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(480, 3, 'taskcategory', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(481, 3, 'cable_management', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(482, 7, 'statistic', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(483, 7, 'password_update', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(484, 7, 'show_group_hardware', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(485, 7, 'rule_dictionnary_software', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(486, 7, 'rule_dictionnary_dropdown', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(487, 7, 'budget', 96);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(488, 7, 'notification', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(489, 7, 'rule_mailcollector', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(490, 7, 'changevalidation', 1044);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(491, 3, 'state', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(492, 7, 'calendar', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(493, 7, 'slm', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(494, 7, 'rule_dictionnary_printer', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(495, 7, 'problem', 1151);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(496, 5, 'knowbasecategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(497, 6, 'itilcategory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(498, 6, 'location', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(499, 7, 'itiltemplate', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(500, 7, 'ticketrecurrent', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(501, 7, 'ticketcost', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(502, 1, 'change', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(503, 2, 'change', 1057);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(504, 7, 'ticketvalidation', 15376);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(505, 8, 'backup', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(506, 8, 'bookmark_public', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(507, 8, 'budget', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(508, 8, 'calendar', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(509, 8, 'cartridge', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(510, 8, 'change', 1057);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(511, 8, 'changevalidation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(512, 8, 'computer', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(513, 8, 'config', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(514, 8, 'consumable', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(515, 8, 'contact_enterprise', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(516, 8, 'contract', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(517, 8, 'device', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(518, 8, 'document', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(519, 8, 'domain', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(520, 8, 'dropdown', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(521, 8, 'entity', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(522, 8, 'followup', 8193);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(523, 8, 'global_validation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(524, 8, 'group', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(525, 8, 'infocom', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(526, 8, 'internet', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(527, 8, 'itilcategory', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(528, 8, 'knowbase', 10241);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(529, 8, 'knowbasecategory', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(530, 8, 'link', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(531, 8, 'location', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(532, 8, 'logs', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(533, 8, 'monitor', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(534, 8, 'cable_management', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(535, 8, 'networking', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(536, 8, 'notification', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(537, 8, 'password_update', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(538, 8, 'peripheral', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(539, 8, 'phone', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(540, 8, 'planning', 3073);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(541, 8, 'printer', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(542, 8, 'problem', 1057);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(543, 8, 'profile', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(544, 8, 'project', 1057);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(545, 8, 'projecttask', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(546, 8, 'queuednotification', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(547, 8, 'reminder_public', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(548, 8, 'reports', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(549, 8, 'reservation', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(550, 8, 'rssfeed_public', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(551, 8, 'rule_dictionnary_dropdown', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(552, 8, 'rule_dictionnary_printer', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(553, 8, 'rule_dictionnary_software', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(554, 8, 'rule_import', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(555, 8, 'rule_location', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(556, 8, 'rule_ldap', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(557, 8, 'rule_mailcollector', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(558, 8, 'rule_softwarecategories', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(559, 8, 'rule_ticket', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(560, 8, 'search_config', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(561, 8, 'show_group_hardware', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(562, 8, 'slm', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(563, 8, 'software', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(564, 8, 'solutiontemplate', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(565, 8, 'itilfollowuptemplate', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(566, 8, 'state', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(567, 8, 'statistic', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(568, 8, 'task', 8193);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(569, 8, 'taskcategory', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(570, 8, 'ticket', 138241);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(571, 8, 'ticketcost', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(572, 8, 'ticketrecurrent', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(573, 8, 'itiltemplate', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(574, 8, 'ticketvalidation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(575, 8, 'transfer', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(576, 8, 'typedoc', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(577, 8, 'user', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(578, 1, 'license', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(579, 2, 'license', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(580, 3, 'license', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(581, 4, 'license', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(582, 5, 'license', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(583, 6, 'license', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(584, 7, 'license', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(585, 8, 'license', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(586, 1, 'line', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(587, 2, 'line', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(588, 3, 'line', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(589, 4, 'line', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(590, 5, 'line', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(591, 6, 'line', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(592, 7, 'line', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(593, 8, 'line', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(594, 1, 'lineoperator', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(595, 2, 'lineoperator', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(596, 3, 'lineoperator', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(597, 4, 'lineoperator', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(598, 5, 'lineoperator', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(599, 6, 'lineoperator', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(600, 7, 'lineoperator', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(601, 8, 'lineoperator', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(602, 1, 'devicesimcard_pinpuk', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(603, 2, 'devicesimcard_pinpuk', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(604, 3, 'devicesimcard_pinpuk', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(605, 4, 'devicesimcard_pinpuk', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(606, 5, 'devicesimcard_pinpuk', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(607, 6, 'devicesimcard_pinpuk', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(608, 7, 'devicesimcard_pinpuk', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(609, 8, 'devicesimcard_pinpuk', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(610, 1, 'certificate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(611, 2, 'certificate', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(612, 3, 'certificate', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(613, 4, 'certificate', 255);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(614, 5, 'certificate', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(615, 6, 'certificate', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(616, 7, 'certificate', 127);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(617, 8, 'certificate', 33);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(618, 1, 'datacenter', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(619, 2, 'datacenter', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(620, 3, 'datacenter', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(621, 4, 'datacenter', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(622, 5, 'datacenter', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(623, 6, 'datacenter', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(624, 7, 'datacenter', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(625, 8, 'datacenter', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(626, 4, 'rule_asset', 1047);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(627, 1, 'personalization', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(628, 2, 'personalization', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(629, 3, 'personalization', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(630, 4, 'personalization', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(631, 5, 'personalization', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(632, 6, 'personalization', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(633, 7, 'personalization', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(634, 8, 'personalization', 3);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(635, 1, 'rule_asset', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(636, 2, 'rule_asset', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(637, 3, 'rule_asset', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(638, 5, 'rule_asset', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(639, 6, 'rule_asset', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(640, 7, 'rule_asset', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(641, 8, 'rule_asset', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(642, 1, 'global_validation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(643, 2, 'global_validation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(644, 3, 'global_validation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(645, 4, 'global_validation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(646, 5, 'global_validation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(647, 6, 'global_validation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(648, 7, 'global_validation', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(649, 1, 'cluster', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(650, 2, 'cluster', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(651, 3, 'cluster', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(652, 4, 'cluster', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(653, 5, 'cluster', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(654, 6, 'cluster', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(655, 7, 'cluster', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(656, 8, 'cluster', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(657, 1, 'externalevent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(658, 2, 'externalevent', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(659, 3, 'externalevent', 1055);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(660, 4, 'externalevent', 1055);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(661, 5, 'externalevent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(662, 6, 'externalevent', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(663, 7, 'externalevent', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(664, 8, 'externalevent', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(665, 1, 'dashboard', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(666, 2, 'dashboard', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(667, 3, 'dashboard', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(668, 4, 'dashboard', 23);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(669, 5, 'dashboard', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(670, 6, 'dashboard', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(671, 7, 'dashboard', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(672, 8, 'dashboard', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(673, 1, 'appliance', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(674, 2, 'appliance', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(675, 3, 'appliance', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(676, 4, 'appliance', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(677, 5, 'appliance', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(678, 6, 'appliance', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(679, 7, 'appliance', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(680, 8, 'appliance', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(681, 1, 'inventory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(682, 2, 'inventory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(683, 3, 'inventory', 3073);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(684, 4, 'inventory', 3073);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(685, 5, 'inventory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(686, 6, 'inventory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(687, 7, 'inventory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(688, 8, 'inventory', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(689, 1, 'pendingreason', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(690, 2, 'pendingreason', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(691, 3, 'pendingreason', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(692, 4, 'pendingreason', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(693, 5, 'pendingreason', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(694, 6, 'pendingreason', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(695, 7, 'pendingreason', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(696, 8, 'pendingreason', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(697, 1, 'database', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(698, 2, 'database', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(699, 3, 'database', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(700, 4, 'database', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(701, 5, 'database', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(702, 6, 'database', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(703, 7, 'database', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(704, 8, 'database', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(705, 1, 'recurrentchange', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(706, 2, 'recurrentchange', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(707, 3, 'recurrentchange', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(708, 4, 'recurrentchange', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(709, 5, 'recurrentchange', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(710, 6, 'recurrentchange', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(711, 7, 'recurrentchange', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(712, 8, 'recurrentchange', 1);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(713, 1, 'locked_field', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(714, 2, 'locked_field', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(715, 3, 'locked_field', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(716, 4, 'locked_field', 6);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(717, 5, 'locked_field', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(718, 6, 'locked_field', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(719, 7, 'locked_field', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(720, 8, 'locked_field', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(721, 1, 'snmpcredential', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(722, 2, 'snmpcredential', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(723, 3, 'snmpcredential', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(724, 4, 'snmpcredential', 31);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(725, 5, 'snmpcredential', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(726, 6, 'snmpcredential', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(727, 7, 'snmpcredential', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(728, 8, 'snmpcredential', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(729, 1, 'refusedequipment', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(730, 2, 'refusedequipment', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(731, 3, 'refusedequipment', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(732, 4, 'refusedequipment', 19);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(733, 5, 'refusedequipment', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(734, 6, 'refusedequipment', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(735, 7, 'refusedequipment', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(736, 8, 'refusedequipment', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(737, 1, 'agent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(738, 2, 'agent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(739, 3, 'agent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(740, 4, 'agent', 19);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(741, 5, 'agent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(742, 6, 'agent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(743, 7, 'agent', 0);
REPLACE INTO `glpi_profilerights` (`id`, `profiles_id`, `name`, `rights`) VALUES(744, 8, 'agent', 0);

--
-- Volcado de datos para la tabla `glpi_profiles`
--

REPLACE INTO `glpi_profiles` (`id`, `name`, `interface`, `is_default`, `helpdesk_hardware`, `helpdesk_item_type`, `ticket_status`, `date_mod`, `comment`, `problem_status`, `create_ticket_on_login`, `tickettemplates_id`, `changetemplates_id`, `problemtemplates_id`, `change_status`, `managed_domainrecordtypes`, `date_creation`) VALUES(1, 'Self-Service', 'helpdesk', 1, 1, '[\"Computer\",\"Monitor\",\"NetworkEquipment\",\"Peripheral\",\"Phone\",\"Printer\",\"Software\", \"DCRoom\", \"Rack\", \"Enclosure\", \"Database\"]', '{\"1\":{\"2\":0,\"3\":0,\"4\":0,\"5\":0,\"6\":0},\"2\":{\"1\":0,\"3\":0,\"4\":0,\"5\":0,\"6\":0},\"3\":{\"1\":0,\"2\":0,\"4\":0,\"5\":0,\"6\":0},\"4\":{\"1\":0,\"2\":0,\"3\":0,\"5\":0,\"6\":0},\"5\":{\"1\":0,\"2\":0,\"3\":0,\"4\":0},\"6\":{\"1\":0,\"2\":0,\"3\":0,\"4\":0,\"5\":0}}', NULL, '', '[]', 0, 0, 0, 0, NULL, '[]', NULL);
REPLACE INTO `glpi_profiles` (`id`, `name`, `interface`, `is_default`, `helpdesk_hardware`, `helpdesk_item_type`, `ticket_status`, `date_mod`, `comment`, `problem_status`, `create_ticket_on_login`, `tickettemplates_id`, `changetemplates_id`, `problemtemplates_id`, `change_status`, `managed_domainrecordtypes`, `date_creation`) VALUES(2, 'Observer', 'central', 0, 1, '[\"Computer\",\"Monitor\",\"NetworkEquipment\",\"Peripheral\",\"Phone\",\"Printer\",\"Software\", \"DCRoom\", \"Rack\", \"Enclosure\", \"Database\"]', '[]', NULL, '', '[]', 0, 0, 0, 0, NULL, '[]', NULL);
REPLACE INTO `glpi_profiles` (`id`, `name`, `interface`, `is_default`, `helpdesk_hardware`, `helpdesk_item_type`, `ticket_status`, `date_mod`, `comment`, `problem_status`, `create_ticket_on_login`, `tickettemplates_id`, `changetemplates_id`, `problemtemplates_id`, `change_status`, `managed_domainrecordtypes`, `date_creation`) VALUES(3, 'Admin', 'central', 0, 3, '[\"Computer\",\"Monitor\",\"NetworkEquipment\",\"Peripheral\",\"Phone\",\"Printer\",\"Software\", \"DCRoom\", \"Rack\", \"Enclosure\", \"Database\"]', '[]', NULL, '', '[]', 0, 0, 0, 0, NULL, '[-1]', NULL);
REPLACE INTO `glpi_profiles` (`id`, `name`, `interface`, `is_default`, `helpdesk_hardware`, `helpdesk_item_type`, `ticket_status`, `date_mod`, `comment`, `problem_status`, `create_ticket_on_login`, `tickettemplates_id`, `changetemplates_id`, `problemtemplates_id`, `change_status`, `managed_domainrecordtypes`, `date_creation`) VALUES(4, 'Super-Admin', 'central', 0, 3, '[\"Computer\",\"Monitor\",\"NetworkEquipment\",\"Peripheral\",\"Phone\",\"Printer\",\"Software\", \"DCRoom\", \"Rack\", \"Enclosure\", \"Database\"]', '[]', NULL, '', '[]', 0, 0, 0, 0, NULL, '[-1]', NULL);
REPLACE INTO `glpi_profiles` (`id`, `name`, `interface`, `is_default`, `helpdesk_hardware`, `helpdesk_item_type`, `ticket_status`, `date_mod`, `comment`, `problem_status`, `create_ticket_on_login`, `tickettemplates_id`, `changetemplates_id`, `problemtemplates_id`, `change_status`, `managed_domainrecordtypes`, `date_creation`) VALUES(5, 'Hotliner', 'central', 0, 3, '[\"Computer\",\"Monitor\",\"NetworkEquipment\",\"Peripheral\",\"Phone\",\"Printer\",\"Software\", \"DCRoom\", \"Rack\", \"Enclosure\", \"Database\"]', '[]', NULL, '', '[]', 1, 0, 0, 0, NULL, '[]', NULL);
REPLACE INTO `glpi_profiles` (`id`, `name`, `interface`, `is_default`, `helpdesk_hardware`, `helpdesk_item_type`, `ticket_status`, `date_mod`, `comment`, `problem_status`, `create_ticket_on_login`, `tickettemplates_id`, `changetemplates_id`, `problemtemplates_id`, `change_status`, `managed_domainrecordtypes`, `date_creation`) VALUES(6, 'Technician', 'central', 0, 3, '[\"Computer\",\"Monitor\",\"NetworkEquipment\",\"Peripheral\",\"Phone\",\"Printer\",\"Software\", \"DCRoom\", \"Rack\", \"Enclosure\", \"Database\"]', '[]', NULL, '', '[]', 0, 0, 0, 0, NULL, '[]', NULL);
REPLACE INTO `glpi_profiles` (`id`, `name`, `interface`, `is_default`, `helpdesk_hardware`, `helpdesk_item_type`, `ticket_status`, `date_mod`, `comment`, `problem_status`, `create_ticket_on_login`, `tickettemplates_id`, `changetemplates_id`, `problemtemplates_id`, `change_status`, `managed_domainrecordtypes`, `date_creation`) VALUES(7, 'Supervisor', 'central', 0, 3, '[\"Computer\",\"Monitor\",\"NetworkEquipment\",\"Peripheral\",\"Phone\",\"Printer\",\"Software\", \"DCRoom\", \"Rack\", \"Enclosure\", \"Database\"]', '[]', NULL, '', '[]', 0, 0, 0, 0, NULL, '[]', NULL);
REPLACE INTO `glpi_profiles` (`id`, `name`, `interface`, `is_default`, `helpdesk_hardware`, `helpdesk_item_type`, `ticket_status`, `date_mod`, `comment`, `problem_status`, `create_ticket_on_login`, `tickettemplates_id`, `changetemplates_id`, `problemtemplates_id`, `change_status`, `managed_domainrecordtypes`, `date_creation`) VALUES(8, 'Read-Only', 'central', 0, 0, '[]', '{\"1\":{\"2\":0,\"3\":0,\"4\":0,\"5\":0,\"6\":0},\"2\":{\"1\":0,\"3\":0,\"4\":0,\"5\":0,\"6\":0},\"3\":{\"1\":0,\"2\":0,\"4\":0,\"5\":0,\"6\":0},\"4\":{\"1\":0,\"2\":0,\"3\":0,\"5\":0,\"6\":0},\"5\":{\"1\":0,\"2\":0,\"3\":0,\"4\":0,\"6\":0},\"6\":{\"1\":0,\"2\":0,\"3\":0,\"4\":0,\"5\":0}}', NULL, 'This profile defines read-only access. It is used when objects are locked. It can also be used to give to users rights to unlock objects.', '{\"1\":{\"7\":0,\"2\":0,\"3\":0,\"4\":0,\"5\":0,\"8\":0,\"6\":0},\"7\":{\"1\":0,\"2\":0,\"3\":0,\"4\":0,\"5\":0,\"8\":0,\"6\":0},\"2\":{\"1\":0,\"7\":0,\"3\":0,\"4\":0,\"5\":0,\"8\":0,\"6\":0},\"3\":{\"1\":0,\"7\":0,\"2\":0,\"4\":0,\"5\":0,\"8\":0,\"6\":0},\"4\":{\"1\":0,\"7\":0,\"2\":0,\"3\":0,\"5\":0,\"8\":0,\"6\":0},\"5\":{\"1\":0,\"7\":0,\"2\":0,\"3\":0,\"4\":0,\"8\":0,\"6\":0},\"8\":{\"1\":0,\"7\":0,\"2\":0,\"3\":0,\"4\":0,\"5\":0,\"6\":0},\"6\":{\"1\":0,\"7\":0,\"2\":0,\"3\":0,\"4\":0,\"5\":0,\"8\":0}}', 0, 0, 0, 0, '{\"1\":{\"9\":0,\"10\":0,\"7\":0,\"4\":0,\"11\":0,\"12\":0,\"5\":0,\"8\":0,\"6\":0},\"9\":{\"1\":0,\"10\":0,\"7\":0,\"4\":0,\"11\":0,\"12\":0,\"5\":0,\"8\":0,\"6\":0},\"10\":{\"1\":0,\"9\":0,\"7\":0,\"4\":0,\"11\":0,\"12\":0,\"5\":0,\"8\":0,\"6\":0},\"7\":{\"1\":0,\"9\":0,\"10\":0,\"4\":0,\"11\":0,\"12\":0,\"5\":0,\"8\":0,\"6\":0},\"4\":{\"1\":0,\"9\":0,\"10\":0,\"7\":0,\"11\":0,\"12\":0,\"5\":0,\"8\":0,\"6\":0},\"11\":{\"1\":0,\"9\":0,\"10\":0,\"7\":0,\"4\":0,\"12\":0,\"5\":0,\"8\":0,\"6\":0},\"12\":{\"1\":0,\"9\":0,\"10\":0,\"7\":0,\"4\":0,\"11\":0,\"5\":0,\"8\":0,\"6\":0},\"5\":{\"1\":0,\"9\":0,\"10\":0,\"7\":0,\"4\":0,\"11\":0,\"12\":0,\"8\":0,\"6\":0},\"8\":{\"1\":0,\"9\":0,\"10\":0,\"7\":0,\"4\":0,\"11\":0,\"12\":0,\"5\":0,\"6\":0},\"6\":{\"1\":0,\"9\":0,\"10\":0,\"7\":0,\"4\":0,\"11\":0,\"12\":0,\"5\":0,\"8\":0}}', '[]', NULL);

--
-- Volcado de datos para la tabla `glpi_profiles_users`
--

REPLACE INTO `glpi_profiles_users` (`id`, `users_id`, `profiles_id`, `entities_id`, `is_recursive`, `is_dynamic`, `is_default_profile`) VALUES(2, 2, 4, 0, 1, 0, 0);
REPLACE INTO `glpi_profiles_users` (`id`, `users_id`, `profiles_id`, `entities_id`, `is_recursive`, `is_dynamic`, `is_default_profile`) VALUES(3, 3, 1, 0, 1, 0, 0);
REPLACE INTO `glpi_profiles_users` (`id`, `users_id`, `profiles_id`, `entities_id`, `is_recursive`, `is_dynamic`, `is_default_profile`) VALUES(4, 4, 6, 0, 1, 0, 0);
REPLACE INTO `glpi_profiles_users` (`id`, `users_id`, `profiles_id`, `entities_id`, `is_recursive`, `is_dynamic`, `is_default_profile`) VALUES(5, 5, 2, 0, 1, 0, 0);

--
-- Volcado de datos para la tabla `glpi_projectstates`
--

REPLACE INTO `glpi_projectstates` (`id`, `name`, `comment`, `color`, `is_finished`, `date_mod`, `date_creation`) VALUES(1, 'New', NULL, '#06ff00', 0, NULL, NULL);
REPLACE INTO `glpi_projectstates` (`id`, `name`, `comment`, `color`, `is_finished`, `date_mod`, `date_creation`) VALUES(2, 'Processing', NULL, '#ffb800', 0, NULL, NULL);
REPLACE INTO `glpi_projectstates` (`id`, `name`, `comment`, `color`, `is_finished`, `date_mod`, `date_creation`) VALUES(3, 'Closed', NULL, '#ff0000', 1, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_rackmodels`
--

REPLACE INTO `glpi_rackmodels` (`id`, `name`, `comment`, `product_number`, `date_mod`, `date_creation`, `pictures`) VALUES(1, 'RackModel1', 'Comment', '1213231', '2023-03-19 19:35:56', '2023-03-19 19:35:56', NULL);

--
-- Volcado de datos para la tabla `glpi_racks`
--

REPLACE INTO `glpi_racks` (`id`, `name`, `comment`, `entities_id`, `is_recursive`, `locations_id`, `serial`, `otherserial`, `rackmodels_id`, `manufacturers_id`, `racktypes_id`, `states_id`, `users_id_tech`, `groups_id_tech`, `width`, `height`, `depth`, `number_units`, `is_template`, `template_name`, `is_deleted`, `dcrooms_id`, `room_orientation`, `position`, `bgcolor`, `max_power`, `mesured_power`, `max_weight`, `date_mod`, `date_creation`) VALUES(1, 'Rack1', 'Comment', 0, 0, 1, '111111111111', '1232313', 1, 2, 1, 2, 0, 0, 0, 0, 0, 42, 0, NULL, 0, 1, 1, '1,1', '#fec95c', 0, 0, 0, '2023-03-19 19:36:30', '2023-03-19 19:36:30');

--
-- Volcado de datos para la tabla `glpi_racktypes`
--

REPLACE INTO `glpi_racktypes` (`id`, `entities_id`, `is_recursive`, `name`, `comment`, `date_creation`, `date_mod`) VALUES(1, 0, 0, 'RackType1', 'Comment', '2023-03-19 19:35:43', '2023-03-19 19:35:43');

--
-- Volcado de datos para la tabla `glpi_requesttypes`
--

REPLACE INTO `glpi_requesttypes` (`id`, `name`, `is_helpdesk_default`, `is_followup_default`, `is_mail_default`, `is_mailfollowup_default`, `is_active`, `is_ticketheader`, `is_itilfollowup`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'Helpdesk', 1, 1, 0, 0, 1, 1, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_requesttypes` (`id`, `name`, `is_helpdesk_default`, `is_followup_default`, `is_mail_default`, `is_mailfollowup_default`, `is_active`, `is_ticketheader`, `is_itilfollowup`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'E-Mail', 0, 0, 1, 1, 1, 1, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_requesttypes` (`id`, `name`, `is_helpdesk_default`, `is_followup_default`, `is_mail_default`, `is_mailfollowup_default`, `is_active`, `is_ticketheader`, `is_itilfollowup`, `comment`, `date_mod`, `date_creation`) VALUES(3, 'Phone', 0, 0, 0, 0, 1, 1, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_requesttypes` (`id`, `name`, `is_helpdesk_default`, `is_followup_default`, `is_mail_default`, `is_mailfollowup_default`, `is_active`, `is_ticketheader`, `is_itilfollowup`, `comment`, `date_mod`, `date_creation`) VALUES(4, 'Direct', 0, 0, 0, 0, 1, 1, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_requesttypes` (`id`, `name`, `is_helpdesk_default`, `is_followup_default`, `is_mail_default`, `is_mailfollowup_default`, `is_active`, `is_ticketheader`, `is_itilfollowup`, `comment`, `date_mod`, `date_creation`) VALUES(5, 'Written', 0, 0, 0, 0, 1, 1, 1, NULL, NULL, NULL);
REPLACE INTO `glpi_requesttypes` (`id`, `name`, `is_helpdesk_default`, `is_followup_default`, `is_mail_default`, `is_mailfollowup_default`, `is_active`, `is_ticketheader`, `is_itilfollowup`, `comment`, `date_mod`, `date_creation`) VALUES(6, 'Other', 0, 0, 0, 0, 1, 1, 1, NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_ruleactions`
--

REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(1, 1, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(2, 2, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(3, 3, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(4, 4, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(5, 5, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(6, 6, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(7, 7, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(8, 8, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(9, 9, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(10, 10, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(11, 11, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(12, 12, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(13, 13, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(14, 14, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(15, 15, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(16, 16, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(17, 17, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(18, 18, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(19, 19, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(20, 20, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(21, 21, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(22, 22, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(23, 23, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(24, 24, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(25, 25, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(26, 26, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(27, 27, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(28, 28, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(29, 29, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(30, 30, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(31, 31, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(32, 32, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(33, 33, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(34, 34, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(35, 35, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(36, 36, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(37, 37, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(38, 38, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(39, 39, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(40, 40, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(41, 41, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(42, 42, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(43, 43, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(44, 44, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(45, 45, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(46, 46, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(47, 47, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(48, 48, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(49, 49, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(50, 50, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(51, 51, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(52, 52, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(53, 53, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(54, 54, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(55, 55, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(56, 56, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(57, 57, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(58, 58, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(59, 59, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(60, 60, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(61, 61, 'assign', '_inventory', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(62, 62, 'assign', '_inventory', '2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(63, 63, 'assign', 'entities_id', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(64, 64, 'assign', '_refuse_email_no_response', '1');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(65, 65, 'assign', '_refuse_email_no_response', '1');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(66, 66, 'assign', 'entities_id', '0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(67, 67, 'assign', '_import_category', '1');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(68, 68, 'fromitem', 'locations_id', '1');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(69, 69, 'fromuser', 'locations_id', '1');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(70, 70, 'regex_result', '_affect_user_by_regex', '#0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(71, 71, 'regex_result', '_affect_user_by_regex', '#0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(72, 72, 'regex_result', '_affect_user_by_regex', '#0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(73, 73, 'append_regex_result', 'name', '#0');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(74, 74, 'append_regex_result', 'name', '#1');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(75, 75, 'append_regex_result', 'name', '#1 #2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(76, 76, 'append_regex_result', 'name', '#1');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(77, 77, 'append_regex_result', 'name', '#2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(78, 78, 'append_regex_result', 'name', '#3');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(79, 79, 'append_regex_result', 'name', '#2');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(80, 80, 'append_regex_result', 'name', '#4');
REPLACE INTO `glpi_ruleactions` (`id`, `rules_id`, `action_type`, `field`, `value`) VALUES(81, 81, 'append_regex_result', 'name', '#4');

--
-- Volcado de datos para la tabla `glpi_rulecriterias`
--

REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(1, 1, 'partial', 0, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(2, 1, 'itemtype', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(3, 2, 'itemtype', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(4, 2, 'mac', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(5, 2, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(6, 2, 'ifnumber', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(7, 2, 'ifnumber', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(8, 2, 'link_criteria_port', 203, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(9, 3, 'itemtype', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(10, 3, 'mac', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(11, 3, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(12, 3, 'ifnumber', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(13, 3, 'ifnumber', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(14, 4, 'itemtype', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(15, 4, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(16, 4, 'ifnumber', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(17, 5, 'itemtype', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(18, 5, 'ip', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(19, 5, 'ip', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(20, 5, 'ifdescr', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(21, 5, 'ifdescr', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(22, 5, 'link_criteria_port', 203, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(23, 6, 'itemtype', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(24, 6, 'ip', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(25, 6, 'ip', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(26, 6, 'ifdescr', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(27, 6, 'ifdescr', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(28, 7, 'itemtype', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(29, 7, 'ip', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(30, 7, 'ifdescr', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(31, 8, 'itemtype', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(32, 8, 'mac', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(33, 8, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(34, 8, 'only_these_criteria', 204, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(35, 9, 'itemtype', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(36, 9, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(37, 9, 'only_these_criteria', 204, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(38, 10, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(39, 10, 'name', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(40, 11, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(41, 11, 'serial', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(42, 11, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(43, 11, 'uuid', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(44, 11, 'uuid', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(45, 12, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(46, 12, 'serial', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(47, 12, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(48, 12, 'uuid', 30, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(49, 13, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(50, 13, 'uuid', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(51, 13, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(52, 14, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(53, 14, 'serial', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(54, 14, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(55, 15, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(56, 15, 'uuid', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(57, 15, 'uuid', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(58, 16, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(59, 16, 'mac', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(60, 16, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(61, 17, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(62, 17, 'name', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(63, 17, 'name', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(64, 18, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(65, 18, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(66, 19, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(67, 19, 'uuid', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(68, 20, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(69, 20, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(70, 21, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(71, 21, 'name', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(72, 22, 'itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(73, 23, 'itemtype', 0, 'Printer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(74, 23, 'name', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(75, 24, 'itemtype', 0, 'Printer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(76, 24, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(77, 24, 'serial', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(78, 25, 'itemtype', 0, 'Printer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(79, 25, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(80, 25, 'mac', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(81, 26, 'itemtype', 0, 'Printer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(82, 26, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(83, 27, 'itemtype', 0, 'Printer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(84, 27, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(85, 28, 'itemtype', 0, 'Printer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(86, 29, 'itemtype', 0, 'NetworkEquipment');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(87, 29, 'name', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(88, 30, 'itemtype', 0, 'NetworkEquipment');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(89, 30, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(90, 30, 'serial', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(91, 31, 'itemtype', 0, 'NetworkEquipment');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(92, 31, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(93, 31, 'mac', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(94, 32, 'itemtype', 0, 'NetworkEquipment');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(95, 32, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(96, 33, 'itemtype', 0, 'NetworkEquipment');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(97, 33, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(98, 34, 'itemtype', 0, 'NetworkEquipment');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(99, 35, 'itemtype', 0, 'Peripheral');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(100, 35, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(101, 35, 'serial', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(102, 36, 'itemtype', 0, 'Peripheral');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(103, 36, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(104, 37, 'itemtype', 0, 'Peripheral');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(105, 38, 'itemtype', 0, 'Monitor');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(106, 38, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(107, 38, 'serial', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(108, 39, 'itemtype', 0, 'Monitor');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(109, 39, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(110, 40, 'itemtype', 0, 'Monitor');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(111, 41, 'itemtype', 0, 'Phone');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(112, 41, 'name', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(113, 42, 'itemtype', 0, 'Phone');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(114, 42, 'mac', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(115, 42, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(116, 43, 'itemtype', 0, 'Phone');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(117, 43, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(118, 44, 'itemtype', 0, 'Phone');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(119, 45, 'itemtype', 0, 'Cluster');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(120, 45, 'uuid', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(121, 45, 'uuid', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(122, 46, 'itemtype', 0, 'Cluster');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(123, 46, 'uuid', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(124, 47, 'itemtype', 0, 'Cluster');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(125, 48, 'itemtype', 0, 'Enclosure');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(126, 48, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(127, 48, 'serial', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(128, 49, 'itemtype', 0, 'Enclosure');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(129, 49, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(130, 50, 'itemtype', 0, 'Enclosure');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(131, 51, 'name', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(132, 52, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(133, 52, 'serial', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(134, 53, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(135, 53, 'mac', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(136, 54, 'serial', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(137, 55, 'mac', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(138, 56, 'itemtype', 0, '');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(139, 57, 'itemtype', 0, 'DatabaseInstance');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(140, 57, 'name', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(141, 57, 'name', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(142, 57, 'linked_item', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(143, 58, 'itemtype', 0, 'DatabaseInstance');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(144, 58, 'name', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(145, 59, 'itemtype', 0, 'DatabaseInstance');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(146, 60, 'itemtype', 0, 'Unmanaged');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(147, 60, 'name', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(148, 60, 'name', 10, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(149, 61, 'itemtype', 0, 'Unmanaged');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(150, 61, 'name', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(151, 62, 'itemtype', 0, 'Unmanaged');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(152, 63, 'subject', 6, '/.*/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(153, 64, 'x-auto-response-suppress', 6, '/\\S+/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(154, 65, 'auto-submitted', 6, '/^(?!.*no).+$/i');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(155, 66, 'TYPE', 0, '3');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(156, 66, 'TYPE', 0, '2');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(157, 67, 'name', 0, '*');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(158, 68, 'locations_id', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(159, 68, 'items_locations', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(160, 69, 'locations_id', 9, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(161, 69, '_locations_id_of_requester', 8, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(162, 70, '_itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(163, 70, '_auto', 0, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(164, 70, 'contact', 6, '/(.*)@/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(165, 71, '_itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(166, 71, '_auto', 0, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(167, 71, 'contact', 6, '/(.*)[,|\\/]/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(168, 72, '_itemtype', 0, 'Computer');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(169, 72, '_auto', 0, '1');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(170, 72, 'contact', 6, '/(.*)/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(171, 73, 'os_name', 6, '/(SUSE|SunOS|Red Hat|CentOS|Ubuntu|Debian|Fedora|AlmaLinux|Oracle)(?:\\D+|)([\\d.]+) ?(?:\\(?([\\w ]+)\\)?)?/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(172, 74, 'os_name', 6, '/(Microsoft)(?&#62;\\(R\\)|®)? (Windows) (XP|\\d\\.\\d|\\d{1,4}|Vista)(™)? ?(.*)/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(173, 75, 'os_name', 6, '/(Microsoft)(?&#62;\\(R\\)|®)? (?:(Hyper-V|Windows)(?:\\(R\\))?) ((?:Server|))(?:\\(R\\)|®)? (\\d{4}(?: R2)?)(?:[,\\s]++)?([^\\s]*)(?: Edition(?: x64)?)?$/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(174, 76, 'os_name', 6, '/(SUSE|SunOS|Red Hat|CentOS|Ubuntu|Debian|Fedora|AlmaLinux|Oracle)(?:\\D+|)([\\d.]+) ?(?:\\(?([\\w ]+)\\)?)?/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(175, 77, 'os_name', 6, '/(Microsoft)(?&#62;\\(R\\)|®)? (Windows) (XP|\\d\\.\\d|\\d{1,4}|Vista)(™)? ?(.*)/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(176, 78, 'os_name', 6, '/(Microsoft)(?&#62;\\(R\\)|®)? (?:(Hyper-V|Windows)(?:\\(R\\))?) ((?:Server|))(?:\\(R\\)|®)? (\\d{4}(?: R2)?)(?:[,\\s]++)?([^\\s]*)(?: Edition(?: x64)?)?$/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(177, 79, 'os_name', 6, '/(SUSE|SunOS|Red Hat|CentOS|Ubuntu|Debian|Fedora|AlmaLinux|Oracle)(?:\\D+|)([\\d.]+) ?(?:\\(?([\\w ]+)\\)?)?/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(178, 80, 'os_name', 6, '/(Microsoft)(?&#62;\\(R\\)|®)? (Windows) (XP|\\d\\.\\d|\\d{1,4}|Vista)(™)? ?(.*)/');
REPLACE INTO `glpi_rulecriterias` (`id`, `rules_id`, `criteria`, `condition`, `pattern`) VALUES(179, 81, 'os_name', 6, '/(Microsoft)(?&#62;\\(R\\)|®)? (?:(Hyper-V|Windows)(?:\\(R\\))?) ((?:Server|))(?:\\(R\\)|®)? (\\d{4}(?: R2)?)(?:[,\\s]++)?([^\\s]*)(?: Edition(?: x64)?)?$/');

--
-- Volcado de datos para la tabla `glpi_rulerightparameters`
--

REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(1, '(LDAP)Organization', 'o', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(2, '(LDAP)Common Name', 'cn', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(3, '(LDAP)Department Number', 'departmentnumber', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(4, '(LDAP)Email', 'mail', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(5, 'Object Class', 'objectclass', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(6, '(LDAP)User ID', 'uid', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(7, '(LDAP)Telephone Number', 'phone', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(8, '(LDAP)Employee Number', 'employeenumber', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(9, '(LDAP)Manager', 'manager', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(10, '(LDAP)DistinguishedName', 'dn', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(12, '(AD)User ID', 'samaccountname', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(13, '(LDAP) Title', 'title', NULL, NULL, NULL);
REPLACE INTO `glpi_rulerightparameters` (`id`, `name`, `value`, `comment`, `date_mod`, `date_creation`) VALUES(14, '(LDAP) MemberOf', 'memberof', NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_rules`
--

REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(1, 0, 'RuleImportAsset', 1, 'No creation on partial import', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_no_creation_on_partial_import', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(2, 0, 'RuleImportAsset', 2, 'Global update (by mac+ifnumber restricted port)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_update_mac_ifnumber_restricted_port', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(3, 0, 'RuleImportAsset', 3, 'Global update (by mac+ifnumber not restricted port)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_update_mac_ifnumber_no_restricted_port', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(4, 0, 'RuleImportAsset', 4, 'Global import (by mac+ifnumber)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_import_mac_ifnumber', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(5, 0, 'RuleImportAsset', 5, 'Global update (by ip+ifdescr restricted port)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_update_mac_ifdescr_restricted_port', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(6, 0, 'RuleImportAsset', 6, 'Global update (by ip+ifdescr not restricted port)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_update_ip_ifdescr_no_restricted_port', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(7, 0, 'RuleImportAsset', 7, 'Global import (by ip+ifdescr)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_import_ip_ifdescr', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(8, 0, 'RuleImportAsset', 8, 'Update only mac address (mac on switch port)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_update_only_mac_adress', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(9, 0, 'RuleImportAsset', 9, 'Import only mac address (mac on switch port)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_import_only_mac_adress', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(10, 0, 'RuleImportAsset', 10, 'Computer constraint (name)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_constraint_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(11, 0, 'RuleImportAsset', 11, 'Computer update (by serial + uuid)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_update_serial_uuid', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(12, 0, 'RuleImportAsset', 12, 'Computer update (by serial + uuid is empty in GLPI)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_update_serial_uuid_empty', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(13, 0, 'RuleImportAsset', 13, 'Computer import (by serial + uuid)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_import_serial_uuid', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(14, 0, 'RuleImportAsset', 14, 'Computer update (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_update_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(15, 0, 'RuleImportAsset', 15, 'Computer update (by uuid)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_update_uuid', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(16, 0, 'RuleImportAsset', 16, 'Computer update (by mac)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_update_mac', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(17, 0, 'RuleImportAsset', 17, 'Computer update (by name)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_update_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(18, 0, 'RuleImportAsset', 18, 'Computer import (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_import_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(19, 0, 'RuleImportAsset', 19, 'Computer import (by uuid)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_import_uuid', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(20, 0, 'RuleImportAsset', 20, 'Computer import (by mac)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_import_mac', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(21, 0, 'RuleImportAsset', 21, 'Computer import (by name)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_import_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(22, 0, 'RuleImportAsset', 22, 'Computer import denied', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_computer_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(23, 0, 'RuleImportAsset', 23, 'Printer constraint (name)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_printer_constraint_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(24, 0, 'RuleImportAsset', 24, 'Printer update (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_printer_update_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(25, 0, 'RuleImportAsset', 25, 'Printer update (by mac)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_printer_update_mac', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(26, 0, 'RuleImportAsset', 26, 'Printer import (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_printer_import_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(27, 0, 'RuleImportAsset', 27, 'Printer import (by mac)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_printer_import_mac', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(28, 0, 'RuleImportAsset', 28, 'Printer import denied', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_printer_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(29, 0, 'RuleImportAsset', 29, 'NetworkEquipment constraint (name)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_networkequipment_constraint_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(30, 0, 'RuleImportAsset', 30, 'NetworkEquipment update (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_networkequipment_update_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(31, 0, 'RuleImportAsset', 31, 'NetworkEquipment update (by mac)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_networkequipment_update_mac', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(32, 0, 'RuleImportAsset', 32, 'NetworkEquipment import (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_networkequipment_import_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(33, 0, 'RuleImportAsset', 33, 'NetworkEquipment import (by mac)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_networkequipment_import_mac', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(34, 0, 'RuleImportAsset', 34, 'NetworkEquipment import denied', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_networkequipment_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(35, 0, 'RuleImportAsset', 35, 'Device update (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_device_update_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(36, 0, 'RuleImportAsset', 36, 'Device import (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_device_importe_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(37, 0, 'RuleImportAsset', 37, 'Device import denied', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_device_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(38, 0, 'RuleImportAsset', 38, 'Monitor update (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_monitor_update_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(39, 0, 'RuleImportAsset', 39, 'Monitor import (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_monitor_import_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(40, 0, 'RuleImportAsset', 40, 'Monitor import denied', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_monitor_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(41, 0, 'RuleImportAsset', 41, 'Phone constraint (name)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_phone_constraint_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(42, 0, 'RuleImportAsset', 42, 'Phone update (by mac)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_phone_update_mac', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(43, 0, 'RuleImportAsset', 43, 'Phone import (by mac)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_phone_import_mac', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(44, 0, 'RuleImportAsset', 44, 'Phone import denied', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_phone_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(45, 0, 'RuleImportAsset', 45, 'Cluster update (by uuid)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_cluster_update_uuid', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(46, 0, 'RuleImportAsset', 46, 'Cluster import (by uuid)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_cluster_import_uuid', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(47, 0, 'RuleImportAsset', 47, 'Cluster import denied', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_cluster_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(48, 0, 'RuleImportAsset', 48, 'Enclosure update (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_enclosure_update_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(49, 0, 'RuleImportAsset', 49, 'Enclosure import (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_enclosure_import_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(50, 0, 'RuleImportAsset', 50, 'Enclosure import denied', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_enclosure_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(51, 0, 'RuleImportAsset', 51, 'Global constraint (name)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_constraint_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(52, 0, 'RuleImportAsset', 52, 'Global update (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_update_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(53, 0, 'RuleImportAsset', 53, 'Global update (by mac)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_update_mac', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(54, 0, 'RuleImportAsset', 54, 'Global import (by serial)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_import_serial', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(55, 0, 'RuleImportAsset', 55, 'Global import (by mac)', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_import_mac', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(56, 0, 'RuleImportAsset', 56, 'Global import denied', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_global_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(57, 0, 'RuleImportAsset', 57, 'Database update (by name)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_database_update_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(58, 0, 'RuleImportAsset', 58, 'Database import (by name)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_database_import_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(59, 0, 'RuleImportAsset', 59, 'Database import denied', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_database_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(60, 0, 'RuleImportAsset', 60, 'Unmanaged update (by name)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_unmanaged_update_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(61, 0, 'RuleImportAsset', 61, 'Unmanaged import (by name)', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_unmanaged_import_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(62, 0, 'RuleImportAsset', 62, 'Unmanaged import denied', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_import_asset_unmanaged_import_denied', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(63, 0, 'RuleMailCollector', 3, 'Root', '', 'OR', 1, '', '2023-03-17 19:45:27', 0, 'glpi_rule_mail_collector_root', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(64, 0, 'RuleMailCollector', 1, 'X-Auto-Response-Suppress', 'Exclude Auto-Reply emails using X-Auto-Response-Suppress header', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_mail_collector_x_auto_response_suppress', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(65, 0, 'RuleMailCollector', 2, 'Auto-Reply Auto-Submitted', 'Exclude Auto-Reply emails using Auto-Submitted header', 'OR', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_mail_collector_auto_reply_auto_submitted', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(66, 0, 'RuleRight', 1, 'Root', '', 'OR', 1, '', '2023-03-17 19:45:27', 0, 'glpi_rule_right_root', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(67, 0, 'RuleSoftwareCategory', 1, 'Import category from inventory tool', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_rule_software_category_import_category_from_inventory_tool', 1, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(68, 0, 'RuleTicket', 1, 'Ticket location from item', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_rule_ticket_location_from_item', 1, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(69, 0, 'RuleTicket', 2, 'Ticket location from user', '', 'AND', 0, '', '2023-03-17 19:45:27', 1, 'glpi_rule_rule_ticket_location_from_user', 1, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(70, 0, 'RuleAsset', 1, 'Domain user assignation', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_rule_asset_domain_user_assignation', 3, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(71, 0, 'RuleAsset', 2, 'Multiple users: assign to the first', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_rule_asset_multiple_user_assign_to_first', 3, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(72, 0, 'RuleAsset', 3, 'One user assignation', '', 'AND', 1, '', '2023-03-17 19:45:27', 1, 'glpi_rule_rule_asset_one_user_assignation', 3, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(73, 0, 'RuleDictionnaryOperatingSystem', 1, 'Clean Linux OS Name', '', 'AND', 0, '/(SUSE|SunOS|Red Hat|CentOS|Ubuntu|Debian|Fedora|AlmaLinux|Oracle)(?:\\D+|)([\\d.]+) ?(?:\\(?([\\w ]+)\\)?)?/\n\n            Example :\n            Ubuntu 22.04.1 LTS -&#62; #0 = Ubuntu\n            SUSE Linux Enterprise Server 11 (x86_64)  -&#62;#0 = SUSE\n            SunOS -&#62; #0 = SunOS\n            Red Hat Enterprise Linux Server release 7.9 (Maipo) -&#62; #0 = Red Hat\n            Oracle Linux Server release 7.3 -&#62; #0 = Oracle\n            Fedora release 36 (Thirty Six) -&#62; #0 = Fedora\n            Debian GNU/Linux 9.5 (stretch) -&#62; #0 = Debian\n            CentOS Stream release 8 -&#62; #0 = CentOS\n            AlmaLinux 9.0 (Emerald Puma) -&#62; #0 = AlmaLinux', '2023-03-17 19:45:27', 1, 'clean_linux_os_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(74, 0, 'RuleDictionnaryOperatingSystem', 2, 'Clean Windows OS Name', '', 'AND', 0, '/(Microsoft)(?&#62;\\(R\\)|®)? (Windows) (XP|\\d\\.\\d|\\d{1,4}|Vista)(™)? ?(.*)/\n\n            Example :\n            Microsoft Windows XP Professionnel -&#62; #1 : Windows\n            Microsoft Windows 7 Enterprise  -&#62; #1 : Windows\n            Microsoft® Windows Vista Professionnel  -&#62; #1 : Windows\n            Microsoft Windows XP Édition familiale  -&#62; #1 : Windows\n            Microsoft Windows 10 Entreprise  -&#62; #1 : Windows\n            Microsoft Windows 10 Professionnel  -&#62; #1 : Windows\n            Microsoft Windows 11 Professionnel  -&#62; #1 : Windows', '2023-03-17 19:45:27', 1, 'clean_windows_os_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(75, 0, 'RuleDictionnaryOperatingSystem', 3, 'Clean Windows Server OS Name', '', 'AND', 0, '/(Microsoft)(?&#62;\\(R\\)|®)? (?:(Hyper-V|Windows)(?:\\(R\\))?) ((?:Server|))(?:\\(R\\)|®)? (\\d{4}(?: R2)?)(?:[,\\s]++)?([^\\s]*)(?: Edition(?: x64)?)?$/\n\n            Example :\n            Microsoft Windows Server 2012 R2 Datacenter -&#62; #1 #2 : Windows Server\n            Microsoft(R) Windows(R) Server 2003, Standard Edition x64 -&#62; #1 #2 : Windows Server\n            Microsoft Hyper-V Server 2012 R2 -&#62; #1 #2 : Hyper-V Server\n            Microsoft® Windows Server® 2008 Standard -&#62; #1 #2 : Windows Server', '2023-03-17 19:45:27', 1, 'clean_windows_server_os_name', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(76, 0, 'RuleDictionnaryOperatingSystemVersion', 1, 'Clean Linux OS Version', '', 'AND', 0, '/(SUSE|SunOS|Red Hat|CentOS|Ubuntu|Debian|Fedora|AlmaLinux|Oracle)(?:\\D+|)([\\d.]+) ?(?:\\(?([\\w ]+)\\)?)?/\n\n            Example :\n            Ubuntu 22.04.1 LTS -&#62; #1 = 22.04.1\n            SUSE Linux Enterprise Server 11 (x86_64) -&#62; #1 =  11\n            SunOS 5.10 -&#62; #1 = 5.10\n            Red Hat Enterprise Linux Server release 7.9 (Maipo) -&#62; #1 = 7.9\n            Oracle Linux Server release 7.3 -&#62; #1 = 7.3\n            Fedora release 36 (Thirty Six) -&#62; #1 =  36\n            Debian GNU/Linux 9.5 (stretch) -&#62; #1 = 9.5\n            CentOS release 6.9 (Final) -&#62; #1 = 6.9\n            AlmaLinux 9.0 (Emerald Puma) -&#62; #1 = 9.0', '2023-03-17 19:45:27', 1, 'clean_linux_os_version', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(77, 0, 'RuleDictionnaryOperatingSystemVersion', 2, 'Clean Windows OS Version', '', 'AND', 0, '/(Microsoft)(?&#62;\\(R\\)|®)? (Windows) (XP|\\d\\.\\d|\\d{1,4}|Vista)(™)? ?(.*)/\n\n            Example :\n            Microsoft Windows XP Professionnel -&#62; #2 : XP\n            Microsoft Windows 7 Enterprise  -&#62; #2 : 7\n            Microsoft® Windows Vista Professionnel  -&#62; #2 : Vista\n            Microsoft Windows XP Édition familiale  -&#62; #2 : XP\n            Microsoft Windows 10 Entreprise  -&#62; #2 : 10\n            Microsoft Windows 10 Professionnel  -&#62; #2 : 10\n            Microsoft Windows 11 Professionnel  -&#62; #2 : 11', '2023-03-17 19:45:27', 1, 'clean_windows_os_version', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(78, 0, 'RuleDictionnaryOperatingSystemVersion', 3, 'Clean Windows Server OS Version', '', 'AND', 0, '/(Microsoft)(?&#62;\\(R\\)|®)? (?:(Hyper-V|Windows)(?:\\(R\\))?) ((?:Server|))(?:\\(R\\)|®)? (\\d{4}(?: R2)?)(?:[,\\s]++)?([^\\s]*)(?: Edition(?: x64)?)?$/\n\n            Example :\n            Microsoft Windows Server 2012 R2 Datacenter -&#62; #3 : 2012 R2\n            Microsoft(R) Windows(R) Server 2003, Standard Edition x64 -&#62; #3 : 2003\n            Microsoft Hyper-V Server 2012 R2 -&#62; #3 : 2012 R2\n            Microsoft® Windows Server® 2008 Standard -&#62; #3 : 2008', '2023-03-17 19:45:27', 1, 'clean_windows_server_os_version', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(79, 0, 'RuleDictionnaryOperatingSystemEdition', 1, 'Clean Linux OS Edition', '', 'AND', 0, '/(SUSE|SunOS|Red Hat|CentOS|Ubuntu|Debian|Fedora|AlmaLinux|Oracle)(?:\\D+|)([\\d.]+) ?(?:\\(?([\\w ]+)\\)?)?/\n\n        Example :\n        Ubuntu 22.04.1 LTS -&#62; #2 = LTS\n        SUSE Linux Enterprise Server 11 (x86_64) -&#62; #2 = x86_64\n        Red Hat Enterprise Linux Server release 7.9 (Maipo) -&#62; #2 = Maipo\n        Red Hat Enterprise Linux Server release 6.10 (Santiago) -&#62; #2 = Santiago\n        Fedora release 36 (Thirty Six) -&#62; #2 = Thirty Six\n        Debian GNU/Linux 9.5 (stretch) -&#62; #2 = stretch\n        Debian GNU/Linux 8.9 (jessie) -&#62; #2 = jessie\n        CentOS Linux release 7.2.1511 (Core) -&#62; #2 = Core\n        AlmaLinux 9.0 (Emerald Puma) -&#62; #2 = Emerald Puma\n        AlmaLinux 8.6 (Sky Tiger) -&#62; #2 = Sky Tiger', '2023-03-17 19:45:27', 1, 'clean_linux_os_edition', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(80, 0, 'RuleDictionnaryOperatingSystemEdition', 2, 'Clean Windows OS Edition', '', 'AND', 0, '/(Microsoft)(?&#62;\\(R\\)|®)? (Windows) (XP|\\d\\.\\d|\\d{1,4}|Vista)(™)? ?(.*)/\n\n        Example :\n        Microsoft Windows XP Professionnel -&#62; #4 : Professionnel\n        Microsoft Windows 7 Enterprise  -&#62; #4 : Enterprise\n        Microsoft® Windows Vista Professionnel  -&#62; #4 : Professionnel\n        Microsoft Windows XP Édition familiale  -&#62; #4 : Édition familiale\n        Microsoft Windows 10 Entreprise  -&#62; #4 : Entreprise\n        Microsoft Windows 10 Professionnel  -&#62; #4 : Professionnel\n        Microsoft Windows 11 Professionnel  -&#62; #4 : Professionnel', '2023-03-17 19:45:27', 1, 'clean_windows_os_edition', 0, '2023-03-17 19:45:27');
REPLACE INTO `glpi_rules` (`id`, `entities_id`, `sub_type`, `ranking`, `name`, `description`, `match`, `is_active`, `comment`, `date_mod`, `is_recursive`, `uuid`, `condition`, `date_creation`) VALUES(81, 0, 'RuleDictionnaryOperatingSystemEdition', 3, 'Clean Windows Server OS Edition', '', 'AND', 0, '/(Microsoft)(?&#62;\\(R\\)|®)? (?:(Hyper-V|Windows)(?:\\(R\\))?) ((?:Server|))(?:\\(R\\)|®)? (\\d{4}(?: R2)?)(?:[,\\s]++)?([^\\s]*)(?: Edition(?: x64)?)?$/\n\n        Example :\n        Microsoft Windows Server 2012 R2 Datacenter -&#62; #4 : Datacenter\n        Microsoft(R) Windows(R) Server 2003, Standard Edition x64 -&#62; #4 : Standard\n        Microsoft Hyper-V Server 2012 R2 -&#62; #4 :\n        Microsoft® Windows Server® 2008 Standard -&#62; #4: Standard', '2023-03-17 19:45:27', 1, 'clean_windows_server_os_edition', 0, '2023-03-17 19:45:27');

--
-- Volcado de datos para la tabla `glpi_snmpcredentials`
--

REPLACE INTO `glpi_snmpcredentials` (`id`, `name`, `snmpversion`, `community`, `username`, `authentication`, `auth_passphrase`, `encryption`, `priv_passphrase`, `is_deleted`) VALUES(1, 'Public community v1', '1', 'public', NULL, NULL, NULL, NULL, NULL, 0);
REPLACE INTO `glpi_snmpcredentials` (`id`, `name`, `snmpversion`, `community`, `username`, `authentication`, `auth_passphrase`, `encryption`, `priv_passphrase`, `is_deleted`) VALUES(2, 'Public community v2c', '2', 'public', NULL, NULL, NULL, NULL, NULL, 0);

--
-- Volcado de datos para la tabla `glpi_socketmodels`
--

REPLACE INTO `glpi_socketmodels` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'Socket1', 'comment', '2023-03-19 19:39:44', '2023-03-19 19:39:44');
REPLACE INTO `glpi_socketmodels` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'SocketModel1', 'comment', '2023-03-19 19:40:04', '2023-03-19 19:40:04');

--
-- Volcado de datos para la tabla `glpi_sockets`
--

REPLACE INTO `glpi_sockets` (`id`, `position`, `locations_id`, `name`, `socketmodels_id`, `wiring_side`, `itemtype`, `items_id`, `networkports_id`, `comment`, `date_mod`, `date_creation`) VALUES(1, -1, 1, 'Socket1', 2, 1, 'Computer', 1, 0, 'comment', '2023-03-19 19:40:20', '2023-03-19 19:40:20');

--
-- Volcado de datos para la tabla `glpi_softwarecategories`
--

REPLACE INTO `glpi_softwarecategories` (`id`, `name`, `comment`, `softwarecategories_id`, `completename`, `level`, `ancestors_cache`, `sons_cache`) VALUES(1, 'Inventoried', NULL, 0, 'Software from inventories', 1, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_softwarelicensetypes`
--

REPLACE INTO `glpi_softwarelicensetypes` (`id`, `name`, `comment`, `date_mod`, `date_creation`, `softwarelicensetypes_id`, `level`, `ancestors_cache`, `sons_cache`, `entities_id`, `is_recursive`, `completename`) VALUES(1, 'OEM', NULL, NULL, NULL, 0, 0, NULL, NULL, 0, 1, 'OEM');

--
-- Volcado de datos para la tabla `glpi_softwares`
--

REPLACE INTO `glpi_softwares` (`id`, `entities_id`, `is_recursive`, `name`, `comment`, `locations_id`, `users_id_tech`, `groups_id_tech`, `is_update`, `softwares_id`, `manufacturers_id`, `is_deleted`, `is_template`, `template_name`, `date_mod`, `users_id`, `groups_id`, `ticket_tco`, `is_helpdesk_visible`, `softwarecategories_id`, `is_valid`, `date_creation`, `pictures`) VALUES(1, 0, 0, 'Software1', 'Software1Comment', 1, 0, 0, 0, 0, 0, 0, 0, NULL, '2023-03-19 19:20:51', 0, 0, '0.0000', 1, 1, 1, '2023-03-19 19:20:51', NULL);
REPLACE INTO `glpi_softwares` (`id`, `entities_id`, `is_recursive`, `name`, `comment`, `locations_id`, `users_id_tech`, `groups_id_tech`, `is_update`, `softwares_id`, `manufacturers_id`, `is_deleted`, `is_template`, `template_name`, `date_mod`, `users_id`, `groups_id`, `ticket_tco`, `is_helpdesk_visible`, `softwarecategories_id`, `is_valid`, `date_creation`, `pictures`) VALUES(2, 0, 0, 'Software2', 'Software2Comment', 1, 0, 0, 1, 1, 0, 0, 0, NULL, '2023-03-19 19:21:10', 0, 0, '0.0000', 1, 1, 1, '2023-03-19 19:21:10', NULL);

--
-- Volcado de datos para la tabla `glpi_ssovariables`
--

REPLACE INTO `glpi_ssovariables` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(1, 'HTTP_AUTH_USER', NULL, NULL, NULL);
REPLACE INTO `glpi_ssovariables` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(2, 'REMOTE_USER', NULL, NULL, NULL);
REPLACE INTO `glpi_ssovariables` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(3, 'PHP_AUTH_USER', NULL, NULL, NULL);
REPLACE INTO `glpi_ssovariables` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(4, 'USERNAME', NULL, NULL, NULL);
REPLACE INTO `glpi_ssovariables` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(5, 'REDIRECT_REMOTE_USER', NULL, NULL, NULL);
REPLACE INTO `glpi_ssovariables` (`id`, `name`, `comment`, `date_mod`, `date_creation`) VALUES(6, 'HTTP_REMOTE_USER', NULL, NULL, NULL);

--
-- Volcado de datos para la tabla `glpi_states`
--

REPLACE INTO `glpi_states` (`id`, `name`, `entities_id`, `is_recursive`, `comment`, `states_id`, `completename`, `level`, `ancestors_cache`, `sons_cache`, `is_visible_computer`, `is_visible_monitor`, `is_visible_networkequipment`, `is_visible_peripheral`, `is_visible_phone`, `is_visible_printer`, `is_visible_softwareversion`, `is_visible_softwarelicense`, `is_visible_line`, `is_visible_certificate`, `is_visible_rack`, `is_visible_passivedcequipment`, `is_visible_enclosure`, `is_visible_pdu`, `is_visible_cluster`, `is_visible_contract`, `is_visible_appliance`, `is_visible_databaseinstance`, `is_visible_cable`, `date_mod`, `date_creation`) VALUES(1, 'Live', 0, 0, '', 0, 'Live', 1, '[]', NULL, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, '2023-03-19 19:15:09', '2023-03-19 19:15:09');
REPLACE INTO `glpi_states` (`id`, `name`, `entities_id`, `is_recursive`, `comment`, `states_id`, `completename`, `level`, `ancestors_cache`, `sons_cache`, `is_visible_computer`, `is_visible_monitor`, `is_visible_networkequipment`, `is_visible_peripheral`, `is_visible_phone`, `is_visible_printer`, `is_visible_softwareversion`, `is_visible_softwarelicense`, `is_visible_line`, `is_visible_certificate`, `is_visible_rack`, `is_visible_passivedcequipment`, `is_visible_enclosure`, `is_visible_pdu`, `is_visible_cluster`, `is_visible_contract`, `is_visible_appliance`, `is_visible_databaseinstance`, `is_visible_cable`, `date_mod`, `date_creation`) VALUES(2, 'Down', 0, 0, '', 0, 'Down', 1, '[]', NULL, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, '2023-03-19 19:15:14', '2023-03-19 19:15:14');

--
-- Volcado de datos para la tabla `glpi_tickettemplatemandatoryfields`
--

REPLACE INTO `glpi_tickettemplatemandatoryfields` (`id`, `tickettemplates_id`, `num`) VALUES(1, 1, 21);

--
-- Volcado de datos para la tabla `glpi_tickettemplates`
--

REPLACE INTO `glpi_tickettemplates` (`id`, `name`, `entities_id`, `is_recursive`, `comment`) VALUES(1, 'Default', 0, 1, NULL);

--
-- Volcado de datos para la tabla `glpi_transfers`
--

REPLACE INTO `glpi_transfers` (`id`, `name`, `keep_ticket`, `keep_networklink`, `keep_reservation`, `keep_history`, `keep_device`, `keep_infocom`, `keep_dc_monitor`, `clean_dc_monitor`, `keep_dc_phone`, `clean_dc_phone`, `keep_dc_peripheral`, `clean_dc_peripheral`, `keep_dc_printer`, `clean_dc_printer`, `keep_supplier`, `clean_supplier`, `keep_contact`, `clean_contact`, `keep_contract`, `clean_contract`, `keep_software`, `clean_software`, `keep_document`, `clean_document`, `keep_cartridgeitem`, `clean_cartridgeitem`, `keep_cartridge`, `keep_consumable`, `date_mod`, `date_creation`, `comment`, `keep_disk`, `keep_certificate`, `clean_certificate`, `lock_updated_fields`) VALUES(1, 'complete', 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, NULL, 1, 1, 1, 0);

--
-- Volcado de datos para la tabla `glpi_users`
--

REPLACE INTO `glpi_users` (`id`, `name`, `password`, `password_last_update`, `phone`, `phone2`, `mobile`, `realname`, `firstname`, `locations_id`, `language`, `use_mode`, `list_limit`, `is_active`, `comment`, `auths_id`, `authtype`, `last_login`, `date_mod`, `date_sync`, `is_deleted`, `profiles_id`, `entities_id`, `usertitles_id`, `usercategories_id`, `date_format`, `number_format`, `names_format`, `csv_delimiter`, `is_ids_visible`, `use_flat_dropdowntree`, `show_jobs_at_login`, `priority_1`, `priority_2`, `priority_3`, `priority_4`, `priority_5`, `priority_6`, `followup_private`, `task_private`, `default_requesttypes_id`, `password_forget_token`, `password_forget_token_date`, `user_dn`, `registration_number`, `show_count_on_tabs`, `refresh_views`, `set_default_tech`, `personal_token`, `personal_token_date`, `api_token`, `api_token_date`, `cookie_token`, `cookie_token_date`, `display_count_on_home`, `notification_to_myself`, `duedateok_color`, `duedatewarning_color`, `duedatecritical_color`, `duedatewarning_less`, `duedatecritical_less`, `duedatewarning_unit`, `duedatecritical_unit`, `display_options`, `is_deleted_ldap`, `pdffont`, `picture`, `begin_date`, `end_date`, `keep_devices_when_purging_item`, `privatebookmarkorder`, `backcreated`, `task_state`, `palette`, `page_layout`, `fold_menu`, `fold_search`, `savedsearches_pinned`, `timeline_order`, `itil_layout`, `richtext_layout`, `set_default_requester`, `lock_autolock_mode`, `lock_directunlock_notification`, `date_creation`, `highcontrast_css`, `plannings`, `sync_field`, `groups_id`, `users_id_supervisor`, `timezone`, `default_dashboard_central`, `default_dashboard_assets`, `default_dashboard_helpdesk`, `default_dashboard_mini_ticket`, `default_central_tab`, `nickname`, `timeline_action_btn_layout`, `timeline_date_format`) VALUES(2, 'glpi', '$2y$10$rXXzbc2ShaiCldwkw4AZL.n.9QSH7c0c9XJAyyjrbL9BwmWditAYm', NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, 0, 20, 1, NULL, 0, 1, '2023-03-19 19:12:54', '2023-03-19 19:12:54', NULL, 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '$2y$10$MUQx3pD1pgfqlgSgkRM0HeriJgzOGBc3oVi40AmRlDHNIVZ8qKzxq', '2023-03-19 19:12:54', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
REPLACE INTO `glpi_users` (`id`, `name`, `password`, `password_last_update`, `phone`, `phone2`, `mobile`, `realname`, `firstname`, `locations_id`, `language`, `use_mode`, `list_limit`, `is_active`, `comment`, `auths_id`, `authtype`, `last_login`, `date_mod`, `date_sync`, `is_deleted`, `profiles_id`, `entities_id`, `usertitles_id`, `usercategories_id`, `date_format`, `number_format`, `names_format`, `csv_delimiter`, `is_ids_visible`, `use_flat_dropdowntree`, `show_jobs_at_login`, `priority_1`, `priority_2`, `priority_3`, `priority_4`, `priority_5`, `priority_6`, `followup_private`, `task_private`, `default_requesttypes_id`, `password_forget_token`, `password_forget_token_date`, `user_dn`, `registration_number`, `show_count_on_tabs`, `refresh_views`, `set_default_tech`, `personal_token`, `personal_token_date`, `api_token`, `api_token_date`, `cookie_token`, `cookie_token_date`, `display_count_on_home`, `notification_to_myself`, `duedateok_color`, `duedatewarning_color`, `duedatecritical_color`, `duedatewarning_less`, `duedatecritical_less`, `duedatewarning_unit`, `duedatecritical_unit`, `display_options`, `is_deleted_ldap`, `pdffont`, `picture`, `begin_date`, `end_date`, `keep_devices_when_purging_item`, `privatebookmarkorder`, `backcreated`, `task_state`, `palette`, `page_layout`, `fold_menu`, `fold_search`, `savedsearches_pinned`, `timeline_order`, `itil_layout`, `richtext_layout`, `set_default_requester`, `lock_autolock_mode`, `lock_directunlock_notification`, `date_creation`, `highcontrast_css`, `plannings`, `sync_field`, `groups_id`, `users_id_supervisor`, `timezone`, `default_dashboard_central`, `default_dashboard_assets`, `default_dashboard_helpdesk`, `default_dashboard_mini_ticket`, `default_central_tab`, `nickname`, `timeline_action_btn_layout`, `timeline_date_format`) VALUES(3, 'post-only', '$2y$10$dTMar1F3ef5X/H1IjX9gYOjQWBR1K4bERGf4/oTPxFtJE/c3vXILm', NULL, NULL, NULL, NULL, NULL, NULL, 0, 'en_GB', 0, 20, 1, NULL, 0, 1, NULL, NULL, NULL, 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, 0, 0);
REPLACE INTO `glpi_users` (`id`, `name`, `password`, `password_last_update`, `phone`, `phone2`, `mobile`, `realname`, `firstname`, `locations_id`, `language`, `use_mode`, `list_limit`, `is_active`, `comment`, `auths_id`, `authtype`, `last_login`, `date_mod`, `date_sync`, `is_deleted`, `profiles_id`, `entities_id`, `usertitles_id`, `usercategories_id`, `date_format`, `number_format`, `names_format`, `csv_delimiter`, `is_ids_visible`, `use_flat_dropdowntree`, `show_jobs_at_login`, `priority_1`, `priority_2`, `priority_3`, `priority_4`, `priority_5`, `priority_6`, `followup_private`, `task_private`, `default_requesttypes_id`, `password_forget_token`, `password_forget_token_date`, `user_dn`, `registration_number`, `show_count_on_tabs`, `refresh_views`, `set_default_tech`, `personal_token`, `personal_token_date`, `api_token`, `api_token_date`, `cookie_token`, `cookie_token_date`, `display_count_on_home`, `notification_to_myself`, `duedateok_color`, `duedatewarning_color`, `duedatecritical_color`, `duedatewarning_less`, `duedatecritical_less`, `duedatewarning_unit`, `duedatecritical_unit`, `display_options`, `is_deleted_ldap`, `pdffont`, `picture`, `begin_date`, `end_date`, `keep_devices_when_purging_item`, `privatebookmarkorder`, `backcreated`, `task_state`, `palette`, `page_layout`, `fold_menu`, `fold_search`, `savedsearches_pinned`, `timeline_order`, `itil_layout`, `richtext_layout`, `set_default_requester`, `lock_autolock_mode`, `lock_directunlock_notification`, `date_creation`, `highcontrast_css`, `plannings`, `sync_field`, `groups_id`, `users_id_supervisor`, `timezone`, `default_dashboard_central`, `default_dashboard_assets`, `default_dashboard_helpdesk`, `default_dashboard_mini_ticket`, `default_central_tab`, `nickname`, `timeline_action_btn_layout`, `timeline_date_format`) VALUES(4, 'tech', '$2y$10$.xEgErizkp6Az0z.DHyoeOoenuh0RcsX4JapBk2JMD6VI17KtB1lO', NULL, NULL, NULL, NULL, NULL, NULL, 0, 'en_GB', 0, 20, 1, NULL, 0, 1, NULL, NULL, NULL, 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, 0, 0);
REPLACE INTO `glpi_users` (`id`, `name`, `password`, `password_last_update`, `phone`, `phone2`, `mobile`, `realname`, `firstname`, `locations_id`, `language`, `use_mode`, `list_limit`, `is_active`, `comment`, `auths_id`, `authtype`, `last_login`, `date_mod`, `date_sync`, `is_deleted`, `profiles_id`, `entities_id`, `usertitles_id`, `usercategories_id`, `date_format`, `number_format`, `names_format`, `csv_delimiter`, `is_ids_visible`, `use_flat_dropdowntree`, `show_jobs_at_login`, `priority_1`, `priority_2`, `priority_3`, `priority_4`, `priority_5`, `priority_6`, `followup_private`, `task_private`, `default_requesttypes_id`, `password_forget_token`, `password_forget_token_date`, `user_dn`, `registration_number`, `show_count_on_tabs`, `refresh_views`, `set_default_tech`, `personal_token`, `personal_token_date`, `api_token`, `api_token_date`, `cookie_token`, `cookie_token_date`, `display_count_on_home`, `notification_to_myself`, `duedateok_color`, `duedatewarning_color`, `duedatecritical_color`, `duedatewarning_less`, `duedatecritical_less`, `duedatewarning_unit`, `duedatecritical_unit`, `display_options`, `is_deleted_ldap`, `pdffont`, `picture`, `begin_date`, `end_date`, `keep_devices_when_purging_item`, `privatebookmarkorder`, `backcreated`, `task_state`, `palette`, `page_layout`, `fold_menu`, `fold_search`, `savedsearches_pinned`, `timeline_order`, `itil_layout`, `richtext_layout`, `set_default_requester`, `lock_autolock_mode`, `lock_directunlock_notification`, `date_creation`, `highcontrast_css`, `plannings`, `sync_field`, `groups_id`, `users_id_supervisor`, `timezone`, `default_dashboard_central`, `default_dashboard_assets`, `default_dashboard_helpdesk`, `default_dashboard_mini_ticket`, `default_central_tab`, `nickname`, `timeline_action_btn_layout`, `timeline_date_format`) VALUES(5, 'normal', '$2y$10$Z6doq4zVHkSPZFbPeXTCluN1Q/r0ryZ3ZsSJncJqkN3.8cRiN0NV.', NULL, NULL, NULL, NULL, NULL, NULL, 0, 'en_GB', 0, 20, 1, NULL, 0, 1, NULL, NULL, NULL, 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, 0, 0);
REPLACE INTO `glpi_users` (`id`, `name`, `password`, `password_last_update`, `phone`, `phone2`, `mobile`, `realname`, `firstname`, `locations_id`, `language`, `use_mode`, `list_limit`, `is_active`, `comment`, `auths_id`, `authtype`, `last_login`, `date_mod`, `date_sync`, `is_deleted`, `profiles_id`, `entities_id`, `usertitles_id`, `usercategories_id`, `date_format`, `number_format`, `names_format`, `csv_delimiter`, `is_ids_visible`, `use_flat_dropdowntree`, `show_jobs_at_login`, `priority_1`, `priority_2`, `priority_3`, `priority_4`, `priority_5`, `priority_6`, `followup_private`, `task_private`, `default_requesttypes_id`, `password_forget_token`, `password_forget_token_date`, `user_dn`, `registration_number`, `show_count_on_tabs`, `refresh_views`, `set_default_tech`, `personal_token`, `personal_token_date`, `api_token`, `api_token_date`, `cookie_token`, `cookie_token_date`, `display_count_on_home`, `notification_to_myself`, `duedateok_color`, `duedatewarning_color`, `duedatecritical_color`, `duedatewarning_less`, `duedatecritical_less`, `duedatewarning_unit`, `duedatecritical_unit`, `display_options`, `is_deleted_ldap`, `pdffont`, `picture`, `begin_date`, `end_date`, `keep_devices_when_purging_item`, `privatebookmarkorder`, `backcreated`, `task_state`, `palette`, `page_layout`, `fold_menu`, `fold_search`, `savedsearches_pinned`, `timeline_order`, `itil_layout`, `richtext_layout`, `set_default_requester`, `lock_autolock_mode`, `lock_directunlock_notification`, `date_creation`, `highcontrast_css`, `plannings`, `sync_field`, `groups_id`, `users_id_supervisor`, `timezone`, `default_dashboard_central`, `default_dashboard_assets`, `default_dashboard_helpdesk`, `default_dashboard_mini_ticket`, `default_central_tab`, `nickname`, `timeline_action_btn_layout`, `timeline_date_format`) VALUES(6, 'glpi-system', '', NULL, NULL, NULL, NULL, 'Support', NULL, 0, NULL, 0, NULL, 1, NULL, 0, 1, NULL, NULL, NULL, 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, 0, NULL, 0, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
