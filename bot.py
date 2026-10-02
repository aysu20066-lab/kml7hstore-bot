import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 8406214575

logging.basicConfig(level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 المتجر", callback_data="store")],
        [InlineKeyboardButton("📦 طلباتي", callback_data="orders")],
        [InlineKeyboardButton("📞 الدعم", callback_data="support")],
    ]

    if update.effective_user.id == ADMIN_ID:
        keyboard.append(
            [InlineKeyboardButton("⚙️ إدارة المتجر", callback_data="admin")]
        )

    await update.message.reply_text(
        "مرحباً بك في 🏪 متجر حلب\n\n"
        "شحن ألعاب ورصيد موبايل بسرعة وأمان.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "store":
        keyboard = [
            [InlineKeyboardButton("🎮 Free Fire", callback_data="freefire")],
            [InlineKeyboardButton("🎮 PUBG Mobile", callback_data="pubg")],
            [InlineKeyboardButton("🎮 Blood Strike", callback_data="bloodstrike")],
            [InlineKeyboardButton("🎮 Jawaker", callback_data="jawaker")],
            [InlineKeyboardButton("📱 MTN", callback_data="mtn")],
            [InlineKeyboardButton("📱 Syriatel", callback_data="syriatel")],
            [InlineKeyboardButton("🔙 رجوع", callback_data="back")],
        ]

        await query.edit_message_text(
            "🛒 اختر القسم:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "freefire":
        await query.edit_message_text(
            "🔥 Free Fire\n\n"
            "💎 110 جوهرة — 140 ل.س\n"
            "💎 210 + 21 — 280 ل.س\n"
            "💎 530 + 53 — 680 ل.س\n"
            "💎 1080 + 108 — 1360 ل.س\n"
            "💎 2200 + 220 — 2720 ل.س\n\n"
            "سيتم إضافة الطلبات والدفع في الخطوة التالية."
        )

    elif query.data == "pubg":
        await query.edit_message_text("🎮 PUBG Mobile\n\nسيتم إضافة الباقات قريباً.")

    elif query.data == "bloodstrike":
        await query.edit_message_text("🎮 Blood Strike\n\nسيتم إضافة الباقات قريباً.")

    elif query.data == "jawaker":
        await query.edit_message_text("🎮 Jawaker\n\nسيتم إضافة الباقات قريباً.")

    elif query.data == "mtn":
        await query.edit_message_text("📱 MTN Syria\n\nسيتم إضافة الباقات قريباً.")

    elif query.data == "syriatel":
        await query.edit_message_text("📱 Syriatel\n\nسيتم إضافة الباقات قريباً.")

    elif query.data == "orders":
        await query.edit_message_text("📦 لا توجد طلبات حالياً.")

    elif query.data == "support":
        await query.edit_message_text(
            "📞 الدعم\n\n"
            "واتساب: +963995751695\n\n"
            "متجر حلب — بإدارة أحمد ومحمد"
        )

    elif query.data == "admin":
        if update.effective_user.id != ADMIN_ID:
            return

        keyboard = [
            [InlineKeyboardButton("➕ إضافة منتج", callback_data="add_product")],
            [InlineKeyboardButton("🛍️ المنتجات", callback_data="products")],
            [InlineKeyboardButton("📋 الطلبات", callback_data="admin_orders")],
            [InlineKeyboardButton("💳 الدفع", callback_data="payment")],
        ]

        await query.edit_message_text(
            "⚙️ لوحة إدارة متجر حلب",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "add_product":
        await query.edit_message_text(
            "➕ إضافة منتج\n\n"
            "هذه الوظيفة سنبرمجها في الخطوة التالية."
        )

    elif query.data == "products":
        await query.edit_message_text("🛍️ إدارة المنتجات\n\nسنضيف المنتجات هنا.")

    elif query.data == "admin_orders":
        await query.edit_message_text("📋 الطلبات\n\nلا توجد طلبات حالياً.")

    elif query.data == "payment":
        await query.edit_message_text(
            "💳 الدفع\n\n"
            "طريقة الدفع: Sham Cash\n"
            "سيتم إضافة رقم التحويل وإثبات الدفع لاحقاً."
        )

    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("🛒 المتجر", callback_data="store")],
            [InlineKeyboardButton("📦 طلباتي", callback_data="orders")],
            [InlineKeyboardButton("📞 الدعم", callback_data="support")],
        ]

        if update.effective_user.id == ADMIN_ID:
            keyboard.append(
                [InlineKeyboardButton("⚙️ إدارة المتجر", callback_data="admin")]
            )

        await query.edit_message_text(
            "🏪 متجر حلب",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN غير موجود")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
