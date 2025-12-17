import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def save_application(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO loan_applications (
        phone_number, loan_amount, purpose, tenure, income,
        address, id_type, kyc_status, kyc_reason,
        employment_type, job_duration, existing_emi,
        missed_payments, bank_vintage,
        risk_level, underwriting_decision,
        underwriting_reason, approved_amount, approved_tenure,
        application_state
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON DUPLICATE KEY UPDATE
        kyc_status=VALUES(kyc_status),
        kyc_reason=VALUES(kyc_reason),
        employment_type=VALUES(employment_type),
        job_duration=VALUES(job_duration),
        existing_emi=VALUES(existing_emi),
        missed_payments=VALUES(missed_payments),
        bank_vintage=VALUES(bank_vintage),
        risk_level=VALUES(risk_level),
        underwriting_decision=VALUES(underwriting_decision),
        underwriting_reason=VALUES(underwriting_reason),
        approved_amount=VALUES(approved_amount),
        approved_tenure=VALUES(approved_tenure),
        application_state=VALUES(application_state)
    """

    cursor.execute(query, (
        data.get("phone"),
        data.get("loan_amount"),
        data.get("purpose"),
        data.get("tenure"),
        data.get("income"),
        data.get("address"),
        data.get("id_type"),
        data.get("kyc_status"),
        data.get("kyc_reason"),
        data.get("employment_type"),
        data.get("job_duration"),
        data.get("existing_emi"),
        data.get("missed_payments"),
        data.get("bank_vintage"),
        data.get("risk_level"),
        data.get("underwriting_decision"),
        data.get("underwriting_reason"),
        data.get("approved_amount"),
        data.get("approved_tenure"),
        data.get("application_state")
    ))

    conn.commit()
    cursor.close()
    conn.close()
