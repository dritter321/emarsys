-- SQLite does not support INTERVAL
-- SQLite has a DATE and DATETIME for achieving the same functionality
WITH last_six_months AS (
    SELECT *
    FROM marketing_email_sent
    WHERE event_time >= DATETIME('now', '-6 months')
)
SELECT
    DATE(event_time, 'weekday 0') AS week_start,
    COUNT(*) AS entry_count
FROM last_six_months
GROUP BY week_start
ORDER BY week_start;