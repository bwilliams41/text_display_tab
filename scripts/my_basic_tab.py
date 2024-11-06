import gradio as gr
from modules import script_callbacks

def render_my_tab():
    # Define the content of the new tab
    with gr.Blocks() as my_tab:
        gr.Markdown("# Welcome to My Basic Extension")
        gr.Markdown("This is some sample text displayed on a new tab in Forge UI.")
    return my_tab

# Register the tab with Forge UI
def on_ui_tabs():
    script_callbacks.add_tab("My Basic Tab", render_my_tab, "my_basic_tab")

# Register the callback
script_callbacks.on_ui_tabs(on_ui_tabs)
