from statistics import mean

nMeses = 30
pInflacionMen = 0.03
ps_T_Interes = []

for nMes in range(1, nMeses + 1):
    pT_Interes = round((1 - pInflacionMen) ** nMes, 2)
    ps_T_Interes.append(pT_Interes)

    print("nMes =", nMes, ", pT_Interes =", pT_Interes)

pMed_P_T_Interes = mean(ps_T_Interes)

print("\npMed_P_T_Interes =", round(pMed_P_T_Interes, 2),\
      ", estas ahorrando un", round(1 - pMed_P_T_Interes, 2))
