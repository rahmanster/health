def bmi(weight, height):
    w_in_kg = weight/2.2046
    h_in_m = height*0.0254
    bmi = round((w_in_kg)/((h_in_m)**2),1)
    return bmi

