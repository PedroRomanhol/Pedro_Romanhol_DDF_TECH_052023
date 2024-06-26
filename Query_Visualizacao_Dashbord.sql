--Gr�f de pizza para categorias
SELECT "PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" AS "_C4", COUNT(*) AS "count"
FROM "DADOSFERA_PRD_TREINAMENTOS"."PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"
WHERE ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Food')
    OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Electronics') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Books') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Toys and Games') 
	OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Decoration') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Womens Fashion') OR 
	("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Mens Fashion') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Beleza') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Office')
GROUP BY "PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4"
ORDER BY "PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" ASC

--Gr�f de pizza para categorias (Numerico)
SELECT "PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" AS "_C3", COUNT(*) AS "count"
FROM "DADOSFERA_PRD_TREINAMENTOS"."PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"
WHERE ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" = '0')
    OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" = '1') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" = '2') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" = '3') OR 
	("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" = '4') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" = '5') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" = '6') OR 
	("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" = '7') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" = '8')
GROUP BY "PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3"
ORDER BY "PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3" ASC

--Gr�f de barras para categorias
SELECT "source"."_C4" AS "_C4", "source"."count" AS "count"
FROM (SELECT "PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" AS "_C4", COUNT(*) AS "count" FROM "DADOSFERA_PRD_TREINAMENTOS"."PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"
WHERE ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Food')
    OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Electronics') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Books') OR 
	("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Toys and Games') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Decoration') OR 
	("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Womens Fashion') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Mens Fashion') OR 
	("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Beleza') OR ("PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" = 'Office')
GROUP BY "PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4"
ORDER BY "PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C4" ASC) AS "source"
LIMIT 1048575

--Valores Distintos
SELECT count(distinct "PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"."_C3") AS "count"
FROM "DADOSFERA_PRD_TREINAMENTOS"."PUBLIC"."TB__HW7CAI__CORPUS_CATEGORY_PEDRO"