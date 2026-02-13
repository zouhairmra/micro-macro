TEXT = {
    "navigation": {"English": "Navigation", "العربية": "التنقل"},
    "demand_supply": {"English": "Demand & Supply", "العربية": "العرض والطلب"},
    "elasticity": {"English": "Elasticity", "العربية": "المرونة"},
    "quiz": {"English": "Practice Quiz", "العربية": "الاختبار التدريبي"},
    "competition": {"English": "Live Classroom Competition", "العربية": "المسابقة المباشرة"},
    "teacher_panel": {"English": "Teacher Panel", "العربية": "لوحة المعلم"},
    "chatbot": {"English": "AI Question Bot", "العربية": "بوت الأسئلة الذكي"},
    "next_question": {"English": "Next Question", "العربية": "السؤال التالي"},
    "submit_answer": {"English": "Submit Answer", "العربية": "إرسال الإجابة"},
    "choose_answer": {"English": "Choose your answer:", "العربية": "اختر إجابتك:"},
    "correct": {"English": "Correct!", "العربية": "صحيح!"},
    "wrong": {"English": "Wrong!", "العربية": "خطأ!"},
    "correct_answer": {"English": "Correct answer:", "العربية": "الإجابة الصحيحة:"},
    "your_score": {"English": "Your Score", "العربية": "نقاطك"},
    "no_more_questions": {"English": "No more questions!", "العربية": "لا توجد أسئلة متاحة بعد!"},
    "topic": {"English": "Topic", "العربية": "الموضوع"},
    "explanation": {"English": "Explanation", "العربية": "الشرح"},
    "ask_bot": {"English": "Ask the Bot for a Question", "العربية": "اطلب سؤال من البوت"}
}

def get_text(key, lang="English"):
    return TEXT[key][lang]
