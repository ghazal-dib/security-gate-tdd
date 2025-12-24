# 🔐 Security Gate – DevSecOps (TDD-Based)

A **Python-based Security Gate** built using **Test-Driven Development (TDD)** principles and integrated into a **GitHub Actions CI/CD pipeline**.

This project simulates how real DevSecOps teams **block, warn, or allow deployments** based on security scan results.

---

## 🎯 Project Goals

This project demonstrates how to:

* Apply **Test Driven Development (TDD)** to security logic
* Safely consume scanner outputs (even malformed data)
* Enforce security decisions automatically in CI/CD
* Produce **machine-readable security decisions** (JSON artifacts)
* Fail fast on critical security issues

---

## 🧱 Project Structure

```
security-gate-tdd/
│
├── gate.py                # Security decision logic
├── scanner.py             # Simulated security scanner
├── test_gate.py           # Unit tests (TDD, mocking, patching)
├── scan_result.json       # Example scan output (ignored in Git)
├── gate_decision.json     # Gate decision artifact (generated)
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignored files & caches
│
└── .github/
    └── workflows/
        └── pipeline.yml   # GitHub Actions CI/CD pipeline
```

---

## ⚙️ How It Works

### 1️⃣ Security Scan (scanner.py)

A simulated scanner produces a JSON file:

```json
{
  "critical": 0,
  "high": 1,
  "medium": 3
}
```

In real projects, this could be:

* Trivy
* Snyk
* Semgrep
* OWASP Dependency-Check

---

### 2️⃣ Security Gate Logic (gate.py)

The gate evaluates the scan results using clear rules:

| Condition      | Decision |
| -------------- | -------- |
| `critical > 0` | ❌ BLOCK  |
| `high > 0`     | ⚠️ WARN  |
| `medium >= 5`  | ⚠️ WARN  |
| Otherwise      | ✅ ALLOW  |

The gate:

* Defends against missing files
* Defends against invalid JSON
* Defends against wrong data types
* Always returns a safe decision

---

### 3️⃣ Decision Artifact

After evaluation, the gate writes a structured artifact:

```json
{
  "decision": "WARN",
  "counts": {
    "critical": 0,
    "high": 1,
    "medium": 3
  },
  "generated_at_utc": "2025-01-01T12:00:00Z"
}
```

This allows:

* Auditing
* Reporting
* Downstream automation

---

## 🧪 Testing Strategy (TDD)

* All logic is covered by **unit tests**
* External dependencies are **mocked**
* Scanner input is **patched**
* Edge cases are tested:

  * Empty report
  * Non-dictionary report
  * String instead of numbers
  * Missing fields

Example:

```python
@patch("gate.load_scan_result")
def test_block_when_critical_found(self, mock_scanner):
    mock_scanner.return_value = {"critical": 1}
    decision, *_ = security_gate()
    self.assertEqual(decision, "BLOCK")
```

---

## 🚀 CI/CD Pipeline

Implemented with **GitHub Actions**:

### Pipeline Flow

1. Run unit tests (`pytest`)
2. Run scanner
3. Run security gate
4. Upload artifacts:

   * `scan_result.json`
   * `gate_decision.json`
5. Fail pipeline on **BLOCK**

---

## 🛡️ Why This Project Is Professional

This project reflects **real-world DevSecOps practices**:

* ✅ Test-driven security logic
* ✅ Fail-fast pipeline enforcement
* ✅ Safe handling of untrusted scanner output
* ✅ Auditable security decisions
* ✅ CI-friendly exit codes
* ✅ Clean separation of concerns

---

## 🧠 Skills Demonstrated

* Python (clean, defensive coding)
* Test Driven Development (TDD)
* Mocking & patching (`unittest.mock`)
* CI/CD security gates
* GitHub Actions
* JSON-based security automation

---

## ▶️ Run Locally

```bash
python scanner.py
python gate.py
```

Run tests:

```bash
pytest
```

---

## 📌 Future Improvements (Optional)

* Replace scanner with real tools (Trivy / Semgrep)
* Add severity thresholds via config
* Add SARIF support
* Upload results to security dashboards

---

## 👩‍💻 Target Audience

This project is suitable for:

* Junior DevSecOps Engineers
* Security Automation roles
* CI/CD-focused security teams

---

