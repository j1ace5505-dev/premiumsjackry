import requests
import json
from datetime import datetime, timedelta
from config.settings import settings

class QRISGateway:
    """QRIS Payment Gateway Integration"""
    
    def __init__(self):
        self.api_key = settings.QRIS_API_KEY
        self.merchant_id = settings.QRIS_MERCHANT_ID
        self.api_url = settings.QRIS_API_URL
        self.api_secret = settings.QRIS_API_SECRET
    
    def generate_payment_qr(self, user_id: int, amount: float, description: str) -> dict:
        """
        Generate QRIS QR code for payment
        
        Args:
            user_id: Telegram user ID
            amount: Payment amount in IDR
            description: Payment description
        
        Returns:
            dict with qris_url and reference_id
        """
        try:
            payload = {
                'merchant_id': self.merchant_id,
                'amount': int(amount),
                'description': description,
                'reference_id': f"USER_{user_id}_{int(datetime.now().timestamp())}",
                'callback_url': f"https://your-domain.com/webhook/qris/callback",
                'expiry_time': (datetime.now() + timedelta(minutes=10)).isoformat()
            }
            
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            response = requests.post(
                f"{self.api_url}/api/qr-code/create",
                json=payload,
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'success': True,
                    'qris_url': data.get('qr_code_url'),
                    'reference_id': payload['reference_id'],
                    'amount': amount,
                    'expires_at': payload['expiry_time']
                }
            else:
                return {
                    'success': False,
                    'error': 'Failed to generate QRIS code',
                    'details': response.text
                }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def check_payment_status(self, reference_id: str) -> dict:
        """
        Check payment status from QRIS gateway
        
        Args:
            reference_id: QRIS reference ID
        
        Returns:
            dict with payment status
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            response = requests.get(
                f"{self.api_url}/api/qr-code/status/{reference_id}",
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'success': True,
                    'status': data.get('status'),  # 'success', 'pending', 'expired'
                    'transaction_id': data.get('transaction_id'),
                    'amount': data.get('amount')
                }
            else:
                return {
                    'success': False,
                    'status': 'unknown'
                }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def verify_webhook(self, payload: dict, signature: str) -> bool:
        """
        Verify webhook signature from QRIS provider
        """
        import hmac
        import hashlib
        
        try:
            payload_str = json.dumps(payload, separators=(',', ':'), sort_keys=True)
            expected_signature = hmac.new(
                self.api_secret.encode(),
                payload_str.encode(),
                hashlib.sha256
            ).hexdigest()
            
            return hmac.compare_digest(expected_signature, signature)
        
        except Exception:
            return False

qris_gateway = QRISGateway()
