from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class FinancialAnalysis:
    unit_economics: str
    operational_costs: str
    revenue_streams: str
    financial_stability: str
    risk_level: str
    confidence_score: float


class FinancialSustainabilityAgent:
    def __init__(self, openai_client):
        self.client = openai_client
        self.model = "gpt-4o-mini"
    
    def analyze(self, business_idea: str) -> FinancialAnalysis:
        prompt = f"""أنت محلل مالي محترف (Financial Sustainability Analyst).
        
مهمتك: تحليل الاستدامة المالية ونمذجة اقتصاديات الوحدة.

الفكرة/المشروع المطروح:
{business_idea}

قم بتحليل شامل يتضمن:
1. اقتصاديات الوحدة (Unit Economics): كم تكلفة الوحدة؟ وكم الربح؟
2. التكاليف التشغيلية (Operational Costs): ما هي المصاريف الثابتة والمتغيرة؟
3. مصادر الدخل (Revenue Streams): كيف سيولد المشروع الإيرادات؟
4. الاستقرار المالي طويل الأمد (Long-term Financial Stability): هل المشروع قابل للاستمرار؟
5. مستوى المخاطرة (Risk Level): منخفض/متوسط/عالي
6. نسبة الثقة (Confidence Score): 0-100%

أجب بصيغة JSON:
{{
    "unit_economics": "...",
    "operational_costs": "...",
    "revenue_streams": "...",
    "financial_stability": "...",
    "risk_level": "منخفض/متوسط/عالي",
    "confidence_score": 0.85
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        import json
        result = json.loads(response.choices[0].message.content)
        
        return FinancialAnalysis(
            unit_economics=result.get("unit_economics", ""),
            operational_costs=result.get("operational_costs", ""),
            revenue_streams=result.get("revenue_streams", ""),
            financial_stability=result.get("financial_stability", ""),
            risk_level=result.get("risk_level", "متوسط"),
            confidence_score=result.get("confidence_score", 0.5)
        )
