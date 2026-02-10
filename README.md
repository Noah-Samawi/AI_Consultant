# AI Strategic Consultant System
# نظام التحليل الاستراتيجي متعدد الوكلاء

A multi-agent strategic analysis system using the Directed Diamond Topology and Graph of Thoughts (GoT) framework.

## System Architecture

### Phase 1: The Divergence Layer
Three parallel agents analyze different aspects:
- **Market Logic Agent**: Market dynamics and demand-side gaps
- **Financial Sustainability Agent**: Unit economics and financial viability
- **Competitive Durability Agent**: Entry barriers and moat strength

### Phase 2: The Synthesis Node
- **Strategic Synthesizer Agent**: Performs conflict resolution and produces final strategic memo

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

```python
from orchestrator import AIConsultantOrchestrator

orchestrator = AIConsultantOrchestrator()

business_idea = """
منصة توصيل مخبوزات محلية يومية عبر الاشتراكات الشهرية في الرياض.
الفكرة: ربط المخابز الصغيرة بالعملاء، مع ضمان جودة وطازجية يومية.
"""

result = orchestrator.analyze(business_idea)
```

## Project Structure

```
AI_Consultant/
├── agents/
│   ├── __init__.py
│   ├── market_logic.py
│   ├── financial_sustainability.py
│   ├── competitive_durability.py
│   └── strategic_synthesizer.py
├── orchestrator.py
├── requirements.txt
└── README.md
```

## Output Format

The system provides a comprehensive dashboard in Arabic with:
- Executive Summary (ملخص تنفيذي)
- Detailed Analysis (التحليل التفصيلي لكل مسار)
- Risk Level & Confidence Score (مستوى المخاطر ونسبة الثقة)
- Final Recommendation (التوصية النهائية)

## Features

- Multi-agent parallel processing
- Conflict resolution between agent outputs
- Bilingual output (Arabic with English technical terms)
- Rich CLI interface with colored output
- Structured JSON responses
- Comprehensive strategic analysis
