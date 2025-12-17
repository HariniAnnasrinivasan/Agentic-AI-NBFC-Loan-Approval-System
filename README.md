# 🤖 Agentic AI NBFC Loan Approval System

An end-to-end **Agentic AI–driven Personal Loan Processing System** that simulates a real-world **NBFC loan workflow** — from customer interaction to KYC verification, underwriting, and sanction letter generation.

This project demonstrates how **multiple AI agents** can collaborate to automate financial decision-making in a fair, explainable, and customer-friendly way.

---

## 📌 Problem Statement

Traditional NBFC loan processes are:
- Manual and time-consuming
- Dependent on human agents
- Inconsistent in decision-making
- Poor in customer experience

The goal of this project is to build an **AI-powered conversational loan assistant** that:
- Interacts like a human loan officer
- Automates verification and risk assessment
- Explains decisions clearly and politely
- Generates professional sanction letters
- Maintains customer history using a database

---

## 🧠 Solution Overview

This system is built using an **Agentic AI architecture**, where each agent has a **single, well-defined responsibility**, similar to roles in a real NBFC.

The system handles the **entire loan lifecycle**:
> Customer chat → KYC verification → Risk assessment → Loan decision → Sanction letter generation

---

## 🧩 Agents Implemented

### 1️⃣ Master Agent (Orchestrator)
- Controls the entire workflow
- Coordinates all other agents
- Maintains session memory
- Handles new vs returning customers
- Ensures polite and clear communication
- Saves application data to the database

---

### 2️⃣ Sales Agent (Customer Interaction)
- Acts like a human loan officer
- Collects loan details:
  - Loan amount
  - Purpose
  - Tenure
  - Income
  - Phone number
  - Address
  - ID proof
- Explains EMI in simple words
- Persuades politely if customer hesitates
- Never approves or rejects loans

---

### 3️⃣ Verification Agent (KYC)
- Verifies customer identity (KYC)
- Checks:
  - Phone number
  - Address
  - ID proof type
- Outcomes:
  - ✅ KYC Verified
  - 🟡 KYC Partial → Manual review
  - ❌ KYC Failed → Manual review
- Always explains the result politely

---

### 4️⃣ Underwriting Agent (Risk Assessment)
- Evaluates financial risk using:
  - Income stability
  - Employment type
  - Job duration
  - Existing EMIs
  - Missed payment history
  - Bank account vintage
- Decisions:
  - ✅ Approved
  - 🟡 Approved with changes (lower amount / longer tenure)
  - ❌ Rejected
- All decisions are **explainable and fair**

---

### 5️⃣ Sanction Letter Agent
- Generates a **professional PDF sanction letter**
- Triggered for:
  - Approved loans
  - Approved-with-changes loans
- Includes:
  - Approved amount
  - Tenure
  - EMI estimate
  - Interest rate
  - Terms & conditions

---

## 🗄️ Database Usage

The system uses a database to:
- Store customer applications
- Track KYC status
- Store underwriting decisions
- Support returning customers
- Maintain an audit trail

This makes the system **persistent and realistic**, not just a chatbot.

---

## 🔁 End-to-End Workflow

1. Customer starts the chat
2. Sales Agent collects loan details
3. Verification Agent performs KYC
   - If not verified → Manual review
4. Underwriting Agent assesses risk
5. Loan decision is made:
   - Approved
   - Approved with changes
   - Rejected
6. Decision is explained politely to the customer
7. Sanction letter is generated (if approved)
8. Application data is stored in the database

---

## 🛠️ Tech Stack

- **Python**
- **Agent-based architecture**
- **Google Gemini (LLM)**
- **MySQL / SQLite (database)**
- **ReportLab (PDF generation)**
- **Git & GitHub**

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/HariniAnnasrinivasan/Agentic-AI-NBFC-Loan-Approval-System.git
cd Agentic-AI-NBFC-Loan-Approval-System

### Install Dependencies
pip install -r requirements.txt

### Set Environment Variables

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key_here

### Run the Application
python run_chat.py
