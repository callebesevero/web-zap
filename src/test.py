from streamlit import chat_input, chat_message, session_state, set_page_config, title

set_page_config(page_title='Web Zap', page_icon='😁')
title('Web Zap 😁')

if not 'message_list' in session_state:
    session_state['message_list'] = []

for mss in session_state['message_list']:
    chat_message(avatar=mss['avatar'], name=mss['name'], width='content').write(mss['content'])

message = chat_input('Type your message:')
if message:
    chat_message(name='user', avatar='user', width='content').write(message)
    user_message_dict = {
        'avatar': 'user',
        'name': 'user',
        'content': message
    }

    session_state['message_list'].append(user_message_dict)