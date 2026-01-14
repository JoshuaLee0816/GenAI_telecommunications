# Data Schema

This document defines the structure of a support ticket dataset.
Serves as a data constract between human operators, the LLM and downstream automation logic.

The LLM is expected to :
- classify ticket type
- Assess serverity and urgency
- Recommend handling workflow and escalation

## Field Definitions

### ticket_id
Purpose: Unique identifier for a support ticket
Used by LLM: No

### created_at
Purpose: Timestamp indicating when the ticket was created
Used by LLM: Conditional (only for urgency-related reasoning)

### issue_summary
Purpose: Short human-written summary of the customer issue.
Used by LLM: Yes

### issue_description
Purpose: Raw customer description of the issue, possibly unstrcutured.
Used by LLM: Yes

### service_type
Purpose: Indicates the service category involved (e.g., mobile, broadband, enterprise)
Used by LLM : Yes

### affected_area
Purpose: Geographic or logical area affected by the issue.
Used by LLM: conditional

### device_type
Purpose: Customer device or equipment related to the issue.
Used by LLM: Yes

### network_type
Purpose: Network category involved (e.g., 4G, 5G, fiber)
Used by LLM: Yes

### outage_flag
Purpose: Indicates whether a known outage exists at the time of ticket creation.
Used by LLM: Yes (As a hint, not a conclusion)

### historical_ticket_count
Purpose: Number of past tickets from the same customer or area.
Used by LLM: Conditional

### priority_hint
Purpose: Preliminary priority assigned by external systems or agents.
Used by LLM: Yes (as weak guidance only)