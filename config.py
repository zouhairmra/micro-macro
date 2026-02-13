TEXT = {
    "navigation": {"English": "Navigation", "العربية": "التنقل"},
    "demand_supply": {"English": "Demand & Supply", "العربية": "العرض والطلب"},
    "elasticity": {"English": "Elasticity", "العربية": "المرونة"},
    "quiz": {"English": "Practice Quiz", "العربية": "الاختبار التدريبي"},
    "competition": {"English": "Competition", "العربية": "المسابقة"},
    "teacher_panel": {"English": "Teacher Panel", "العربية": "لوحة المعلم"},
    "chatbot": {"English": "AI Question Bot", "العربية": "بوت الأسئلة الذكي"}  # <-- clé ajoutée
}

def get_text(key, lang="English"):
    return TEXT[key][lang]
