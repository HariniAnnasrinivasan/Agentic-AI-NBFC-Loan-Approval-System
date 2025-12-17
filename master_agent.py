from sales_agent import SalesAgent
from verification_agent import VerificationAgent
from underwriting_agent import UnderwritingAgent
from db import save_application
from sanction_letter_agent import SanctionLetterAgent


class MasterAgent:
    def __init__(self):
        self.sales = SalesAgent()
        self.verifier = VerificationAgent()
        self.underwriter = UnderwritingAgent()

    def start_chat(self):
        print("\n🤖 NBFC Loan Assistant\n")

        memory = self.sales.start_conversation()

        # ---------------- KYC ----------------
        status, reason = self.verifier.verify_kyc(memory)
        memory["kyc_status"] = status
        memory["kyc_reason"] = reason

        print("\n🤖", reason)

        if status != "KYC_VERIFIED":
            memory["application_state"] = "MANUAL_REVIEW_PENDING"
            save_application(memory)
            print(
                "🤖 Our verification team will carefully review your details. "
                "You will hear from us soon. Thank you for your patience."
            )
            return

        # ---------------- UNDERWRITING ----------------
        print("\n🤖 I need a few more details to assess your loan safely.")

        memory["employment_type"] = input("🤖 Employment type (salaried/self-employed/freelancer): ")
        memory["job_duration"] = input("🤖 How long have you been in this job/business?: ")
        memory["existing_emi"] = input("🤖 Total existing EMI amount (0 if none): ")
        memory["missed_payments"] = input("🤖 Have you missed EMIs earlier? (yes/no): ")
        memory["bank_vintage"] = input("🤖 How long have you had your bank account?: ")

        result = self.underwriter.assess_risk(memory)

        # 🔑 IMPORTANT FIX
        memory.update(result)

        print("\n🤖", result["reason"])

        # ---------------- DECISION HANDLING ----------------
        if result["decision"] == "APPROVED":
            print(
                f"🤖 Your loan of ₹{result['approved_amount']:,} "
                f"for {result['approved_tenure']} years has been approved."
            )

            sanction_agent = SanctionLetterAgent()
            pdf_path = sanction_agent.generate(memory)

            print("\n🤖 Your sanction letter has been generated successfully.")
            print(f"🤖 You can find it here: {pdf_path}")

        elif result["decision"] == "APPROVED_WITH_CHANGES":
            print(
                f"🤖 We can approve ₹{result['approved_amount']:,} "
                f"over {result['approved_tenure']} years so that your EMI stays comfortable."
            )

            sanction_agent = SanctionLetterAgent()
            pdf_path = sanction_agent.generate(memory)

            print("\n🤖 Your sanction letter has been generated successfully.")
            print(f"🤖 You can find it here: {pdf_path}")

        else:
            print(
                "🤖 We truly appreciate your interest. "
                "At this moment, approving this loan may not be financially safe for you. "
                "Please feel free to come back anytime — we’ll be happy to assist you."
            )

        save_application(memory)
