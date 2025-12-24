from datetime import datetime
import sys
import json
def load_scan_result(path="scan_result.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            result = json.load(f)
        return result if isinstance(result, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def _to_int(x):
    try:
        return int(x)
    except (ValueError, TypeError):
        return 0

def security_gate():

    """ Decide whether to BLOCK, WARN, or ALLOW based on scan results """

    report = load_scan_result()

    if not isinstance(report, dict):
        report = {}

    critical_count = _to_int(report.get("critical", 0))
    high_count = _to_int(report.get("high", 0))
    medium_count = _to_int(report.get("medium", 0)) 

    if critical_count > 0:
        return "BLOCK", critical_count, high_count, medium_count

    if high_count > 0:
        return "WARN", critical_count, high_count, medium_count
    
    if medium_count >= 5:
        return "WARN", critical_count, high_count, medium_count

    return "ALLOW", critical_count, high_count, medium_count

def write_decision_file(decision, critical, high, medium, path="gate_decision.json"):
    """ Write the gate decision and counts to a JSON file """
    payload = {
        "decision": decision,
        "counts":{
        "critical": critical,
        "high": high,
        "medium": medium
        },
        "generated_at_utc": datetime.utcnow().isoformat()+ "Z"
    }
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)

def main():
    decision, critical, high, medium = security_gate()

    write_decision_file(decision, critical, high, medium)

    if decision == "BLOCK":
        print("❌ Security Gate: BLOCKED (critical issues found)")
        sys.exit(1)

    if decision == "WARN":
        print("⚠️ Security Gate: WARNING (review required)")
        sys.exit(0)

    print("✅ Security Gate: ALLOWED")
    sys.exit(0)


if __name__ == "__main__":
    main()
