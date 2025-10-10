CREATE TABLE `companies` (
  `companyid` int NOT NULL,
  `industryid` int NOT NULL,
  `parentindustryid` int DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `annualrevenue` int DEFAULT NULL,
  PRIMARY KEY (`companyid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci