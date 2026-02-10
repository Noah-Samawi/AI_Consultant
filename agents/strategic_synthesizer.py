from typing import Dict, Any
from dataclasses import dataclass
from .market_logic import MarketAnalysis
from .financial_sustainability import FinancialAnalysis
from .competitive_durability import CompetitiveAnalysis


@dataclass
class StrategicMemo:
    executive_summary: str
    detailed_analysis: Dict[str, str]
    overall_risk_level: str
    overall_confidence_score: float
    final_recommendation: str
    conflicts_identified: str
    resolution_rationale: str


class StrategicSynthesizerAgent:
    def __init__(self, openai_client):
        self.client = openai_client
        self.model = "gpt-4o"
    
    def synthesize(
        self,
        business_idea: str,
        market_analysis: MarketAnalysis,
        financial_analysis: FinancialAnalysis,
        competitive_analysis: CompetitiveAnalysis
    ) -> StrategicMemo:
        prompt = f"""أنت شريك عام استراتيجي (General Partner / Strategic Decision Maker).

مهمتك: إجراء "حل التعارض" (Conflict Resolution) بين آراء المحللين الثلاثة، وإصدار مذكرة استراتيجية نهائية.

الفكرة/المشروع المطروح:
{business_idea}

========== تحليل السوق (Market Logic) ==========
الطلب السوقي: {market_analysis.market_demand}
شرائح العملاء: {market_analysis.customer_segments}
اتجاهات السوق: {market_analysis.market_trends}
فجوات الطلب: {market_analysis.demand_gaps}
مستوى المخاطرة: {market_analysis.risk_level}
نسبة الثقة: {market_analysis.confidence_score * 100}%

========== التحليل المالي (Financial Sustainability) ==========
اقتصاديات الوحدة: {financial_analysis.unit_economics}
التكاليف التشغيلية: {financial_analysis.operational_costs}
مصادر الدخل: {financial_analysis.revenue_streams}
الاستقرار المالي: {financial_analysis.financial_stability}
مستوى المخاطرة: {financial_analysis.risk_level}
نسبة الثقة: {financial_analysis.confidence_score * 100}%

========== التحليل التنافسي (Competitive Durability) ==========
حواجز الدخول: {competitive_analysis.entry_barriers}
قوة الحماية التنافسية: {competitive_analysis.moat_strength}
سهولة التكرار: {competitive_analysis.ease_of_replication}
عرض القيمة الفريد: {competitive_analysis.unique_value_proposition}
مستوى المخاطرة: {competitive_analysis.risk_level}
نسبة الثقة: {competitive_analysis.confidence_score * 100}%

========== المطلوب منك ==========
1. تحديد التعارضات بين آراء المحللين الثلاثة
2. حل هذه التعارضات بناءً على المنطق الاستراتيجي
3. إصدار مذكرة استراتيجية نهائية تتضمن:
   - ملخص تنفيذي (Executive Summary)
   - تحليل تفصيلي لكل مسار (Detailed Analysis)
   - مستوى المخاطرة الإجمالي (Overall Risk Level)
   - نسبة الثقة الإجمالية (Overall Confidence Score)
   - التوصية النهائية (Final Recommendation)

أجب بصيغة JSON:
{{
    "executive_summary": "ملخص تنفيذي شامل من 3-5 جمل يوضح الصورة الكبيرة",
    "detailed_analysis": {{
        "market_perspective": "تحليل من منظور السوق",
        "financial_perspective": "تحليل من منظور مالي",
        "competitive_perspective": "تحليل من منظور تنافسي"
    }},
    "overall_risk_level": "منخفض/متوسط/عالي",
    "overall_confidence_score": 0.85,
    "final_recommendation": "التوصية النهائية: هل يجب المضي في المشروع؟ ولماذا؟",
    "conflicts_identified": "التعارضات التي وجدتها بين المحللين",
    "resolution_rationale": "كيف تم حل هذه التعارضات والمبررات"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        import json
        result = json.loads(response.choices[0].message.content)
        
        return StrategicMemo(
            executive_summary=result.get("executive_summary", ""),
            detailed_analysis=result.get("detailed_analysis", {}),
            overall_risk_level=result.get("overall_risk_level", "متوسط"),
            overall_confidence_score=result.get("overall_confidence_score", 0.5),
            final_recommendation=result.get("final_recommendation", ""),
            conflicts_identified=result.get("conflicts_identified", ""),
            resolution_rationale=result.get("resolution_rationale", "")
        )
