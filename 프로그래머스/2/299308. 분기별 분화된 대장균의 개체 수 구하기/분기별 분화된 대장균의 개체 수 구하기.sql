SELECT
    CASE
        WHEN QUARTER(DIFFERENTIATION_DATE) = 1 THEN '1Q'
        WHEN QUARTER(DIFFERENTIATION_DATE) = 2 THEN '2Q'
        WHEN QUARTER(DIFFERENTIATION_DATE) = 3 THEN '3Q'
        WHEN QUARTER(DIFFERENTIATION_DATE) = 4 THEN '4Q'
    END AS QUARTER, COUNT(*) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER