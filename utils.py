import random

def generate_question():
    questions = [
        {"question": "If elasticity > 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Elastic"},
        {"question": "If elasticity < 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Inelastic"},
        {"question": "If elasticity = 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Unit Elastic"}
    ]
    return random.choice(questions)

def calculate_equilibrium(a, b, c, d):
    eq_price = (a - c) / (b + d)
    eq_quantity = a - b * eq_price
    return eq_price, eq_quantity
