import streamlit as st


def login(
        signup_code: int = 0
):
    name = st.text_input(label='Type your username:', key=f'signup{signup_code}').capitalize().strip()

    if st.button('Log-in'):
        if not name in signed_users:
            signed_users.append(name)
            st.session_state['user'] = name
        else:
            st.error('This name already is signed. Try other!')
            signup_code += 1


@st.cache_resource
def get_message_list():
    return []


@st.cache_resource
def get_signed_users():
    return []


@st.fragment(run_every=0.5)
def show_chat():
    global message_list

    message_list = get_message_list()
    try:
        for mss in message_list:
            st.chat_message(avatar=None, name=mss['name'], width='content').write(mss['content'])
    except:
        return


def main():
    global signed_users

    if not 'user' in st.session_state:
        signed_users = get_signed_users()
        login()
    else:
        st.set_page_config(page_title='Web Zap', page_icon='💬')
        st.title('Web Zap 💬')
        st.write(f'Welcome, {st.session_state['user']}!')

        message = st.chat_input('Type your message:')

        if message:
            user_message_dict = {
                'name': st.session_state['user'],
                'content': f'({st.session_state['user']}) {message}'
            }

            show_chat()

            message_list.append(user_message_dict)


if __name__=='__main__':
    main()