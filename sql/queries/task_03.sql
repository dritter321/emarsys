-- Sqlite doesn't support multiple columns in the COUNT(DISTINCT ...)
-- So, we need to concatenate the columns to get the unique values
SELECT
    (COUNT(DISTINCT mo.campaign_id || '-' || mo.user_id) * 100.0) / COUNT(DISTINCT ms.campaign_id || '-' || ms.user_id) AS match_rate_percentage
FROM
    marketing_email_sent ms
LEFT JOIN
    marketing_email_opened mo
ON
    ms.campaign_id = mo.campaign_id
    AND ms.user_id = mo.user_id;