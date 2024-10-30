def calculate_total_credits(kurs):
    total_credits = 0
    for object in kurs:
        total_credits += object.credits
    return total_credits
