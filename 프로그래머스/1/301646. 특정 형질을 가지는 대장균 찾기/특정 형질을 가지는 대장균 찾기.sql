SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE BIN(GENOTYPE) & 5 AND !(BIN(GENOTYPE) & 2)