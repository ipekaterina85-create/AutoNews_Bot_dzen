import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ============================================
# КОНФИГУРАЦИЯ
# ============================================

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID', '@autoimpulse_f')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен!")

# ============================================
# ЛОГИРОВАНИЕ
# ============================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================
# ИНИЦИАЛИЗАЦИЯ
# ============================================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ============================================
# ТЕКСТ СТАТЬИ ПРО LADA VESTA NG
# ============================================

VESTA_ARTICLE = """
🔥 ПРОДОЛЖЕНИЕ: Lada Vesta NG — СРАВНЕНИЕ С КОНКУРЕНТАМИ

📊 СРАВНИТЕЛЬНАЯ ТАБЛИЦА

ЦЕНА:
• Vesta NG: 1.65 млн₽
• Solaris: 1.4 млн₽
• Tiggo 7: 2.4 млн₽

РАСХОД (город/трасса):
• Vesta NG: 9.5 / 7.5 л
• Solaris: 8.5 / 6.5 л
• Tiggo 7: 10.5 / 8.5 л

КЛИРЕНС:
• Vesta NG: 178 мм ✅
• Solaris: 160 мм
• Tiggo 7: 190 мм

ГАРАНТИЯ:
• Vesta NG: 3 года
• Solaris: 5 лет ✅
• Tiggo 7: 5 лет ✅

ТО ЗА 5 ЛЕТ:
• Vesta NG: 250 тыс₽
• Solaris: 200 тыс₽ ✅
• Tiggo 7: 300 тыс₽

ЛИКВИДНОСТЬ:
• Vesta NG: 60%
• Solaris: 70% ✅
• Tiggo 7: 65%

💡 ВЫВОД:
• Vesta дешевле, но больше расход
• Solaris экономичнее на 468 000₽ за 5 лет
• Tiggo комфортнее, но дороже на 800 000₽

━━━━━━━━━━━━━━━━━━━

📋 ЧЕК-ЛИСТ: Как проверить Vesta NG

ДВИГАТЕЛЬ:
✓ Запустить холодный — не должно быть стука
✓ Проверить уровень масла
✓ Прогреть — не должно быть дыма

ВАРИАТОР:
✓ Переключения должны быть плавными
✓ Не должно быть пинков
✓ Проверить уровень жидкости

ПОДВЕСКА:
✓ Прокатиться по неровностям
✓ Не должно быть стуков
✓ Проверить сайлентблоки

КУЗОВ:
✓ Проверить зазоры
✓ Осмотреть на коррозию
✓ Проверить работу дверей

ЭЛЕКТРОНИКА:
✓ Проверить мультимедиа
✓ Протестировать стеклоподъемники
✓ Проверить климат-контроль

ДОКУМЕНТЫ:
✓ Сервисная книжка
✓ Гарантия
✓ Количество владельцев

━━━━━━━━━━━━━━━━━━━

💰 СТОИМОСТЬ ВЛАДЕНИЯ (5 лет)

Lada Vesta NG: 3 175 000₽
Hyundai Solaris: 2 707 000₽
Chery Tiggo 7: 4 318 000₽

🎯 ВЫВОД:
Vesta дешевле только на первый взгляд!
Solaris сэкономит 468 000₽ за 5 лет!

━━━━━━━━━━━━━━━━━━━

📱 Подписывайтесь на канал: t.me/autoimpulse_f
"""

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
# /start — ГЛАВНЫЙ ОБРАБОТЧИК
# ============================================

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    
    logger.info(f"Пользователь {username} ({user_id}) открыл бота")
    
    # Проверяем подписку
    is_subscribed = await check_subscription(user_id)
    
    if is_subscribed:
        # Подписан — сразу отправляем статью
        await message.answer("✅ Отлично! Вы подписаны!\n\nОтправляю продолжение статьи про Lada Vesta NG...")
        await message.answer(VESTA_ARTICLE)
        logger.info(f"✅ Отправлено продолжение пользователю {username}")
    else:
        # Не подписан — просим подписаться
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="🔔 Подписаться на канал", 
                url=f"https://t.me/{CHANNEL_ID.replace('@', '')}"
            )],
            [InlineKeyboardButton(
                text="✅ Я подписался", 
                callback_data="check_subscription"
            )]
        ])
        
        await message.answer(
            "📱 Чтобы получить продолжение статьи\n"
            "про Lada Vesta NG,\n\n"
            "подпишитесь на наш канал!\n\n"
            "Там я публикую:\n"
            "⚡ Эксклюзивные автоновости\n"
            "💰 Актуальные цены и аналитику\n"
            "🔍 Честные обзоры и тесты\n\n"
            "После подписки нажмите кнопку ниже 👇",
            reply_markup=keyboard
        )
        logger.info(f"⏳ {username} не подписан")

# ============================================
# ПРОВЕРКА ПОДПИСКИ (кнопка "Я подписался")
# ============================================

@dp.callback_query(lambda c: c.data == 'check_subscription')
async def check_subscription_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    username = callback_query.from_user.username or callback_query.from_user.first_name
    
    is_subscribed = await check_subscription(user_id)
    
    if is_subscribed:
        await callback_query.message.answer("✅ Подписка подтверждена!\n\nОтправляю продолжение...")
        await callback_query.message.answer(VESTA_ARTICLE)
        logger.info(f"✅ {username} подписался и получил статью")
    else:
        await callback_query.answer("⚠️ Я всё ещё не вижу подписку!", show_alert=True)
        logger.info(f"⚠️ {username} всё ещё не подписался")

# ============================================
# ЗАПУСК
# ============================================

async def main():
    logger.info("🤖 Бот запускается...")
    logger.info(f"📚 Статья: Lada Vesta NG")
    logger.info(f"🔗 Ссылка: t.me/autoimpulse_news_bot?start=vesta")
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
