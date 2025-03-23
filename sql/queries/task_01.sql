SELECT
    campaign_id , COUNT(*)
FROM
    marketing_email_sent
GROUP BY
    campaign_id