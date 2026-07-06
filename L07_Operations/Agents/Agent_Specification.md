# Agent Specification (CAS Extension)

To instantiate a new agent, a complete specification must be added to the Agent Registry using the following format:

**Agent Name**: [Name]
**Agent ID**: AG-[XXX]
**Status**: [Core | Specialist | Temporary | Experimental | Retired]

## Core Definition
* **Purpose**: (What specific problem does this agent solve?)
* **Authority Limit**: (What decisions is this agent explicitly NOT allowed to make?)

## Boundaries
* **Scope**: (What exact domains does it govern?)
* **Non-Scope**: (What domains does it explicitly exclude?)

## Operational Interface
* **Inputs**: (What files/data trigger this agent?)
* **Outputs**: (What artifacts does it produce?)
* **Dependencies**: (What other agents or systems does it rely on?)

## Governance
* **Quality Gates**: (How is the output automatically or manually validated?)
* **KPIs**: (What metric defines this agent's success?)
* **Failure Modes**: (How does reality break this agent?)
* **Escalation Rules**: (When must it defer to the human Steward?)
* **Retirement Criteria**: (Under what conditions should this agent be sent to the Cemetery?)
