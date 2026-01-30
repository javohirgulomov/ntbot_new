from aiogram import Router, F, types
from keyboards.default.menu import courses_menu, contacts_menu, main_menu

router = Router()


@router.message(F.text == "📚 Courses")
async def show_courses_menu(message: types.Message):
    await message.answer("Select a course to learn more:", reply_markup=courses_menu)

@router.message(F.text == "📞 Contacts")
async def show_contacts_menu(message: types.Message):
    await message.answer("Select a branch for contact info:", reply_markup=contacts_menu)

@router.message(F.text == "🔙 Back to Main Menu")
async def go_back_main(message: types.Message):
    await message.answer("Main Menu:", reply_markup=main_menu)


@router.message(F.text == "📱 Frontend Development")
async def frontend_info(message: types.Message):
    await message.answer("<b>📱 Frontend Development</b>\n\nLearn React, HTML, CSS, and JavaScript.", parse_mode="HTML")

@router.message(F.text == "💻 Backend Development")
async def backend_info(message: types.Message):
    await message.answer("<b>💻 Backend Development</b>\n\nLearn Python, Django, FastAPI, and PostgreSQL.", parse_mode="HTML")

@router.message(F.text == "🎨 Graphic Design")
async def design_info(message: types.Message):
    await message.answer("<b>🎨 Graphic Design</b>\n\nLearn Figma, Photoshop, and UI/UX principles.", parse_mode="HTML")


@router.message(F.text == "📍 Chilonzor")
async def chilonzor_contact(message: types.Message):
    await message.answer("📞 <b>Chilonzor Branch:</b>\n+998 71 200 11 22", parse_mode="HTML")

@router.message(F.text == "📍 Xadra")
async def xadra_contact(message: types.Message):
    await message.answer("📞 <b>Xadra Branch:</b>\n+998 71 200 33 44", parse_mode="HTML")

@router.message(F.text == "📍 Olmazor")
async def olmazor_contact(message: types.Message):
    await message.answer("📞 <b>Olmazor Branch:</b>\n+998 71 200 55 66", parse_mode="HTML")

