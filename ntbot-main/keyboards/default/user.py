from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

share_contact = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="☎️ Share phone number", request_contact=True)
    ]], resize_keyboard=True
)

share_location = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="📍 Share my location", request_location=True)
    ]], resize_keyboard=True
)

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎓 Courses"),
            KeyboardButton(text="🎉 Events"),
        ],
        [
            KeyboardButton(text="☎️ Contacts"),
            KeyboardButton(text="⚙️ Settings"),
        ]
    ], resize_keyboard=True
)


courses_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🐍 Python Backend"),KeyboardButton(text="🎨 UX/UI")],
        [KeyboardButton(text="📱 Android Dev"), KeyboardButton(text="💻 Frontend")],
        [KeyboardButton(text="⬅ Back")]
    ],
    resize_keyboard=True
)

contacts_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Chilonzor Branch"), KeyboardButton(text="📍 Xadra Branch")],
        [KeyboardButton(text="📍 Oybek Branch")],
        [KeyboardButton(text="⬅ Back")]
    ],
    resize_keyboard=True
)