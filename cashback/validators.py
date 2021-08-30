from validate_docbr import CPF

def validate_cpf(value):
    cpf = CPF()
    return cpf.validate(value)

def validate_amount(value):
    
    products = value['products']
    amount = value['amount']
    
    total = 0
    for product in products:
        price = product['price']
        quantity = product['quantity']
        total += float(price) * quantity
    
    return float(amount) == total