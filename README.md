# Premium Sales Jackry - Telegram Auto Order Bot

Automated Telegram bot for premium app sales with QRIS payment gateway integration.

## Features

- ✅ Telegram bot integration using python-telegram-bot
- ✅ QRIS payment gateway integration
- ✅ Automated order processing
- ✅ Premium package management
- ✅ Payment verification system
- ✅ User database management
- ✅ Admin dashboard

## Prerequisites

- Python 3.8+
- Telegram Bot Token (from @BotFather)
- QRIS Payment Gateway API credentials
- PostgreSQL or SQLite database

## Installation

```bash
git clone https://github.com/j1ace5505-dev/premiumsjackry.git
cd premiumsjackry
pip install -r requirements.txt
cp .env.example .env
# Update .env with your credentials
python main.py
```

## Project Structure

```
premiumsjackry/
├── src/
│   ├── bot/
│   │   ├── handlers/        # Message handlers
│   │   ├── callbacks/       # Callback handlers
│   │   └── middleware/      # Bot middleware
│   ├── payment/
│   │   ├── qris.py          # QRIS gateway integration
│   │   └── payment_handler.py
│   ├── database/
│   │   ├── models.py        # Database models
│   │   └── db_manager.py    # Database operations
│   └── admin/               # Admin functions
├── config/
│   ├── settings.py
│   └── constants.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Configuration

Create a `.env` file in the root directory:

```env
# Telegram
TELEGRAM_BOT_TOKEN=your_bot_token_here

# QRIS Payment Gateway
QRIS_API_KEY=your_qris_api_key
QRIS_MERCHANT_ID=your_merchant_id
QRIS_API_URL=https://api.qris-provider.com

# Database
DATABASE_URL=sqlite:///premium_sales.db

# Admin Settings
ADMIN_ID=your_telegram_id
```

## Usage

### Start the Bot

```bash
python main.py
```

### Commands

- `/start` - Show main menu
- `/packages` - View premium packages
- `/buy <package_id>` - Initiate purchase
- `/status` - Check order status
- `/admin` - Admin panel (admin only)

## License

MIT
