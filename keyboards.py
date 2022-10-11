from tkinter import Menu
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

#Главное меню
menu = KeyboardButton("Меню")
buy = KeyboardButton("Корзина")
call = KeyboardButton("Связаться с администратором")
main_menu =  ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

main_menu.add(menu)
main_menu.row(
    buy, call
)
#############


rolls = KeyboardButton("Роллы")
sets = KeyboardButton("Сеты")
sushi = KeyboardButton("Суши")
lapsha = KeyboardButton("Лапша")
shaurma = KeyboardButton("Шаурма")
supi = KeyboardButton("Супы")
back = KeyboardButton("Вернуться в главное меню")

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    rolls, sets, sushi,
)
menu_kb.row(
    lapsha, shaurma, supi
)
menu_kb.row(
    back
)


#Admin kb

add_menu = KeyboardButton("Добавить меню")
edit_menu = KeyboardButton("Редактировать меню")
admin_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(
    add_menu, edit_menu
)