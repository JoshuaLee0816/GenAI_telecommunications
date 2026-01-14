# Sample Input/Output for GenAI Ticket Processing

This document shows example tickets in CSV form and their corresponding output JSON.

---

## Example 1

### CSV Input
ticket_id,created_at,issue_summary,issue_description,service_type,affected_area,device_type,network_type,outage_flag,historical_ticket_count,priority_hint
TICKET-001,2026-01-14,"Cannot connect to 5G network","Customer reports that phone cannot access 5G in downtown area","mobile","Downtown","smartphone","5G",TRUE,2,"high"

### JSON Output
{
  "ticket_type": "network_outage",
  "severity": "high",
  "escalation_required": true,
  "recommended_actions": [
    "check base station status",
    "notify on-call engineer"
  ],
  "confidence": 0.85
}

---

## Example 2

### CSV Input
ticket_id,created_at,issue_summary,issue_description,service_type,affected_area,device_type,network_type,outage_flag,historical_ticket_count,priority_hint
TICKET-002,2026-01-14,"Billing discrepancy","Customer charged twice for last month","billing","N/A","N/A","N/A",FALSE,1,"medium"

### JSON Output
{
  "ticket_type": "billing_issue",
  "severity": "medium",
  "escalation_required": false,
  "recommended_actions": [
    "review billing records",
    "issue refund if applicable"
  ],
  "confidence": 0.9
}