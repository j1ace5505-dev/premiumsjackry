# Premium Packages
PREMIUM_PACKAGES = {
    'basic': {
        'name': 'Basic',
        'price': 50000,  # IDR
        'duration_days': 30,
        'features': ['Basic features', 'Email support']
    },
    'pro': {
        'name': 'Pro',
        'price': 150000,  # IDR
        'duration_days': 90,
        'features': ['All Basic features', 'Priority support', 'Advanced analytics']
    },
    'enterprise': {
        'name': 'Enterprise',
        'price': 500000,  # IDR
        'duration_days': 365,
        'features': ['All Pro features', '24/7 support', 'Custom integrations', 'Dedicated account manager']
    }
}

# Payment Status
PAYMENT_STATUS = {
    'PENDING': 'pending',
    'PROCESSING': 'processing',
    'SUCCESS': 'success',
    'FAILED': 'failed',
    'EXPIRED': 'expired'
}

# Messages
MESSAGES = {
    'welcome': '🎉 Welcome to Premium Sales Jackry!\n\nChoose an option:',
    'select_package': '📦 Select a premium package:',
    'payment_pending': '⏳ Payment pending. Please complete the QRIS payment within 10 minutes.',
    'payment_success': '✅ Payment successful! Your premium access is now active.',
    'payment_failed': '❌ Payment failed. Please try again.',
}
