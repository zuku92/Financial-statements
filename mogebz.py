                                                # ფინანსური უწყისები
# ანუიტეტი
print("მოთხოვნილი სესხის თანხა:")
vada = int(input('ვადა:'))
procenti = int(input('პროცენტი'))
tanxa = int(input('თანხა:'))
procenti=(procenti*0.57)
jami=(tanxa*procenti/100)+tanxa
shenatani=jami/vada
print(f'შენატანი უდრის {round(shenatani)}')

# ბალანსი
print("ბალანსი")
print("ლიკვიდური/მოკლევადიანი აქტივები")

cash = float(input("ნაღდი თანხა/სალარო"))
maragebi = float(input("მარაგები/ნედლეული"))
cash_transit = float(input("თანხა გზაში"))
bank_count =float(input("საბანკო ანგარიში"))

sum_of_lic_active = cash+maragebi+cash_transit+bank_count
print("მოკლევადიანი აქტივები",  sum_of_lic_active)


print("გრძელვადიანი აქტივები:")

debit= float(input("დებიტორები/ნისია"))
inventors =float(input("ინვენტარი"))
furniture =float(input("ავეჯი/დახლები-თაროები"))
teqnic = float(input("ტექნიკა/მანქანა-დანადგარები"))
ground =float(input("უძრავი ქონება"))

sum_of_main_active = debit+inventors+furniture+teqnic+ground
print("გრძელვადიანი აქტივები",  sum_of_main_active)

all_active = sum_of_main_active+sum_of_lic_active
print("სულ აქტივები:", all_active)



print("პასივები/ვალდებულებები")
debit_of_country = float(input("საგადასახადო ვალდებულება"))
short_credit_of_bank = float(input("მოკლევადიანი საბანკო ვალდებულება"))
large_credit_of_bank = float(input("გრძელვადიანი საბანკო ვალდებულება"))

sum_of_pacciv = debit_of_country+short_credit_of_bank+large_credit_of_bank
print("სულ პასივები/ვალდებულებები", sum_of_pacciv)

capital = all_active-sum_of_pacciv
print("საკუთარი კაპიტალი", capital)

if capital<tanxa:


    print("აღნიშნული თანხა ვერ გაიცემა,რადგან საკუთარი კაპიტალი ნაკლებია მოთხოვნილ თანხაზე..!")


else:


    # მოგება-ზარალი
    print("მოგება-ზარალი")
    shemosavali = float(input("შემოსავალი:"))
    fasnamati = float (input("ფასნამატი:"))
    temp_fasnamati = fasnamati/100
    temp_fasnamati+= 1
    tvitgirebuleba = (shemosavali/temp_fasnamati)
    print("თვითღირებულება:")
    print(tvitgirebuleba)
    mogeba = shemosavali - tvitgirebuleba
    print("მოგება:")
    print(mogeba)

    print("ხარჯები:")
    komunaluri = float(input("კომუნალური:"))
    transportireba = float(input("ტრანსპორტირება:"))
    ijara = float(input("იჯარა:"))
    xelfasebi= float(input("ხელფასები:"))
    sagadasaxado = float(input("საგადასახადო:"))
    sxvaxarji= float(input("სხვახარჯი:"))
    dividendebi = float(input("დივიდენდი:"))

    wmmindamogeba = mogeba-komunaluri-transportireba-ijara-xelfasebi-sagadasaxado-sxvaxarji-dividendebi
    print("წმინდა მოგება:")
    print(wmmindamogeba)

    # PTI კოეფიციენტი
    PTI=0
    if wmmindamogeba<=1000:
        PTI=(wmmindamogeba*25)/100
        if shenatani<=PTI:
            print("PTI კოეფიციენტი  აკმაყოფილებს აღნიშნულ პირობებს")
        else:
            print("PTI კოეფიციენტი არ აკმაყოფილებს აღნიშნულ პირობებს, გაზარდეთ ვადა ან შეამცირეთ თანხა..!")


    else:
        PTI=(wmmindamogeba*35)/100
        if shenatani<=PTI:
            print("PTI კოეფიციენტი  აკმაყოფილებს აღნიშნულ პირობებს")
        else:
            print("PTI კოეფიციენტი არ აკმაყოფილებს აღნიშნულ პირობებს, გაზარდეთ ვადა ან შეამცირეთ თანხა..!")





    # სესხის მომსახურების კოეფიციენტი DSCR / ITP
    DSCR = wmmindamogeba / shenatani

    if DSCR <=1:
        print("სესხის მოსახურების კოეფიციენტი არ აკმაყოფილებს მოთხოვნილ თანხას! DSCR/ITP ->", DSCR)
    else:
        print("სესხის მოსახურების კოეფიციენტი აკმაყოფილებს მოთხოვნილ თანხას DSCR/ITP->", DSCR)





