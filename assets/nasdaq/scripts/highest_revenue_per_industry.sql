-- you can chain multiple common table expressions using a comma
WITH a AS (
    SELECT companyid, 
    industryid AS cindustryid, 
    parentcompanyid, 
    name AS companyname,
    annualrevenue
    FROM companies
),

b AS (
    SELECT industryid,
    name AS iname
    FROM industries
)

SELECT companyname, MAX(annualrevenue) AS HighestRevenue FROM a
LEFT JOIN b
ON a.cindustryid = b.industryid
GROUP BY iname;