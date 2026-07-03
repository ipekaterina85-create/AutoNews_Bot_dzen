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
# БАЗА ДАННЫХ СТАТЕЙ (2 статьи)
# ============================================

ARTICLES = {
    'vesta': {
        'title': '🚗 Lada Vesta NG — сравнение с конкурентами',
        'text': """
🔥 ПРОДОЛЖЕНИЕ: Lada Vesta NG — СРАВНЕНИЕ С КОНКУРЕНТАМИ

 СРАВНИТЕЛЬНАЯ ТАБЛИЦА

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

 ВЫВОД:
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

 ВЫВОД:
Vesta дешевле только на первый взгляд!
Solaris сэкономит 468 000₽ за 5 лет!

━━━━━━━━━━━━━━━━━━━

📱 Подписывайтесь: t.me/autoimpulse_f
"""
    },
    
    'util': {
        'title': '💰 Утильсбор 2026 — полный разбор',
        'text': """
🔥 ПРОДОЛЖЕНИЕ: Утильсбор 2026 — ПОЛНЫЙ РАЗБОР

📊 ТАБЛИЦА ПОДОРОЖАНИЯ (до и после 1.10.2026)

Lada Vesta (1.6 л, 106 л.с.):
• До 1.10: 5 200₽
• После 1.10: 5 200₽
• Рост: 0₽ (не меняется!)

Hyundai Solaris (1.6 л, 123 л.с.):
• До 1.10: 326 000₽
• После 1.10: 780 000₽
• Рост: +454 000₽

Kia Rio (1.6 л, 123 л.с.):
• До 1.10: 326 000₽
• После 1.10: 780 000₽
• Рост: +454 000₽

Chery Tiggo 7 (1.5 л, 147 л.с.):
• До 1.10: 326 000₽
• После 1.10: 850 000₽
• Рост: +524 000₽

Haval Jolion (1.5 л, 150 л.с.):
• До 1.10: 326 000₽
• После 1.10: 820 000₽
• Рост: +494 000₽

Geely Coolray (1.5 л, 150 л.с.):
• До 1.10: 326 000₽
• После 1.10: 800 000₽
• Рост: +474 000₽

Toyota Camry (2.5 л, 200 л.с.):
• До 1.10: 520 000₽
• После 1.10: 1 300 000₽
• Рост: +780 000₽

Toyota RAV4 (2.0 л, 149 л.с.):
• До 1.10: 520 000₽
• После 1.10: 1 250 000₽
• Рост: +730 000₽

Mazda CX-5 (2.5 л, 194 л.с.):
• До 1.10: 520 000₽
• После 1.10: 1 280 000₽
• Рост: +760 000₽

BMW X5 (3.0 л, 340 л.с.):
• До 1.10: 780 000₽
• После 1.10: 1 950 000₽
• Рост: +1 170 000₽

Mercedes GLE (3.0 л, 367 л.с.):
• До 1.10: 780 000₽
• После 1.10: 1 900 000₽
• Рост: +1 120 000₽

ЭЛЕКТРОМОБИЛИ (льготы до 2030):
• Tesla Model 3: 5 200₽ (рост 0₽)
• BYD Han: 5 200₽ (рост 0₽)
• Zeekr 001: 5 200₽ (рост 0₽)

━━━━━━━━━━━━━━━━━━━

🎯 ПОШАГОВАЯ СТРАТЕГИЯ ПОКУПКИ

ШАГ 1: Определитесь с бюджетом (1-2 дня)
ШАГ 2: Выберите модель (2-3 дня)
ШАГ 3: Найдите дилера (3-5 дней)
ШАГ 4: Проверьте авто (1 день)
ШАГ 5: Оформите покупку (1 день)
ШАГ 6: Зарегистрируйте авто (1 день)

ИТОГО: 10-15 дней до покупки

━━━━━━━━━━━━━━━━━━━

💡 АЛЬТЕРНАТИВНЫЕ ВАРИАНТЫ

1. LADA (не подорожает)
   • Vesta: от 1.5 млн₽
   • Granta: от 1.1 млн₽
   • Niva Travel: от 1.3 млн₽

2. ЭЛЕКТРОМОБИЛИ (льготы до 2030)
   • Tesla Model 3: от 4.5 млн₽
   • BYD Han: от 3.8 млн₽
   • Утильсбор: всего 5 200₽

3. АВТО С ПРОБЕГОМ (до 3 лет)
   • Утильсбор уже заплачен
   • Цена ниже на 20-30%
   • Большой выбор

━━━━━━━━━━━━━━━━━━━

✅ ЧЕК-ЛИСТ ПРОВЕРКИ АВТО С ПРОБЕГОМ

ДОКУМЕНТЫ:
□ ПТС (оригинал)
□ СТС
□ Диагностическая карта
□ Полис ОСАГО

ВНЕШНИЙ ОСМОТР:
□ Кузов без коррозии
□ Зазоры ровные
□ Краска без сколов
□ Шины с хорошим протектором

ДВИГАТЕЛЬ:
□ Запускается легко
□ Работает ровно
□ Нет посторонних звуков
□ Нет подтёков масла

КОРОБКА ПЕРЕДАЧ:
□ Переключается плавно
□ Нет рывков
□ Нет посторонних звуков

ПОДВЕСКА:
□ Нет стуков
□ Амортизаторы исправны
□ Сайлентблоки целые

ТЕСТ-ДРАЙВ:
□ Разгон нормальный
□ Тормоза эффективные
□ Рулевое управление чёткое
□ Нет вибраций

━━━━━━━━━━━━━━━━━━━

🔮 ПРОГНОЗ ЦЕН НА 2027 ГОД

РЕАЛИСТИЧНЫЙ СЦЕНАРИЙ (вероятность 50%):
• Утильсбор повысят ещё на 20-30%
• Цены вырастут на 10-15%
• Китайские авто займут 70% рынка
• Lada сохранит позиции

ПЕССИМИСТИЧНЫЙ СЦЕНАРИЙ (вероятность 20%):
• Утильсбор повысят на 50-100%
• Цены вырастут на 30-50%
• Параллельный импорт закроют
• Выбор авто резко сократится

ВЫВОД:
Лучшее время для покупки — СЕЙЧАС!

━━━━━━━━━━━━━━━━━━━

💰 ГЛАВНЫЕ СОВЕТЫ

1. НЕ ОТКЛАДЫВАЙТЕ ПОКУПКУ
   • Каждый день = потеря денег
   • С 1 октября цены вырастут
   • Действуйте сейчас!

2. ТОРГУЙТЕСЬ
   • Дилеры готовы давать скидки
   • Можно сэкономить 5-15%
   • Не бойтесь просить скидку

3. ПРОВЕРЯЙТЕ АВТО
   • Особенно с пробегом
   • Берите с собой эксперта
   • Не экономьте на проверке

4. УЧИТЫВАЙТЕ ВСЕ РАСХОДЫ
   • Страховка: 50-100 тыс₽
   • Регистрация: 5-10 тыс₽
   • ТО: 10-30 тыс₽
   • Итого: +70-140 тыс₽

5. СЛЕДИТЕ ЗА НОВОСТЯМИ
   • Возможны изменения
   • Следите за официальными заявлениями
   • Будьте в курсе

━━━━━━━━━━━━━━━━━━━

📱 Подписывайтесь: t.me/autoimpulse_f

Там я публикую:
⚡ Эксклюзивные автоновости
💰 Актуальные цены и аналитику
🔍 Честные обзоры и тесты
🚨 Важную информацию для водителей
"""
    }
}

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
# ФУНКЦИЯ ОТПРАВКИ СТАТЬИ
# ============================================

