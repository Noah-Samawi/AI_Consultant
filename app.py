import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from dotenv import load_dotenv
from openai import OpenAI
from dataclasses import asdict

# استيراد الوكلاء من مجلد agents
try:
    from agents import (
        MarketLogicAgent,
        FinancialSustainabilityAgent,
        CompetitiveDurabilityAgent,
        StrategicSynthesizerAgent,
    )
except ImportError as e:
    print(f"خطأ في استيراد الوكلاء: {e}")
    print("تأكد من وجود مجلد agents وبداخله ملفات الوكلاء.")

# إعداد المسارات المطلقة لضمان عمل templates و static على الماك
current_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, 
            static_folder=os.path.join(current_dir, 'static'), 
            template_folder=os.path.join(current_dir, 'templates'))

# تحميل مفتاح API من ملف .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# تهيئة الوكلاء باستخدام عميل OpenAI
market_agent = MarketLogicAgent(client)
financial_agent = FinancialSustainabilityAgent(client)
competitive_agent = CompetitiveDurabilityAgent(client)
synthesizer = StrategicSynthesizerAgent(client)

@app.route('/')
def index():
    """فتح الصفحة الرئيسية من مجلد templates"""
    return render_template('index.html')

@app.route('/manifest.json')
def serve_manifest():
    """تقديم ملف المانيفست للـ PWA"""
    return send_from_directory(app.static_folder, 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    """تقديم ملف الـ Service Worker"""
    return send_from_directory(app.static_folder, 'sw.js')

@app.route('/analyze', methods=['POST'])
def analyze():
    """استقبال فكرة المشروع وتحليلها عبر الوكلاء"""
    data = request.json
    business_idea = data.get('idea')
    
    if not business_idea:
        return jsonify({"status": "error", "message": "لم يتم تقديم فكرة مشروع"}), 400

    try:
        # المرحلة 1: التحليل بواسطة الوكلاء الثلاثة
        market_analysis = market_agent.analyze(business_idea)
        financial_analysis = financial_agent.analyze(business_idea)
        competitive_analysis = competitive_agent.analyze(business_idea)
        
        # المرحلة 2: التركيب النهائي (Synthesis) للمذكرة الاستراتيجية
        strategic_memo = synthesizer.synthesize(
            business_idea,
            market_analysis,
            financial_analysis,
            competitive_analysis
        )
        
        # إرجاع النتائج بتنسيق JSON للواجهة الفاخرة
        return jsonify({
            "status": "success",
            "market_analysis": asdict(market_analysis),
            "financial_analysis": asdict(financial_analysis),
            "competitive_analysis": asdict(competitive_analysis),
            "strategic_memo": asdict(strategic_memo)
        })

    except Exception as e:
        print(f"حدث خطأ أثناء التحليل: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # طباعة مسار البحث للتأكد عند التشغيل
    print(f"Looking for templates in: {app.template_folder}")
    app.run(debug=True, port=5000)