from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class CompetitiveAnalysis:
    entry_barriers: str
    moat_strength: str
    ease_of_replication: str
    unique_value_proposition: str
    risk_level: str
    confidence_score: float


class CompetitiveDurabilityAgent:
    def __init__(self, openai_client):
        self.client = openai_client
        self.model = "gpt-4o-mini"
    
    def analyze(self, business_idea: str) -> CompetitiveAnalysis:
        prompt = f"""أنت محلل تنافسي محترف (Competitive Durability Analyst).
        
مهمتك: تقييم حواجز الدخول وقوة الحماية التنافسية (Moat).

الفكرة/المشروع المطروح:
{business_idea}

قم بتحليل شامل يتضمن:
1. حواجز الدخول (Entry Barriers): ما مدى صعوبة دخول منافسين جدد؟
2. قوة الحماية التنافسية (Moat Strength): ما الذي يحمي هذا المشروع من المنافسة؟
3. سهولة التكرار (Ease of Replication): هل يمكن تقليد هذه الفكرة بسهولة؟
4. عرض القيمة الفريد (Unique Value Proposition): ما الذي يجعل هذا المشروع مميزاً؟
5. مستوى المخاطرة (Risk Level): منخفض/متوسط/عالي
6. نسبة الثقة (Confidence Score): 0-100%

أجب بصيغة JSON:
{{
    "entry_barriers": "...",
    "moat_strength": "...",
    "ease_of_replication": "...",
    "unique_value_proposition": "...",
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
        
        return CompetitiveAnalysis(
            entry_barriers=result.get("entry_barriers", ""),
            moat_strength=result.get("moat_strength", ""),
            ease_of_replication=result.get("ease_of_replication", ""),
            unique_value_proposition=result.get("unique_value_proposition", ""),
            risk_level=result.get("risk_level", "متوسط"),
            confidence_score=result.get("confidence_score", 0.5)
        )
