#!/usr/bin/env python3
"""
Quick test script to verify email functionality works
"""

import smtplib
from email.message import EmailMessage
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Test email configuration (replace with your actual values)
EMAIL_ADDRESS = "your-email@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "your-app-password"    # Replace with your app password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
TEST_RECIPIENT = "arunkumarhv14@gmail.com"

def create_test_chart():
    """Create a simple test chart"""
    try:
        # Create sample data
        hours = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00']
        consumption = [10, 15, 8, 12, 20, 18]
        
        # Create chart
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(hours, consumption, color='skyblue')
        ax.set_title('Test Chart - Hourly Consumption')
        ax.set_xlabel('Hour')
        ax.set_ylabel('Consumption')
        
        # Save to buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=150, bbox_inches='tight')
        buf.seek(0)
        plt.close(fig)
        
        return buf
    except Exception as e:
        print(f"Error creating chart: {e}")
        return None

def create_test_csv():
    """Create a simple test CSV"""
    try:
        data = {
            'timestamp': ['2025-01-02 10:00:00', '2025-01-02 11:00:00', '2025-01-02 12:00:00'],
            'device_id': ['test-device', 'test-device', 'test-device'],
            'consumption': [10, 15, 12],
            'battery_voltage': [3.8, 3.7, 3.6]
        }
        
        df = pd.DataFrame(data)
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)
        
        return csv_buffer
    except Exception as e:
        print(f"Error creating CSV: {e}")
        return None

def send_test_email():
    """Send a test email with attachments"""
    try:
        print("🧪 Creating test email...")
        
        # Create message
        msg = EmailMessage()
        msg["Subject"] = f"Test Email - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = TEST_RECIPIENT
        
        # Email content
        email_content = f"""
        Test Email Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        This is a test email to verify the email functionality is working correctly.
        
        Device ID: test-device-123
        Status: Testing
        
        Please find attached:
        - Test chart (PNG)
        - Test data (CSV)
        
        If you receive this email with attachments, the email system is working correctly!
        
        Best regards,
        Aquesa Data Monitor Test System
        """
        
        msg.set_content(email_content)
        print("✅ Email content set")
        
        # Create and attach test chart
        chart_buf = create_test_chart()
        if chart_buf:
            chart_data = chart_buf.read()
            chart_filename = f"test_chart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            msg.add_attachment(chart_data, maintype="image", subtype="png", filename=chart_filename)
            print(f"✅ Chart attached ({len(chart_data)} bytes)")
        
        # Create and attach test CSV
        csv_buf = create_test_csv()
        if csv_buf:
            csv_data = csv_buf.getvalue()
            csv_filename = f"test_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            msg.add_attachment(csv_data.encode('utf-8'), maintype="text", subtype="csv", filename=csv_filename)
            print(f"✅ CSV attached ({len(csv_data)} chars)")
        
        # Send email
        print("📤 Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            print("🔐 TLS started")
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            print("🔑 Login successful")
            smtp.send_message(msg)
            print("📨 Message sent")
        
        print(f"✅ Test email sent successfully to {TEST_RECIPIENT}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send test email: {e}")
        import traceback
        print(f"❌ Full traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    print("🧪 Email Functionality Test")
    print("=" * 50)
    print(f"From: {EMAIL_ADDRESS}")
    print(f"To: {TEST_RECIPIENT}")
    print(f"SMTP: {SMTP_SERVER}:{SMTP_PORT}")
    print("=" * 50)
    
    if EMAIL_ADDRESS == "your-email@gmail.com":
        print("❌ Please update EMAIL_ADDRESS and EMAIL_PASSWORD in this script first!")
        exit(1)
    
    success = send_test_email()
    
    if success:
        print("\n🎉 Test completed successfully!")
        print(f"📧 Check {TEST_RECIPIENT} for the test email with attachments.")
        print("If you received the email, the fix is working correctly!")
    else:
        print("\n❌ Test failed. Check the error messages above.")