async def send_article(message_or_callback, article_id: str, user_id: int, username: str):
    """Отправляет статью пользователю с проверкой подписки"""
    
    if article_id not in ARTICLES:
        error_msg = "❌ Статья не найдена. Доступные статьи:\n\n"
        for aid, adata in ARTICLES.items():
            error_msg += f"• {adata['title']}\n"
            error_msg += f"  Ссылка: t.me/autoimpulse_news_bot?start={aid}\n\n"
        
        if isinstance(message_or_callback, types.CallbackQuery):
            await message_or_callback.message.answer(error_msg)
            await message_or_callback.answer()
        else:
            await message_or_callback.answer(error_msg)
        return
    
    article = ARTICLES[article_id]
    is_subscribed = await check_subscription(user_id)
    
    if is_subscribed:
        # Подписан — сразу отправляем статью
        if isinstance(message_or_callback, types.CallbackQuery):
            await message_or_callback.message.answer(
                f"✅ {article['title']}\n\nОтправляю продолжение..."
            )
            await message_or_callback.message.answer(article['text'])
            await message_or_callback.answer()
        else:
            await message_or_callback.answer(
                f"✅ {article['title']}\n\nОтправляю продолжение..."
            )
            await message_or_callback.answer(article['text'])
        
        logger.info(f"✅ Отправлено {article_id} пользователю {username}")
    else:
        # Не подписан — просим подписаться
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="🔔 Подписаться на канал", 
                url=f"https://t.me/{CHANNEL_ID.replace('@', '')}"
            )],
            [InlineKeyboardButton(
                text="✅ Я подписался", 
                callback_data=f"check_{article_id}"
            )]
        ])
        
        text = (
            f"📱 Чтобы получить продолжение статьи\n"
            f"{article['title']},\n\n"
            f"подпишитесь на канал!\n\n"
            f"После подписки нажмите кнопку ниже 👇"
        )
        
        if isinstance(message_or_callback, types.CallbackQuery):
            await message_or_callback.message.answer(text, reply_markup=keyboard)
            await message_or_callback.answer()
        else:
            await message_or_callback.answer(text, reply_markup=keyboard)
        
        logger.info(f"⏳ {username} не подписан (статья: {article_id})")

