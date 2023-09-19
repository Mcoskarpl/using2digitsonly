wynik = []
for X in range (0,10):
    for Y in range (0,10):
        ok_digits = [X,Y]
        plus = X+Y
        minus = abs(X-Y)
        razy = X*Y
        pot1 = X**Y
        pot2 = Y**X
        
                
        tablica = [int(digit) for digit in str(pot2)]
        if X in tablica and Y in tablica:
            if not Y**X in wynik:
                wynik.append(Y**X)
                print (f"{Y}^{X}=",Y**X)
        
        tablica = [int(digit) for digit in str(plus)]
        if X in tablica and Y in tablica:
            if not Y+X in wynik:
                wynik.append(Y+X)
                print (f"{X}+{Y}=",X+Y)
                
        tablica = [int(digit) for digit in str(minus)]
        if X in tablica and Y in tablica:
            if not abs(X-Y) in wynik:
                wynik.append(abs(X-Y))
                print (f"|{X}-{Y}|=",abs(X-Y))
                
        tablica = [int(digit) for digit in str(razy)]
        if X in tablica and Y in tablica:
            if not X*Y in wynik:
                wynik.append(X*Y)
                print (f"{X}*{Y}=",X*Y)
                
        tablica = [int(digit) for digit in str(pot1)]
        if X in tablica and Y in tablica:
            if not X**Y in wynik:
                wynik.append(X**Y)
                print (f"{X}^{Y}=",X**Y)
                
sort = sorted(wynik)

print("Sorted list:", sort)