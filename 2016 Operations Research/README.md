# 2016 Operations Research #
**(IN3702 - Investigación de Operaciones)**


### Homework 1: Leibniz and Montecarlo Methods to Aproximate PI ###

This Homework consists in creating a program that estimates pi through the Leibniz Formula and through Montecarlo Simulations. 

**Input:** Number of iterations. The user adds the number of iterations to simulate, it requires the input to be a positive number and if it's a float it will consider the input as an int.

**Sample Output:** This example shows a result printed after providing an input of 3 (The more iterations, the more precise the model becomes).

N  | Leibniz | Error | Montecarlo | Error
------------- | -------------| -------------| -------------| -------------
1 	| 4.0 |	 27.323954473516267 |	 4.0 |	 27.323954473516267
2 	| 2.666666666666667 	| 15.117363684322484 	| 4.0	| 27.323954473516267
3 	| 3.466666666666667 	| 10.347427210380772 |	 2.6666666666666665 	| 57.55868184216125

Etapas:
§ 𝑇=1,2,3,4,5,6 v Variable de Estado:
§ 𝑔F = Cantidad de Stock en el mes t v Variable de Decisión:
§ 𝑥F =𝑃𝑟𝑒𝑐𝑖𝑜𝑎𝑓𝑖𝑗𝑎𝑟𝑒𝑛𝑒𝑙𝑚𝑒𝑠𝑡
v Variable Aleatoria:
§ 𝑒F = 𝐸𝑥𝑝𝑜𝑠𝑖𝑐𝑖ó𝑛 𝑒𝑛 𝑒𝑙 𝑚𝑒𝑠 𝑡 § 𝐷F = 𝐷𝑒𝑚𝑎𝑛𝑑𝑎 𝑒𝑛 𝑡
v Recurrencia:
§ 𝑞Fe" =𝑞F −𝑚𝑖𝑛 𝐷F,𝑞F
v Utilidad:
§ 𝑉 F 𝑥 F , 𝑞 F = 𝑥 F 𝑚 𝑖 𝑛 𝑞 F , $k l " ( 𝐸 𝑝 𝑥 F , 𝑒 e = i ) ∗ 𝑃 ( 𝑒 = 𝑖 ) ) −
𝐹 F 𝑥 F 𝑥 F 𝑚 𝑖 𝑛 𝑞 F , $k l " ( 𝐸 𝑝 𝑥 F , 𝑒 e = i ) ∗ 𝑃 ( 𝑒 = 𝑖 ) ) − 𝑔𝑚𝑎𝑥0, $ (𝐸𝑝𝑥,𝑒 e=i)∗𝑃(𝑒=𝑖))−𝑞 +𝑉∗ (𝑞 )
kl" F F Fe"Fe"
∗ 𝐷𝑜𝑛𝑑𝑒 𝑒 = 1 𝑒𝑠 𝑒𝑥𝑝𝑜𝑠𝑖𝑐𝑖ó𝑛 𝐴𝑙𝑡𝑎, 𝑒 = 2 𝑒𝑠 𝑒𝑥𝑝𝑜𝑠𝑖𝑐𝑖ó𝑛 𝑀𝑒𝑑𝑖𝑎 𝑦 𝑒 = 3 𝑒𝑠 𝑒𝑥𝑝𝑜𝑠𝑖𝑐𝑖ó𝑛 𝐵𝑎𝑗𝑎
Donde:
0,1 §𝐹𝑥F = 0,2 0,3
𝑠𝑖 𝑥F = 𝑃" ∨ 𝑃# 𝑠𝑖𝑥F=𝑃$
𝑠𝑖 𝑥F = 𝑃& ∨ 𝑃%
§ 𝑉F∗ = 𝑚𝑎𝑥tu 𝑉(𝑥F,𝑞F)
