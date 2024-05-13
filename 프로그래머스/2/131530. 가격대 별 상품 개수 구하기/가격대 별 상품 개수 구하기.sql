SELECT LEFT(PRICE / 10000, 1) * 10000 AS PRICE_GROUP,
COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY LEFT(PRICE / 10000, 1)
ORDER BY LEFT(PRICE / 10000, 1)