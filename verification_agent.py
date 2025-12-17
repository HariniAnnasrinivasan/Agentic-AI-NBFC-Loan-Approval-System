class VerificationAgent:
    def verify_kyc(self, data):
        address = data.get("address", "").lower()
        phone = data.get("phone")
        id_type = data.get("id_type")

        if not phone or not address or not id_type:
            return (
                "KYC_PARTIAL",
                "Some of your identity details are missing. "
                "To keep your application safe, we need all basic information. "
                "You can provide the missing details and continue."
            )

        if "rural" in address or "village" in address:
            return (
                "KYC_FAILED",
                "We were unable to verify your address using digital records. "
                "This sometimes happens for rural or newly registered addresses. "
                "There is nothing to worry about — our team will manually review "
                "your details and update you."
            )

        return (
            "KYC_VERIFIED",
            "Your identity has been successfully verified. "
            "Thank you for sharing your details."
        )
