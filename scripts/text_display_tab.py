import gradio as gr
from modules import script_callbacks

# Debug message to indicate the script has started loading
print("[DEBUG] Loading my_basic_tab.py script...")

def render_my_tab():
    print("[DEBUG] Inside render_my_tab function")
    
    # Define the content of the new tab using Gradio Blocks
    with gr.Blocks() as my_tab:
        with gr.Column():
            gr.Markdown("""
            ## 2.0 MP (Flux maximum)
            
            - 1:1 exact 1448 x 1448, rounded 1408 x 1408
            - 3:2 exact 1773 x 1182, rounded 1728 x 1152
            - 4:3 exact 1672 x 1254, rounded 1664 x 1216
            - 16:9 exact 1936 x 1089, rounded 1920 x 1088
            - 21:9 exact 2212 x 948, rounded 2176 x 960
            
            ## 1.0 MP (SDXL recommended)
            
            I ended up with familiar numbers I've used with SDXL, which gives me confidence in the calculations.
            
            - 1:1 exact 1024 x 1024
            - 3:2 exact 1254 x 836, rounded 1216 x 832
            - 4:3 exact 1182 x 887, rounded 1152 x 896
            - 16:9 exact 1365 x 768, rounded 1344 x 768
            - 21:9 exact 1564 x 670, rounded 1536 x 640
            
            ## 0.1 MP (Flux minimum)
            """)

    # Return in the tuple format expected by Forge UI
    result = (my_tab, "My Basic Tab", "my_basic_tab")
    print(f"[DEBUG] Returning tuple: {result}")
    return [(my_tab, "My Basic Tab", "my_basic_tab")]

# Debug message before registering the callback
print("[DEBUG] Registering the on_ui_tabs callback")

# Register the callback to add the new tab
try:
    script_callbacks.on_ui_tabs(render_my_tab)
    print("[DEBUG] Successfully registered on_ui_tabs callback")
except AttributeError as e:
    print(f"[ERROR] Failed to register on_ui_tabs callback: {e}")
except Exception as e:
    print(f"[ERROR] An unexpected error occurred while registering callback: {e}")
