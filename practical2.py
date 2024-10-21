def verify_otp(otp):
    """
    Verifies if the OTP is valid.
    A valid OTP is either a 4-digit or 6-digit numeric string.
    
    Parameters:
    otp (str): The OTP to verify.
    
    Returns:
    bool: True if the OTP is valid, False otherwise.
    """
    return (len(otp) == 4 or len(otp) == 6) and otp.isdigit()

# Test cases for OTP verification
def run_tests():
    test_cases = [
        ("1234", True),      # Valid 4-digit OTP
        ("123456", True),    # Valid 6-digit OTP
        ("123", False),      # Invalid: less than 4 digits
        ("12345", False),    # Invalid: 5 digits
        ("1234567", False),  # Invalid: more than 6 digits
        ("12a4", False),     # Invalid: non-numeric characters
        ("12345b", False),   # Invalid: non-numeric characters
        ("!@#$%^", False)    # Invalid: non-numeric characters
    ]
    
    for otp, expected in test_cases:
        result = verify_otp(otp)
        print(f"verify_otp('{otp}') = {result}, expected = {expected}")
        assert result == expected, f"Test failed for OTP: {otp}"

run_tests()