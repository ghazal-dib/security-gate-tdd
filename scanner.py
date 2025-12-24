import json

def run_scanner():
     """ Simulate a security scan and write results to a JSON file """

     result = {
          "critical": 0,
          "high": 1,
          "medium": 3
     }

     with open("scan_result.json", "w", encoding="utf-8") as f:
      json.dump(result, f, indent=2)

    
     print("Scan completed. Results written to scan_result.json")
if __name__ == "__main__":
     run_scanner()