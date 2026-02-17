TEXT = {
    "title": {"English": "Economics Classroom Platform", "العربية": "منصة الاقتصاد التعليمية"},
    "navigation": {"English": "Navigation", "العربية": "التنقل"},
    "demand_supply": {"English": "Demand & Supply", "العربية": "العرض والطلب"},
    "elasticity": {"English": "Elasticity", "العربية": "المرونة"},
    "competition": {"English": "Live Classroom Competition", "العربية": "مسابقة الصف المباشرة"},
     
}

def get_text(key, lang="English"):
    return TEXT.get(key, {}).get(lang, key)