# ============================================
# /start с аргументом (deep link)
# ============================================

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    
    # Проверяем, есть ли аргумент (например, "vesta" или "util")
    args = message.text.split()
    article_id = args[1] if len(args) > 1 else None
    
    logger.info(f"Пользователь {username} ({user_id}) открыл бота. Аргумент: {article_id}")
    
    if article_id and article_id in ARTICLES:
        # Есть аргумент — сразу отправляем статью
        await send_article(message, article_id, user_id, username)
    else:
        # Нет аргумента — показываем список статей
        articles_list = " ДОСТУПНЫЕ СТАТЬИ:\n\n"
        for aid, adata in ARTICLES.items():
            articles_list += f"• {adata['title']}\n"
            articles_list += f"  Ссылка: t.me/autoimpulse_news_bot?start={aid}\n\n"
        
        await message.answer(
            f"👋 Привет, {username}!\n\n"
            f"{articles_list}\n"
            "Нажмите на ссылку, чтобы получить продолжение!"
        )

# ============================================
# ПРОВЕРКА ПОДПИСКИ (кнопка "Я подписался")
# ============================================

@dp.callback_query(lambda c: c.data.startswith('check_'))
async def check_subscription_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    username = callback_query.from_user.username or callback_query.from_user.first_name
    article_id = callback_query.data.replace('check_', '')
    
    if article_id not in ARTICLES:
        await callback_query.answer("❌ Статья не найдена", show_alert=True)
        return
    
    article = ARTICLES[article_id]
    is_subscribed = await check_subscription(user_id)
    
    if is_subscribed:
        await callback_query.message.answer("✅ Подписка подтверждена!\n\nОтправляю продолжение...")
        await callback_query.message.answer(article['text'])
        logger.info(f"✅ {username} подписался и получил {article_id}")
    else:
        await callback_query.answer("⚠️ Я всё ещё не вижу подписку!", show_alert=True)
        logger.info(f"⚠️ {username} всё ещё не подписался")

# ============================================
# ЗАПУСК
# ============================================

async def main():
    logger.info("🤖 Бот запускается...")
    logger.info(f"📚 Загружено статей: {len(ARTICLES)}")
    for aid, adata in ARTICLES.items():
        logger.info(f"   • {aid}: {adata['title']}")
        logger.info(f"     Ссылка: t.me/autoimpulse_news_bot?start={aid}")
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
