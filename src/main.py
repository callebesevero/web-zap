import streamlit as st


def login():
    name = st.text_input(label='Type your username:', key='temp_user').capitalize().strip()

    if st.button('Log-in'):
        st.session_state['user'] = name


@st.cache_resource
def list_init():
    return []


@st.fragment(run_every=0.5)
def show_chat():
    global message_list
    message_list = list_init()
    for mss in message_list:
        st.chat_message(avatar=None, name=mss['name'], width='content').write(mss['content'])


def main():
    if not 'user' in st.session_state:
        login()
    else:
        st.set_page_config(page_title='Web Zap', page_icon='💬')
        st.title('Web Zap 💬')
        st.write(f'Welcome, {st.session_state['user']}!')

        message = st.chat_input('Type your message:')

        if message:
            user_message_dict = {
                'name': st.session_state['user'],
                'content': message
            }

            show_chat()

            message_list.append(user_message_dict)


if __name__=='__main__':
    main()