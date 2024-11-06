import gradio as gr
from modules import script_callbacks

# Debug message to indicate the script has started loading
print("[DEBUG] Loading my_basic_tab.py script...")

def render_my_tab():
    print("[DEBUG] Inside render_my_tab function")
    
    # Define the content of the new tab
    try:
        with gr.Blocks() as my_tab:
            gr.Markdown("# Welcome to My Basic Extension")
            gr.Markdown("This is some sample text displayed on a new tab in Forge UI.")
        print("[DEBUG] Successfully created Gradio Blocks for the tab")
        return (my_tab, "My Basic Tab", "my_basic_tab")
    except Exception as e:
        print(f"[ERROR] An error occurred while rendering the tab: {e}")
        return None

# Debug message before registering the callback
print("[DEBUG] Registering the on_ui_tabs callback")

# Register the callback with the updated approach and handle any errors
try:
    script_callbacks.on_ui_tabs(render_my_tab)
    print("[DEBUG] Successfully registered on_ui_tabs callback")
except AttributeError as e:
    print(f"[ERROR] Failed to register on_ui_tabs callback: {e}")
except Exception as e:
    print(f"[ERROR] An unexpected error occurred while registering callback: {e}")
