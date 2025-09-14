price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {round(base, 2)} ₽', f'НДC: {round(vat_amount, 2)} ₽', f'Итого к оплате: {round(total, 2)} ₽', sep='\n')