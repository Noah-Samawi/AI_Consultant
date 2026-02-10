import os
from openai import OpenAI
from dotenv import load_dotenv
from agents import (
    MarketLogicAgent,
    FinancialSustainabilityAgent,
    CompetitiveDurabilityAgent,
    StrategicSynthesizerAgent,
)
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.layout import Layout
from rich.table import Table


class AIConsultantOrchestrator:
    def __init__(self, api_key: str = None):
        if api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            load_dotenv()
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        self.market_agent = MarketLogicAgent(self.client)
        self.financial_agent = FinancialSustainabilityAgent(self.client)
        self.competitive_agent = CompetitiveDurabilityAgent(self.client)
        self.synthesizer = StrategicSynthesizerAgent(self.client)
        self.console = Console()
    
    def analyze(self, business_idea: str):
        self.console.print("\n[bold cyan]═══════════════════════════════════════════════════[/bold cyan]")
        self.console.print("[bold cyan]   نظام التحليل الاستراتيجي متعدد الوكلاء[/bold cyan]")
        self.console.print("[bold cyan]   AI Strategic Consultant System[/bold cyan]")
        self.console.print("[bold cyan]═══════════════════════════════════════════════════[/bold cyan]\n")
        
        self.console.print(Panel(
            f"[yellow]{business_idea}[/yellow]",
            title="[bold]الفكرة المطروحة / Business Idea[/bold]",
            border_style="yellow"
        ))
        
        self.console.print("\n[bold green]● المرحلة 1: طبقة التباعد (The Divergence Layer)[/bold green]")
        self.console.print("[dim]تشغيل ثلاثة وكلاء متوازيين للتحليل...[/dim]\n")
        
        with self.console.status("[bold green]جاري التحليل السوقي...") as status:
            market_analysis = self.market_agent.analyze(business_idea)
            self.console.print("✓ [green]تم التحليل السوقي (Market Logic)[/green]")
            
            status.update("[bold blue]جاري التحليل المالي...")
            financial_analysis = self.financial_agent.analyze(business_idea)
            self.console.print("✓ [blue]تم التحليل المالي (Financial Sustainability)[/blue]")
            
            status.update("[bold magenta]جاري التحليل التنافسي...")
            competitive_analysis = self.competitive_agent.analyze(business_idea)
            self.console.print("✓ [magenta]تم التحليل التنافسي (Competitive Durability)[/magenta]")
        
        self.console.print("\n[bold yellow]● المرحلة 2: عقدة التوليف (The Synthesis Node)[/bold yellow]")
        self.console.print("[dim]جاري حل التعارضات وإنشاء المذكرة الاستراتيجية...[/dim]\n")
        
        with self.console.status("[bold yellow]جاري التوليف الاستراتيجي..."):
            strategic_memo = self.synthesizer.synthesize(
                business_idea,
                market_analysis,
                financial_analysis,
                competitive_analysis
            )
            self.console.print("✓ [yellow]تم إنشاء المذكرة الاستراتيجية (Strategic Memo)[/yellow]")
        
        self._display_dashboard(
            business_idea,
            market_analysis,
            financial_analysis,
            competitive_analysis,
            strategic_memo
        )
        
        return strategic_memo
    
    def _display_dashboard(
        self,
        business_idea,
        market_analysis,
        financial_analysis,
        competitive_analysis,
        strategic_memo
    ):
        self.console.print("\n\n")
        self.console.print("[bold cyan]═══════════════════════════════════════════════════[/bold cyan]")
        self.console.print("[bold cyan]           لوحة التحكم الاستراتيجية[/bold cyan]")
        self.console.print("[bold cyan]           Strategic Dashboard[/bold cyan]")
        self.console.print("[bold cyan]═══════════════════════════════════════════════════[/bold cyan]\n")
        
        self.console.print(Panel(
            strategic_memo.executive_summary,
            title="[bold]📊 ملخص تنفيذي / Executive Summary[/bold]",
            border_style="cyan",
            padding=(1, 2)
        ))
        
        self.console.print("\n[bold]🔍 التحليل التفصيلي لكل مسار / Detailed Analysis[/bold]\n")
        
        market_table = Table(title="[green]تحليل السوق / Market Logic[/green]", show_header=True, header_style="bold green")
        market_table.add_column("العنصر", style="cyan", width=25)
        market_table.add_column("التحليل", style="white", width=65)
        market_table.add_row("الطلب السوقي", market_analysis.market_demand)
        market_table.add_row("شرائح العملاء", market_analysis.customer_segments)
        market_table.add_row("اتجاهات السوق", market_analysis.market_trends)
        market_table.add_row("فجوات الطلب", market_analysis.demand_gaps)
        market_table.add_row("مستوى المخاطرة", market_analysis.risk_level)
        market_table.add_row("نسبة الثقة", f"{market_analysis.confidence_score * 100:.1f}%")
        self.console.print(market_table)
        
        self.console.print()
        
        financial_table = Table(title="[blue]التحليل المالي / Financial Sustainability[/blue]", show_header=True, header_style="bold blue")
        financial_table.add_column("العنصر", style="cyan", width=25)
        financial_table.add_column("التحليل", style="white", width=65)
        financial_table.add_row("اقتصاديات الوحدة", financial_analysis.unit_economics)
        financial_table.add_row("التكاليف التشغيلية", financial_analysis.operational_costs)
        financial_table.add_row("مصادر الدخل", financial_analysis.revenue_streams)
        financial_table.add_row("الاستقرار المالي", financial_analysis.financial_stability)
        financial_table.add_row("مستوى المخاطرة", financial_analysis.risk_level)
        financial_table.add_row("نسبة الثقة", f"{financial_analysis.confidence_score * 100:.1f}%")
        self.console.print(financial_table)
        
        self.console.print()
        
        competitive_table = Table(title="[magenta]التحليل التنافسي / Competitive Durability[/magenta]", show_header=True, header_style="bold magenta")
        competitive_table.add_column("العنصر", style="cyan", width=25)
        competitive_table.add_column("التحليل", style="white", width=65)
        competitive_table.add_row("حواجز الدخول", competitive_analysis.entry_barriers)
        competitive_table.add_row("قوة الحماية", competitive_analysis.moat_strength)
        competitive_table.add_row("سهولة التكرار", competitive_analysis.ease_of_replication)
        competitive_table.add_row("عرض القيمة الفريد", competitive_analysis.unique_value_proposition)
        competitive_table.add_row("مستوى المخاطرة", competitive_analysis.risk_level)
        competitive_table.add_row("نسبة الثقة", f"{competitive_analysis.confidence_score * 100:.1f}%")
        self.console.print(competitive_table)
        
        self.console.print("\n[bold]⚖️ حل التعارضات / Conflict Resolution[/bold]\n")
        
        self.console.print(Panel(
            strategic_memo.conflicts_identified,
            title="[bold]التعارضات المحددة / Identified Conflicts[/bold]",
            border_style="red",
            padding=(1, 2)
        ))
        
        self.console.print(Panel(
            strategic_memo.resolution_rationale,
            title="[bold]مبررات الحل / Resolution Rationale[/bold]",
            border_style="yellow",
            padding=(1, 2)
        ))
        
        risk_color = "red" if strategic_memo.overall_risk_level == "عالي" else "yellow" if strategic_memo.overall_risk_level == "متوسط" else "green"
        confidence_color = "green" if strategic_memo.overall_confidence_score >= 0.7 else "yellow" if strategic_memo.overall_confidence_score >= 0.4 else "red"
        
        self.console.print("\n[bold]📈 مستوى المخاطر ونسبة الثقة / Risk Level & Confidence Score[/bold]\n")
        
        risk_panel = Panel(
            f"[{risk_color}]{strategic_memo.overall_risk_level}[/{risk_color}]",
            title="مستوى المخاطرة الإجمالي",
            border_style=risk_color,
            padding=(1, 2),
            width=50
        )
        
        confidence_panel = Panel(
            f"[{confidence_color}]{strategic_memo.overall_confidence_score * 100:.1f}%[/{confidence_color}]",
            title="نسبة الثقة الإجمالية",
            border_style=confidence_color,
            padding=(1, 2),
            width=50
        )
        
        from rich.columns import Columns
        self.console.print(Columns([risk_panel, confidence_panel]))
        
        self.console.print("\n[bold]🎯 التوصية النهائية / Final Recommendation[/bold]\n")
        
        self.console.print(Panel(
            strategic_memo.final_recommendation,
            title="[bold]التوصية الاستراتيجية / Strategic Recommendation[/bold]",
            border_style="green",
            padding=(1, 2)
        ))
        
        self.console.print("\n[bold cyan]═══════════════════════════════════════════════════[/bold cyan]\n")


def main():
    orchestrator = AIConsultantOrchestrator()
    
    business_idea = """
    منصة توصيل مخبوزات محلية يومية عبر الاشتراكات الشهرية في الرياض.
    الفكرة: ربط المخابز الصغيرة بالعملاء، مع ضمان جودة وطازجية يومية.
    """
    
    orchestrator.analyze(business_idea)


if __name__ == "__main__":
    main()
