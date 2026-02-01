from aiogram import Router, F
from aiogram.types import Message

from keyboards.default.user import user_main_menu, courses_menu, contacts_menu

router = Router()

@router.message(F.text.in_(["🎓 Courses", "🎓 Kurslar", "🎓 Курсы"]))
async def courses_handler(message: Message, _):
    text = _("Select a course:")
    await message.answer(text, reply_markup=await courses_menu(_))

@router.message(F.text.in_(["🎉 Events", "🎉 Tadbirlar", "🎉 События"]))
async def events_handler(message: Message, _):
    text = _("Here are the upcoming events:")
    await message.answer(text)

@router.message(F.text.in_(["☎️ Contacts", "☎️ Aloqa", "☎️ Контакты"]))
async def contact_handler(message: Message, _):
    text = _("Select a branch:")
    await message.answer(text, reply_markup=await contacts_menu(_))

@router.message(F.text.in_(["⚙️ Settings", "⚙️ Sozlamalar", "⚙️ Настройки"]))
async def settings_handler(message: Message, _):
    text = _("Settings menu (coming soon)")
    await message.answer(text)

@router.message(F.text.in_(["⬅ Back", "⬅ Ortga", "⬅ Назад"]))
async def back_handler(message: Message, _):
    text = _("Main menu")
    await message.answer(text, reply_markup=await user_main_menu(_))

@router.message(F.text.in_(["🐍 Python Backend"]))
async def python_course_handler(message: Message, _):
    text = _("Python Backend Development course details...")
    await message.answer(text)

@router.message(F.text.in_(["🎨 UX/UI"]))
async def uxui_course_handler(message: Message, _):
    text = _("UX/UI Design course details...")
    await message.answer(text)

@router.message(F.text.in_(["📱 Android Dev"]))
async def android_course_handler(message: Message, _):
    text = _("Android Development course details...")
    await message.answer(text)

@router.message(F.text.in_(["💻 Frontend"]))
async def frontend_course_handler(message: Message, _):
    text = _("Frontend Development course details...")
    await message.answer(text)

@router.message(F.text.in_(["📍 Chilonzor Branch"]))
async def chilonzor_handler(message: Message, _):
    text = _("Chilonzor Branch\nAddress: ...")
    await message.answer(text)

@router.message(F.text.in_(["📍 Xadra Branch"]))
async def xadra_handler(message: Message, _):
    text = _("Xadra Branch\nAddress: ...")
    await message.answer(text)

@router.message(F.text.in_(["📍 Oybek Branch"]))
async def oybek_handler(message: Message, _):
    text = _("Oybek Branch\nAddress: ...")
    await message.answer(text)