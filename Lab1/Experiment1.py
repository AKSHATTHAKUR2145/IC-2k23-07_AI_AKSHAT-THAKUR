"""Lab 1: Production system / rule-based reasoning."""
from dataclasses import dataclass
from typing import Callable

@dataclass
class Rule:
    name: str
    condition: Callable[[dict], bool]
    action: Callable[[dict], dict]

def run_production_system(facts: dict, rules: list[Rule], max_steps=10):
    """Apply first matching rule repeatedly until no rule matches."""
    trace = []
    for _ in range(max_steps):
        matched = False
        for rule in rules:
            if rule.condition(facts):
                facts = rule.action(facts)
                trace.append((rule.name, facts.copy()))
                matched = True
                break
        if not matched:
            break
    return facts, trace

def main():
    rules = [
        Rule("Fever rule", lambda f: f.get("temperature", 0) >= 38 and "status" not in f,
             lambda f: {**f, "status": "fever"}),
        Rule("Cough rule", lambda f: f.get("cough", False) and f.get("status") == "fever",
             lambda f: {**f, "suggestion": "Consult a doctor; possible respiratory infection"}),
        Rule("Normal rule", lambda f: "status" not in f,
             lambda f: {**f, "status": "normal"}),
    ]
    facts, trace = run_production_system({"temperature": 38.5, "cough": True}, rules)
    print("Final facts:", facts)
    print("Rule trace:")
    for name, state in trace: print(f"  {name} -> {state}")

if __name__ == "__main__":
    main()
