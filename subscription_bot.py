import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ============================================
# КОНФИГУРАЦИЯ
# ============================================

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = '@autoimpulse_f'  # Ваш канал

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не установлен!")

# ============================================
# ЛОГИРОВАНИЕ
# ============================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================
# ИНИЦИАЛИЗАЦИЯ БОТА
# ============================================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ============================================
# ПРОВЕРКА ПОДПИСКИ
# ============================================

async def check_subscription(user_id: int) -> bool:
    """Проверяет, подписан ли пользователь на канал"""
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        logger.error(f"Ошибка проверки подписки: {e}")
        return False

# ============================================
# ПРОДОЛЖЕНИЕ СТАТЬИ (контент для подписчиков)
# ============================================

CONTINUATION_TEXT = """
🔥 **ПРОДОЛЖЕНИЕ: Lada Vesta NG — СРАВНЕНИЕ С КОНКУРЕНТАМИ**

📊 **СРАВНИТЕЛЬНАЯ ТАБЛИЦА**

Lada Vesta NG vs Конкуренты:

**Цена:**
• Vesta NG: 1.65 млн₽
• Solaris: 1.4 млн₽
• Tiggo 7: 2.4 млн₽

**Расход (город/трасса):**
• Vesta NG: 9.5 / 7.5 л
• Solaris: 8.5 / 6.5 л
• Tiggo 7: 10.5 / 8.5 л

**Клиренс:**
• Vesta NG: 178 мм ✅
• Solaris: 160 мм
• Tiggo 7: 190 мм

**Гарантия:**
• Vesta NG: 3 года
• Solaris: 5 лет ✅
• Tiggo 7: 5 лет ✅

**ТО за 5 лет:**
• Vesta NG: 250 тыс₽
• Solaris: 200 тыс₽ ✅
• Tiggo 7: 300 тыс₽

**Ликвидность:**
• Vesta NG: 60%
• Solaris: 70% ✅
• Tiggo 7: 65%

━━━━━━━━━━━━━━━━━━━

💡 **ВЫВОД:**
• Vesta дешевле, но больше расход
• Solaris экономичнее на 468 000₽ за 5 лет
• Tiggo комфортнее, но дороже на 800 000₽

━━━━━━━━━━━━━━━━━━━

📋 **ЧЕК-ЛИСТ: Как проверить Vesta NG**

✅ **Двигатель:**
• Запустить холодный — не должно быть стука
• Проверить уровень масла
• Прогреть — не должно быть сизого дыма

✅ **Вариатор:**
• Переключения должны быть плавными
• Не должно быть пинков
• Проверить уровень жидкости CVT

✅ **Подвеска:**
• Прокатиться по лежачим полицейским
• Не должно быть стуков
• Проверить сайлентблоки

✅ **Кузов:**
• Проверить зазоры (должны быть ровные)
• Осмотреть на предмет коррозии
• Проверить работу всех дверей

✅ **Электроника:**
• Проверить мультимедиа (не глючит ли)
• Протестировать все стеклоподъемники
• Проверить климат-контроль

✅ **Документы:**
• Сервисная книжка (все ТО вовремя?)
• Гарантия (не истекла?)
• Количество владельцев

━━━━━━━━━━━━━━━━━━━

💰 **РЕАЛЬНАЯ СТОИМОСТЬ ВЛАДЕНИЯ (5 лет)**

**Lada Vesta NG:**
• Покупка: 1 650 000₽
• Бензин: 540 000₽
• ТО: 250 000₽
• Страховка: 60 000₽
• Налог: 15 000₽
• Потеря стоимости: 660 000₽
**ИТОГО: 3 175 000₽**

**Hyundai Solaris:**
• Покупка: 1 400 000₽
• Бензин: 480 000₽
• ТО: 200 000₽
• Страховка: 55 000₽
• Налог: 12 000₽
• Потеря стоимости: 560 000₽
**ИТОГО: 2 707 000₽**

**Chery Tiggo 7:**
• Покупка: 2 400 000₽
• Бензин: 570 000₽
• ТО: 300 000₽
• Страховка: 70 000₽
• Налог: 18 000₽
• Потеря стоимости: 960 000₽
**ИТОГО: 4 318 000₽**

🎯 **ВЫВОД:**
Vesta дешевле Solaris только на первый взгляд. 
За 5 лет Solaris сэкономит вам **468 000₽**!

━━━━━━━━━━━━━━━━━━━

📱 **Подписывайтесь на канал**, 
чтобы не пропустить следующие обзоры!

👉 t.me/autoimpulse_f
"""

# ============================================
# ОБРАБОТЧИК /start
# ============================================

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    
    logger.info(f"Пользователь {username} ({user_id}) нажал /start")
    
    # Проверяем подписку
    is_subscribed = await check_subscription(user_id)
    
    if is_subscribed:
        # Пользователь подписан — отправляем продолжение
        await message.answer(
            "✅ **Отлично! Вы подписаны!**\n\n"
            "Отправляю продолжение статьи...",
            parse_mode='Markdown'
        )
        await message.answer(CONTINUATION_TEXT, parse_mode='Markdown')
        
        logger.info(f"✅ Отправлено продолжение пользователю {username}")
    else:
        # Пользователь НЕ подписан — просим подписаться
        builder = InlineKeyboardBuilder()
        builder.button(
            text="🔔 Подписаться на канал",
            url=f"https://t.me/{CHANNEL_ID.replace('@', '')}"
        )
        builder.button(
            text="✅ Я подписался",
            callback_data="check_subscription"
        )
        builder.adjust(1)
        
        await message.answer(
            "📱 **Чтобы получить продолжение статьи,**\n"
            "подпишитесь на наш Telegram-канал!\n\n"
            "Там я публикую:\n"
            "⚡ Эксклюзивные автоновости\n"
            "💰 Актуальные цены и аналитику\n"
            "🔍 Честные обзоры и тесты\n\n"
            "После подписки нажмите кнопку ниже 👇",
            reply_markup=builder.as_markup(),
            parse_mode='Markdown'
        )
        
        logger.info(f"⏳ Пользователь {username} не подписан")

# ============================================
# ОБРАБОТЧИК ПРОВЕРКИ ПОДПИСКИ
# ============================================

@dp.callback_query(lambda c: c.data == 'check_subscription')
async def process_check_subscription(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    username = callback_query.from_user.username or callback_query.from_user.first_name
    
    # Проверяем подписку
    is_subscribed = await check_subscription(user_id)
    
    if is_subscribed:
        # Пользователь подписался — отправляем продолжение
        await callback_query.message.answer(
            "✅ **Отлично! Подписка подтверждена!**\n\n"
            "Отправляю продолжение статьи...",
            parse_mode='Markdown'
        )
        await callback_query.message.answer(CONTINUATION_TEXT, parse_mode='Markdown')
        
        logger.info(f"✅ Пользователь {username} подписался и получил продолжение")
    else:
        # Пользователь всё ещё НЕ подписан
        await callback_query.message.answer(
            "⚠️ **Я всё ещё не вижу вашу подписку.**\n\n"
            "Пожалуйста:\n"
            "1. Нажмите кнопку 'Подписаться на канал'\n"
            "2. Подпишитесь на канал\n"
            "3. Вернитесь в бот и нажмите 'Я подписался'",
            parse_mode='Markdown'
        )
        
        logger.info(f"⚠️ Пользователь {username} всё ещё не подписался")
    
    await callback_query.answer()

# ============================================
# ЗАПУСК БОТА
# ============================================

async def main():
    logger.info("🤖 Бот запускается...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
