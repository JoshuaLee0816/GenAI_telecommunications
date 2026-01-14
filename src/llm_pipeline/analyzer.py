# src/llm_pipeline/analyzer.py

from data_loader.models import Ticket
from data_loader.validator import DataValidator
from llm_pipeline.prompts import (SYSTEM_PROMPT, CATEGORY_PROMPT, PRIORITY_PROMPT)
from rag.retriever import Retriever
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class TicketAnalyzer:
    """
    Analyze a single ticket
    """
    def __init__(self, knowledge_base_path: str, llm_model: str = "gemini"):
        self.retriever = Retriever(knowledge_base_path)
        self.llm_model = llm_model
        self.validator = DataValidator()

    def analyze_ticket(self, ticket: Ticket) -> Dict[str, Any]:

        self.validator.validate_ticket(ticket)

        context = self.retriever.query(ticket.description, top_k = 3)

        prompt = self._build_prompt(ticket, context)

        llm_response = self._query_llm(prompt)

        result = self._parse_response(llm_response)
        
        return result
    
    def _build_prompt(self, ticket: Ticket, context: str) -> str:
        prompt = f"{SYSTEM_PROMPT}\n"
        prompt += f"Ticket Category Hint: {CATEGORY_PROMPT[ticket.category]}\n"
        prompt += f"Priority Assessment Instructions: {PRIORITY_PROMPT}\n"
        prompt += f"Context:\n{context}\n"
        prompt += f"Ticket Description:\n{ticket.description}\n"
        prompt += "Please return structured JSON with fields: category, priority, recommended_action."
        return prompt
    
    def _query_llm(self, prompt: str) -> str:
        # Replace with actual LLM API call
        logger.info(f"Sending prompt to LLM model {self.llm_model}")
        # Example placeholder response
        response = '{"category": "network_issue", "priority": "high", "recommended_action": "Restart router"}'
        return response
    
    def _parse_llm_output(self, llm_output: str) -> Dict[str, Any]:
        import json
        try:
            return json.loads(llm_output)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse LLM output: {llm_output}")
            return {"category": None, "priority": None, "recommended_action": None}

