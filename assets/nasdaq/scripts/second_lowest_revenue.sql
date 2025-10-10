WITH rankedrevenue AS (
    SELECT companyid, 
    industryid, 
    parentcompanyid, 
    name AS companyname,
    annualrevenue,
    -- places ascending numbers from 1 to n according to annualrevenue
    DENSE_RANK() OVER (ORDER BY annualrevenue) AS revenuerank
    FROM companies
)

SELECT companyid, industryid, parentcompanyid, companyname, annualrevenue, revenuerank
FROM rankedrevenue
WHERE revenuerank = 2;