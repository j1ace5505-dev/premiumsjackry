#!/usr/bin/env python3
"""
Premium Sales Jackry - Telegram Auto Order Bot
Main entry point
"""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config.settings import settings

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class PremiumBot:
    def __init__(self):
        self.token = settings.TELEGRAM_BOT_TOKEN
        self.admin_id = settings.ADMIN_ID
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Start command handler"""
        user = update.effective_user
        welcome_text = f"🎉 Welcome {user.first_name}!\n\nI'm your Premium Sales Bot. Choose an option:\n\n📦 /packages - View premium packages\n💳 /buy - Purchase premium access\n📊 /status - Check your subscription status\n❓ /help - Get help"
        await update.message.reply_text(welcome_text)
    
    async def packages(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Show available packages"""
        packages_text = """📦 **Available Premium Packages:**

1️⃣ **Basic** - Rp 50.000 / 30 days
   - Basic features
   - Email support
   
2️⃣ **Pro** - Rp 150.000 / 90 days
   - All Basic features
   - Priority support
   - Advanced analytics
   
3️⃣ **Enterprise** - Rp 500.000 / 365 days
   - All Pro features
   - 24/7 support
   - Custom integrations
   
/buy to purchase
        """
        await update.message.reply_text(packages_text, parse_mode='Markdown')
    
    async def buy(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Initiate purchase"""
        text = "💳 Select package to purchase:\n/buy_basic\n/buy_pro\n/buy_enterprise"
        await update.message.reply_text(text)
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Help command"""
        help_text = """❓ **Help & Support**

/start - Show welcome message
/packages - View available packages
/buy - Purchase premium access
/status - Check your subscription
/help - Show this help message

💬 Need support? Contact @support
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Log errors"""
        logger.error(f"Update {update} caused error {context.error}")
    
    def run(self):
        """Start the bot"""
        if not self.token:
            raise ValueError("TELEGRAM_BOT_TOKEN not set in environment variables")
        
        app = Application.builder().token(self.token).build()
        
        # Commands
        app.add_handler(CommandHandler('start', self.start))
        app.add_handler(CommandHandler('packages', self.packages))
        app.add_handler(CommandHandler('buy', self.buy))
        app.add_handler(CommandHandler('help', self.help))
        
        # Error handler
        app.add_error_handler(self.error_handler)
        
        logger.info("🤖 Bot started. Polling for messages...")
        app.run_polling()

if __name__ == '__main__':
    bot = PremiumBot()
    bot.run()
