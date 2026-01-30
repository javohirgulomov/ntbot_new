from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Courses")],
        [KeyboardButton(text="📞 Contacts"), KeyboardButton(text="🎉 Events")],
        [KeyboardButton(text="⚙️ Settings")]
    ],
    resize_keyboard=True
)

courses_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Frontend Development")],
        [KeyboardButton(text="💻 Backend Development")],
        [KeyboardButton(text="🎨 Graphic Design")],
        [KeyboardButton(text="🔙 Back to Main Menu")]
    ],
    resize_keyboard=True
)

contacts_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Chilonzor")],
        [KeyboardButton(text="📍 Xadra")],
        [KeyboardButton(text="📍 Olmazor")],
        [KeyboardButton(text="🔙 Back to Main Menu")]
    ],
    resize_keyboard=True
)