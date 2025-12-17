from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage


class SalesAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.3
        )

        self.system_prompt = SystemMessage(
            content="""
You are a friendly Personal Loan Sales Agent working for an NBFC.

IMPORTANT RULES:
- Speak like a real human loan officer
- Be polite, calm, and reassuring
- NEVER approve or reject loans
- NEVER mention credit score or internal systems
- Use very simple English
- Convince gently if customer hesitates
- Do NOT explain things the customer did not ask for
"""
        )

    # ---------- EXISTING METHODS (UNCHANGED) ----------

    def ask_question(self, question, memory):
        messages = [
            self.system_prompt,
            HumanMessage(
                content=f"""
Customer details so far:
{memory}

Now ask the customer this question in a natural, human way:
{question}
"""
            )
        ]
        return self.llm.invoke(messages).content

    def explain_emi(self, memory):
        messages = [
            self.system_prompt,
            HumanMessage(
                content=f"""
Customer details:
{memory}

Explain EMI ONLY because income and tenure are now known.
Explain it very simply.
"""
            )
        ]
        return self.llm.invoke(messages).content

    def persuade(self, reason, memory):
        messages = [
            self.system_prompt,
            HumanMessage(
                content=f"""
The customer is hesitant or rejecting the loan.

Reason given by customer:
{reason}

Customer details:
{memory}

Convince the customer politely by explaining benefits like:
- Quick approval
- Flexible EMIs
- No collateral
- Useful for emergencies

Do NOT force. Be respectful.
"""
            )
        ]
        return self.llm.invoke(messages).content

    def summarize(self, memory):
        messages = [
            self.system_prompt,
            HumanMessage(
                content=f"""
Here are the collected customer details:
{memory}

Summarize these details clearly and say eligibility will now be checked.
"""
            )
        ]
        return self.llm.invoke(messages).content

    # ---------- NEW METHOD (FIX) ----------

    def start_conversation(self):
        """
        Controls the entire sales conversation.
        Returns collected customer data as memory dict.
        """

        memory = {}

        print(self.ask_question(
            "Greet the customer and ask how you can help.",
            memory
        ))

        input("\n👤 You: ")

        # Loan amount
        print(self.ask_question("Ask how much loan amount the customer wants.", memory))
        memory["loan_amount"] = input("\n👤 You: ")

        # Purpose
        print(self.ask_question("Ask the purpose of the loan.", memory))
        memory["purpose"] = input("\n👤 You: ")

        # Tenure
        print(self.ask_question("Ask how long they want to repay the loan.", memory))
        memory["tenure"] = input("\n👤 You: ")

        # Income
        print(self.ask_question(
            "Ask monthly income and explain it is needed to suggest comfortable EMI.",
            memory
        ))
        memory["income"] = input("\n👤 You: ")

        # Explain EMI (now it makes sense)
        print("\n🤖", self.explain_emi(memory))

        # Phone
        print(self.ask_question("Ask for the customer's phone number.", memory))
        memory["phone"] = input("\n👤 You: ")

        # Address
        print(self.ask_question("Ask for the customer's current address.", memory))
        memory["address"] = input("\n👤 You: ")

        # ID
        print(self.ask_question("Ask what ID proof they will provide.", memory))
        memory["id_type"] = input("\n👤 You: ")

        # Summary
        print("\n🤖", self.summarize(memory))

        return memory
