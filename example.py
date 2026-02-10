from orchestrator import AIConsultantOrchestrator
import sys


def run_example():
    print("\n" + "="*60)
    print("  Example: AI Strategic Consultant System Demo")
    print("  مثال: نظام المستشار الاستراتيجي بالذكاء الاصطناعي")
    print("="*60 + "\n")
    
    business_ideas = [
        {
            "name": "مشروع توصيل المخبوزات",
            "idea": """
منصة توصيل مخبوزات محلية يومية عبر الاشتراكات الشهرية في الرياض.
الفكرة: ربط المخابز الصغيرة بالعملاء، مع ضمان جودة وطازجية يومية.
السعر: 200 ريال شهرياً للاشتراك اليومي.
            """
        },
        {
            "name": "تطبيق تعليم البرمجة للأطفال",
            "idea": """
تطبيق تفاعلي لتعليم البرمجة للأطفال من 8-14 سنة باللغة العربية.
الفكرة: استخدام الألعاب والتحديات لتعليم مفاهيم البرمجة الأساسية.
نموذج الإيرادات: اشتراك شهري 50 ريال، مع محتوى مجاني محدود.
            """
        }
    ]
    
    try:
        orchestrator = AIConsultantOrchestrator()
        
        for idx, business in enumerate(business_ideas, 1):
            print(f"\n{'='*60}")
            print(f"  مثال {idx}: {business['name']}")
            print(f"  Example {idx}: {business['name']}")
            print(f"{'='*60}\n")
            
            result = orchestrator.analyze(business['idea'])
            
            print(f"\n\n{'='*60}")
            print(f"  انتهى تحليل المثال {idx}")
            print(f"{'='*60}\n")
            
            input("اضغط Enter للمتابعة للمثال التالي...")
    
    except Exception as e:
        print(f"\n[ERROR] حدث خطأ: {str(e)}")
        print("\nتأكد من:")
        print("1. وجود ملف .env يحتوي على OPENAI_API_KEY")
        print("2. تثبيت جميع المكتبات المطلوبة: pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    run_example()
