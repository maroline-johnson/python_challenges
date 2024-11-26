def add_product_code(product_code, product_id):
    if product_id[3] == "-":
        return product_id
    else:
        return f"{product_id[:3]}-{product_code}-{product_id[3:]}"
    
product_code1 = "09283"
product_id1 = "COMLAP-BLK-3GHZ-8GB-1TB"

product_code2 = "36629"
product_id2 = "KIT-36629-CHR-RED-2S-PLAS"

print(add_product_code(product_code1, product_id1))
print(add_product_code(product_code2, product_id2))