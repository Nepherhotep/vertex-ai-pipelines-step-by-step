SELECT
  *
FROM
  `my-project.ml.creatures`
WHERE
  created_date >= CURRENT_DATE()
LIMIT
  10000;
