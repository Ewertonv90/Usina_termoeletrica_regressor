# Usina_termoeletrica_regressor
Projeto de Data science usando regressão para prever a saída de energia elétrica horária líquida (MWh).

Combined cycle power plant
O dataset contém 9568 registros coletados de uma usina termelétrica de ciclo combinado ao longo de 6 anos (2006-2011). É composto pelas seguintes variáveis médias horárias: Temperatura (T), Pressão Ambiente (AP), Umidade Relativa (RH) e Vácuo de Exaustão (V); usadas para prever a saída de energia elétrica horária líquida (EP) da planta. Uma usina termelétrica de ciclo combinado combina o uso de dois sistemas de turbina, uma turbina a gás que queima combustível para gerar eletricidade e uma turbina a vapor que produz eletricidade adicional usando o vapor obtido do calor de exaustão da turbina a gás. O calor de exaustão da turbina a gás é convertido em vapor, que é canalizado para a turbina a vapor para geração adicional de energia elétrica.

Objetivo: prever a saída de energia elétrica horária líquida (MW) a partir das variáveis de entrada.


Descrição das variáveis:

Temperatura (AT) na faixa de 1,81 ° C e 37,11 ° C;
Pressão ambiente (AP) na faixa de 992,89-1033,30 milibar;
Umidade relativa (RH) na faixa de 25,56% a 100,16%;
Vácuo de exaustão (V) na faixa de 25,36-81,56 cm Hg
Produção horária líquida de energia elétrica (PE) 420,26-495,76 MW. As médias foram tiradas de vários sensores localizados ao redor da planta que registram as variáveis ambientais a cada segundo. As variáveis são fornecidas sem normalização.