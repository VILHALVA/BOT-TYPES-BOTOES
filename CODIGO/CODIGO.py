import telebot
from telebot import types
from TOKEN import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    btn_alert = types.InlineKeyboardButton("Exibir Alerta", callback_data="alert")
    btn_notification = types.InlineKeyboardButton("Exibir Notificação", callback_data="notification")
    btn_message = types.InlineKeyboardButton("Enviar Mensagem Regular", callback_data="send_message")
    btn_markdown = types.InlineKeyboardButton("Mensagem com Markdown/HTML", callback_data="send_formatted_message")
    btn_edit_message = types.InlineKeyboardButton("Editar Mensagem", callback_data="edit_message")
    btn_change_buttons = types.InlineKeyboardButton("Mudar Botões", callback_data="change_buttons")
    btn_link = types.InlineKeyboardButton("Abrir Link Externo", url="https://exemplo.com")

    markup.add(btn_message, btn_markdown, btn_edit_message)
    markup.add(btn_change_buttons, btn_link)

    bot.send_message(message.chat.id, "Escolha uma ação:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "alert":
        bot.answer_callback_query(call.id, "Este é um alerta!", show_alert=True)

    elif call.data == "notification":
        bot.answer_callback_query(call.id, "Notificação rápida!", show_alert=False)

    elif call.data == "send_message":
        bot.send_message(call.message.chat.id, "Esta é uma mensagem regular enviada após clicar no botão.")

    elif call.data == "send_formatted_message":
        bot.send_message(call.message.chat.id, "<b>Mensagem em negrito!</b> Aqui está o link: <a href='https://exemplo.com'>Clique aqui</a>", parse_mode="HTML")

    elif call.data == "edit_message":
        bot.edit_message_text("A mensagem foi alterada!", chat_id=call.message.chat.id, message_id=call.message.message_id)

    elif call.data == "change_buttons":
        new_markup = types.InlineKeyboardMarkup()
        new_button = types.InlineKeyboardButton("Novo Botão", callback_data="new_action")
        new_markup.add(new_button)
        bot.edit_message_text("Os botões foram alterados!", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=new_markup)

bot.polling()
