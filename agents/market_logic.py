from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class MarketAnalysis:
    market_demand: str
    customer_segments: str
    market_trends: str
    demand_gaps: str
    risk_level: str
    confidence_score: float


class MarketLogicAgent:
    def __init__(self, openai_client):
        self.client = openai_client
        self.model = "gpt-4o-mini"
    
    def analyze(self, business_idea: str) -> MarketAnalysis:
        prompt = f"""أنت محلل سوق محترف (Market Logic Analyst).
        
مهمتك: تحليل ديناميكيات السوق والفجوات في الطلب.

الفكرة/المشروع المطروح:
{business_idea}

قم بتحليل شامل يتضمن:
1. الطلب السوقي (Market Demand): ما مدى قوة الحاجة لهذا المنتج/الخدمة؟
2. شرائح العملاء المستهدفة (Customer Segments): من هم العملاء المحتملون؟
3. اتجاهات السوق الحالية (Market Trends): ماذا يحدث في هذا السوق الآن؟
4. الفجوات في الطلب (Demand Gaps): ما هي الاحتياجات غير الملباة؟
5. مستوى المخاطرة (Risk Level): منخفض/متوسط/عالي
6. نسبة الثقة (Confidence Score): 0-100%

أجب بصيغة JSON:
{{
    "market_demand": "...",
    "customer_segments": "...",
    "market_trends": "...",
    "demand_gaps": "...",
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
        
        return MarketAnalysis(
            market_demand=result.get("market_demand", ""),
            customer_segments=result.get("customer_segments", ""),
            market_trends=result.get("market_trends", ""),
            demand_gaps=result.get("demand_gaps", ""),
            risk_level=result.get("risk_level", "متوسط"),
            confidence_score=result.get("confidence_score", 0.5)
        )
