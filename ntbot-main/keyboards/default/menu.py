from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu(_):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("🎓 Courses")), KeyboardButton(text=_("🎉 Events"))],
            [KeyboardButton(text=_("☎ Contacts")), KeyboardButton(text=_("⚙ Settings"))],
        ],
        resize_keyboard=True
    )

def get_courses_menu(_):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("📱 Frontend Development")), KeyboardButton(text=_("💻 Backend Development"))],
            [KeyboardButton(text=_("🎨 Graphic Design")), KeyboardButton(text=_("🔙 Back to Main Menu"))]
        ],
        resize_keyboard=True
    )

def get_contacts_menu(_):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("📍 Chilonzor")), KeyboardButton(text=_("📍 Xadra"))],
            [KeyboardButton(text=_("📍 Olmazor")), KeyboardButton(text=_("🔙 Back to Main Menu"))]
        ],
        resize_keyboard=True
    )