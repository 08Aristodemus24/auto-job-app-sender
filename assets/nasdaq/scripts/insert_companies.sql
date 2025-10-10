INSERT INTO `sys`.`companies`
(`companyid`,
`industryid`,
`parentcompanyid`,
`name`,
`annualrevenue`)
VALUES
(1, 1, NULL, "google", 160000),
(2, 1, 1, "waze", 125000),
(3, 1, 1, "youtube", 603000),
(4, 2, NULL, "fiat", 800000),
(5, 2, 4, "ferrari", 115000),
(6, 2, 4, "fiat", 102300),
(7, 2, 5, "mini ferraro", 150000),
(8, 3, 1, "google wallet", 111100),
(9, 3, NULL, "td bank", 160145),
(10, 3, 4, "lamborghini", 130000);
