from utils import parse_money

class UnderwritingAgent:
    def assess_risk(self, data):
        income = parse_money(data["income"])
        loan_amount = parse_money(data["loan_amount"])
        existing_emi = parse_money(data["existing_emi"])

        tenure_years = int(data["tenure"].split()[0])
        tenure_months = tenure_years * 12

        estimated_emi = loan_amount / tenure_months if tenure_months else 0
        emi_ratio = estimated_emi / income if income else 1

        risk_score = 0

        if data["employment_type"].lower() == "salaried":
            risk_score += 1
        else:
            risk_score += 2

        if "year" in data["job_duration"].lower():
            risk_score += 1
        else:
            risk_score += 2

        if existing_emi > 0:
            risk_score += 2

        if data["missed_payments"].lower() == "yes":
            risk_score += 3

        if "year" in data["bank_vintage"].lower():
            risk_score += 1
        else:
            risk_score += 2

        if risk_score <= 5:
            risk_level = "LOW"
        elif risk_score <= 8:
            risk_level = "MEDIUM"
        else:
            risk_level = "HIGH"

        # DECISIONS
        if emi_ratio <= 0.5 and risk_level == "LOW":
            return {
                "decision": "APPROVED",
                "risk_level": risk_level,
                "approved_amount": loan_amount,
                "approved_tenure": tenure_years,
                "reason": (
                    "Based on your income stability, job profile, and current financial commitments, "
                    "your monthly repayment comfortably fits within your income. "
                    "This means the loan should be easy for you to manage without financial stress."
                )
            }

        if risk_level == "MEDIUM":
            adjusted_amount = int(loan_amount * 0.8)
            adjusted_tenure = tenure_years + 2

            return {
                "decision": "APPROVED_WITH_CHANGES",
                "risk_level": risk_level,
                "approved_amount": adjusted_amount,
                "approved_tenure": adjusted_tenure,
                "reason": (
                    "We noticed that your current income and commitments may make the originally "
                    "requested loan slightly heavy on your monthly budget. "
                    "To keep your EMI comfortable and avoid financial pressure, "
                    "we recommend a slightly adjusted loan option."
                )
            }

        return {
            "decision": "REJECTED",
            "risk_level": risk_level,
            "approved_amount": None,
            "approved_tenure": None,
            "reason": (
                "At this moment, your income level, existing loan commitments, "
                "and repayment history indicate that taking on this loan may cause "
                "financial strain. We want to ensure you remain financially safe. "
                "You are welcome to reapply once your situation improves."
            )
        }
