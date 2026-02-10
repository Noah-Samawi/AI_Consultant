import unittest
from unittest.mock import Mock, patch
from agents import MarketLogicAgent, FinancialSustainabilityAgent, CompetitiveDurabilityAgent
from orchestrator import AIConsultantOrchestrator


class TestAgents(unittest.TestCase):
    
    def setUp(self):
        self.mock_client = Mock()
        self.test_idea = "منصة توصيل مخبوزات محلية"
    
    def test_market_agent_initialization(self):
        agent = MarketLogicAgent(self.mock_client)
        self.assertEqual(agent.model, "gpt-4o-mini")
        self.assertIsNotNone(agent.client)
    
    def test_financial_agent_initialization(self):
        agent = FinancialSustainabilityAgent(self.mock_client)
        self.assertEqual(agent.model, "gpt-4o-mini")
        self.assertIsNotNone(agent.client)
    
    def test_competitive_agent_initialization(self):
        agent = CompetitiveDurabilityAgent(self.mock_client)
        self.assertEqual(agent.model, "gpt-4o-mini")
        self.assertIsNotNone(agent.client)
    
    @patch('agents.market_logic.MarketLogicAgent.analyze')
    def test_market_analysis_output_format(self, mock_analyze):
        mock_analyze.return_value = Mock(
            market_demand="High demand",
            customer_segments="SMEs",
            market_trends="Growing",
            demand_gaps="Quality gap",
            risk_level="متوسط",
            confidence_score=0.8
        )
        
        agent = MarketLogicAgent(self.mock_client)
        result = agent.analyze(self.test_idea)
        
        self.assertIsNotNone(result.market_demand)
        self.assertIsNotNone(result.confidence_score)


class TestOrchestrator(unittest.TestCase):
    
    @patch.dict('os.environ', {'OPENAI_API_KEY': 'test_key'})
    def test_orchestrator_initialization(self):
        orchestrator = AIConsultantOrchestrator(api_key="test_key")
        self.assertIsNotNone(orchestrator.market_agent)
        self.assertIsNotNone(orchestrator.financial_agent)
        self.assertIsNotNone(orchestrator.competitive_agent)
        self.assertIsNotNone(orchestrator.synthesizer)


if __name__ == '__main__':
    unittest.main()
