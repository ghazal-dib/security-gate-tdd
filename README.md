[![Security Gate TDD](https://github.com/ghazal-dib/security-gate-tdd/actions/workflows/pipeline.yml/badge.svg)](https://github.com/ghazal-dib/security-gate-tdd/actions/workflows/pipeline.yml)
---

# 🔐 Security Gate TDD (DevSecOps Mini Project)

A **Test-Driven DevSecOps Security Gate** implemented in Python and integrated with **GitHub Actions CI/CD**.
This project simulates how real-world security gates block or warn deployments based on automated scan results.

---

## 🎯 Project Objective

The goal of this project is to demonstrate **how DevSecOps teams enforce security policies automatically** inside CI/CD pipelines using:

* Test Driven Development (TDD)
* Mocking & patching
* Security decision logic
* CI/CD fail-fast gates
* Artifacts for auditability

This mirrors how security gates are implemented in production pipelines.

---

## 🧱 Architecture Overview

```
scanner.py  ──▶ scan_result.json
                   │
                   ▼
             gate.py (decision engine)
                   │
                   ▼
          gate_decision.json + exit code
                   │
                   ▼
          GitHub Actions pipeline
```

* **scanner.py** simulates a security scanner
* **gate.py** evaluates scan results and decides:

  * `BLOCK`
  * `WARN`
  * `ALLOW`
* **test_gate.py** validates logic using TDD and mocks
* **pipeline.yml** enforces security in CI/CD

---

## 📂 Project Structure

```
security-gate-tdd/
├── gate.py                 # Security gate decision engine
├── scanner.py              # Scanner simulation
├── test_gate.py            # Unit tests (TDD)
├── requirements.txt        # Python dependencies
├── README.md
├── .gitignore
└── .github/
    └── workflows/
        └── pipeline.yml
```

---

## ⚙️ How the Security Gate Works

### 1️⃣ Scan Result Loading

* Reads `scan_result.json`
* Handles missing / invalid files safely
* Protects against malformed data

### 2️⃣ Data Normalization

* Uses `_to_int()` to safely convert values
* Prevents crashes if scanner outputs strings or invalid types

### 3️⃣ Decision Rules

| Condition          | Result  |
| ------------------ | ------- |
| Any `critical > 0` | ❌ BLOCK |
| Any `high > 0`     | ⚠️ WARN |
| `medium ≥ 5`       | ⚠️ WARN |
| Otherwise          | ✅ ALLOW |

### 4️⃣ Output

* Writes decision to `gate_decision.json`
* Exits with:

  * `1` → pipeline blocked
  * `0` → pipeline allowed

---

## 🧪 Testing Strategy (TDD)

* Tests written **before** implementation
* Uses `unittest` + `patch`
* Scanner is **mocked**, not executed
* Covers:

  * Critical findings
  * High findings
  * Medium thresholds
  * Empty reports
  * Invalid scanner output

This ensures **pure logic testing**, not external dependency testing.

---

## 🚀 CI/CD Pipeline

The GitHub Actions pipeline enforces security automatically:

### Pipeline Stages

1. **Tests job**

   * Runs unit tests
   * Fails pipeline if logic breaks

2. **Gate job** (runs only if tests pass)

   * Runs scanner
   * Uploads scan result artifact
   * Runs security gate
   * Uploads gate decision artifact

Artifacts provide **traceability and audit evidence**.

---

## 📦 Artifacts Generated

* `scan_result.json` → scanner output
* `gate_decision.json` → final security decision

Both are uploaded as GitHub Actions artifacts.

---

## 🛠 Technologies Used

* Python 3.12
* unittest & pytest
* GitHub Actions
* TDD & mocking
* JSON-based security reporting

---

## 🧠 Why This Project Matters

This project demonstrates **real DevSecOps skills**, including:

* Writing security logic with TDD
* Isolating dependencies via mocks
* Enforcing security via CI/CD
* Producing auditable security decisions
* Fail-fast deployment strategies

✅ Suitable for **Junior / Associate DevSecOps roles**

---

## 🔮 Future Improvements

* Replace scanner simulation with real tools (Trivy, Semgrep)
* Add severity weighting
* Support SARIF input
* Add Slack / Teams notifications

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

## 📜 License

Educational / Demonstration project.

---

