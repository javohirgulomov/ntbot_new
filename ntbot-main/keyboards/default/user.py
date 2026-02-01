from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def share_contact(_):
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=_("☎️ Share phone number"), request_contact=True)
        ]], resize_keyboard=True
    )

async def share_location(_):
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=_("📍 Share my location"), request_location=True)
        ]], resize_keyboard=True
    )

async def user_main_menu(_):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("🎓 Courses")),
                KeyboardButton(text=_("🎉 Events")),
            ],
            [
                KeyboardButton(text=_("☎️ Contacts")),
                KeyboardButton(text=_("⚙️ Settings")),
            ]
        ], resize_keyboard=True
    )

async def courses_menu(_):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("🐍 Python Backend")), KeyboardButton(text=_("🎨 UX/UI"))],
            [KeyboardButton(text=_("📱 Android Dev")), KeyboardButton(text=_("💻 Frontend"))],
            [KeyboardButton(text=_("⬅ Back"))]
        ],
        resize_keyboard=True
    )

async def contacts_menu(_):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("📍 Chilonzor Branch")), KeyboardButton(text=_("📍 Xadra Branch"))],
            [KeyboardButton(text=_("📍 Oybek Branch"))],
            [KeyboardButton(text=_("⬅ Back"))]
        ],
        resize_keyboard=True
    )