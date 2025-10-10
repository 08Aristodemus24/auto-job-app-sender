-- companies which do not have same industry as parent company
-- what we need to do first is to 

-- joins the child company table with the the parent 
-- company table on the parentCompanyId of child
-- and the companyId of the parent company table
-- di pwede C.companyId = P.parentCompanyId kasi the
-- childs companyId will have to defer to parent companys
-- companyId which will be non existent e.g. 117 is the child company
-- and its parent company is 116, so C.parentCompanyId = P.companyId
-- doesn't work because 116 = 
WITH CPCompany AS (
  SELECT 
    C.*,
    -- include also the industryId
    P.industryId AS parentIndustryId,
    P.name AS parentName
  FROM Company C
  LEFT JOIN Company P
  ON C.parentCompanyId = P.companyId
  -- ORDER BY C.industryId
)

-- after this we now have to join the industry id of the
-- parent company
SELECT * FROM CPCompany
WHERE parentCompanyId IS NOT NULL AND industryId != parentIndustryId