def percentual(valor, total):
    return valor/total

def valor_representado():
    sp = 67836.43
    rj = 36678.66
    mg = 29229.88
    es = 27165.48
    outros = 19849.53

    total = sp+rj+mg+es+outros

    print(f"A contribuição do estado de SP foi de: {percentual(sp,total)*100:.2f}%")
    print(f"A contribuição do estado de RJ foi de: {percentual(rj,total)*100:.2f}%")
    print(f"A contribuição do estado de MG foi de: {percentual(mg,total)*100:.2f}%")
    print(f"A contribuição do estado de ES foi de: {percentual(es,total)*100:.2f}%")
    print(f"A contribuição de outros estados foi de: {percentual(outros,total)*100:.2f}%")

valor_representado()