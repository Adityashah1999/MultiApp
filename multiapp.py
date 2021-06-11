"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st


class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar.radio(
        app = st.sidebar.subheader('Navigation Menu')
        app = st.sidebar.selectbox(
            'click on dropdown 👇 menu to navigate',
            self.apps,
            format_func=lambda app: app['title'])
        app['function']()
        st.sidebar.write("Check out the Covid-19 [Dashboard 📊](https://datastudio.google.com/u/0/reporting/986733a0-8433-4e18-bef0-491bcdee9cc5/page/doJLC)")



