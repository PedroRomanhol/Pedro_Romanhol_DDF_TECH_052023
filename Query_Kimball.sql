SELECT 
    dc.categoria_label,
    COUNT(fp.produto_id) AS total_produtos
FROM 
    fato_produto_categoria fp
JOIN 
    dim_categoria dc ON fp.categoria_id = dc.categoria_id
GROUP BY 
    dc.categoria_label
ORDER BY 
    total_produtos DESC;

	SELECT 
    dp.produto_id,
    dp.titulo,
    dp.descricao,
    dc.categoria_label
FROM 
    fato_produto_categoria fp
JOIN 
    dim_produto dp ON fp.produto_id = dp.produto_id
JOIN 
    dim_categoria dc ON fp.categoria_id = dc.categoria_id;