price=float(input('цена, р: '))
discount=float(input('скидка, %: '))
vat=float(input('ндс, %:'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"база после скидки:{base:.2f} р")
print(f"ндс:{vat_amount:.2f} р")
print(f"итого к оплате:{total:.2f} р")