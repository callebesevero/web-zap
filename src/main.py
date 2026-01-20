# https://docs.streamlit.io/develop/api-reference/user/st.login
# https://docs.streamlit.io/develop/api-reference/user/st.user
# https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state    
    # runner.enforceSerializableSessionState

from streamlit import chat_input, chat_message, session_state, set_page_config, title, cache_resource, fragment


@cache_resource
def list_init():
    return []


@fragment(run_every=0.5)
def show_chat():
    global message_list
    message_list = list_init()
    for mss in message_list:
        chat_message(avatar=mss['avatar'], name=mss['name'], width='content').write(mss['content'])


def main():
    set_page_config(page_title='Web Zap', page_icon='😁')
    title('Web Zap 😁')

    message = chat_input('Type your message:')

    if message:
        user_message_dict = {
            'avatar': 'user',
            'name': 'user',
            'content': message
        }

        show_chat()

        message_list.append(user_message_dict)

if __name__=='__main__':
    main()