import unittest
from unittest.mock import patch
from gate import security_gate
from gate import security_gate, _to_int


class TestSecurityGate(unittest.TestCase):

    @patch("gate.load_scan_result")
    def test_block_when_critical_found(self, mock_load):
        """It should BLOCK when a CRITICAL issue is found."""
        mock_load.return_value = {"critical": 1, "high": 0, "medium": 2}

        decision, critical, high, medium = security_gate()

        self.assertEqual(decision, "BLOCK")
        self.assertEqual(critical, 1)
        self.assertEqual(high, 0)
        self.assertEqual(medium, 2)

    @patch("gate.load_scan_result")
    def test_warn_when_high_found(self, mock_load):
        """It should WARN when a HIGH issue is found."""
        mock_load.return_value = {"critical": 0, "high": 1, "medium": 2}

        decision, critical, high, medium = security_gate()

        self.assertEqual(decision, "WARN")
        self.assertEqual(critical, 0)
        self.assertEqual(high, 1)
        self.assertEqual(medium, 2)

    @patch("gate.load_scan_result")
    def test_allow_when_only_medium_found(self, mock_load):
        """It should ALLOW when only MEDIUM issues are found (<5)."""
        mock_load.return_value = {"critical": 0, "high": 0, "medium": 3}

        decision, critical, high, medium = security_gate()

        self.assertEqual(decision, "ALLOW")
        self.assertEqual(critical, 0)
        self.assertEqual(high, 0)
        self.assertEqual(medium, 3)

    @patch("gate.load_scan_result")
    def test_allow_when_report_is_empty(self, mock_load):
        """It should ALLOW when report is empty."""
        mock_load.return_value = {}

        decision, critical, high, medium = security_gate()

        self.assertEqual(decision, "ALLOW")
        self.assertEqual(critical, 0)
        self.assertEqual(high, 0)
        self.assertEqual(medium, 0)

    @patch("gate.load_scan_result")
    def test_edge_case_non_dict_report(self, mock_load):
        """If report is not a dict (e.g., None), it should ALLOW and treat counts as 0."""
        mock_load.return_value = None

        decision, critical, high, medium = security_gate()

        self.assertEqual(decision, "ALLOW")
        self.assertEqual(critical, 0)
        self.assertEqual(high, 0)
        self.assertEqual(medium, 0)

    @patch("gate.load_scan_result")
    def test_warn_when_5_medium_found(self, mock_load):
        """It should WARN when 5 (or more) MEDIUM issues are found."""
        mock_load.return_value = {"critical": 0, "high": 0, "medium": 5}

        decision, critical, high, medium = security_gate()

        self.assertEqual(decision, "WARN")
        self.assertEqual(critical, 0)
        self.assertEqual(high, 0)
        self.assertEqual(medium, 5)
    
    @patch("gate.load_scan_result")
    def test_warn_when_high_is_string_number(self, mock_scanner):
        mock_scanner.return_value = {"critical": 0, "high": "1", "medium": 0}

        decision, critical, high, medium = security_gate()

        self.assertEqual(decision, "WARN")
        self.assertEqual(high, 1)

    def test_to_int_converts_string_number(self):
        self.assertEqual(_to_int("1"), 1)

    def test_to_int_converts_float_string(self):
        self.assertEqual(_to_int("2.5"), 0)  

    def test_to_int_returns_zero_for_none(self):
        self.assertEqual(_to_int(None), 0)

    def test_to_int_returns_zero_for_text(self):
        self.assertEqual(_to_int("abc"), 0)
