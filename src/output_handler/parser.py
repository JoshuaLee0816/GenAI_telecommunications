# src/output_handler/parser.py

import json
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class JSONOutputParser:
    """
    Analyze LLM structural JSON output
    """

    def parse(self, raw_output: str) -> Dict[str, Any]:
        try:
            parsed = json.loads(raw_output)
        except:
            logger.error(f"Invalid JSON output: {raw_output}")
            return self._error_result("Invalid JSON format")
        
        if not isinstance(parsed, dict):
            logger.error(f"Output is not a JSON object: {raw_output}")
            return self._error_result("Output is not a JSON object")
        
        return parsed
    
    def _error_result(self, message: str) -> Dict[str, Any]:
        return {
            "category": None,
            "priority": None,
            "recommended_action": None,
            "error": message
        }   