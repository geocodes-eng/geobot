import gradio as gr
import re
from transformers import pipeline
from query import get_liquefaction_at_point

# Load Qwen model pipeline
pipe = pipeline("text-generation", model="Qwen/Qwen3-0.6B")

def extract_coordinates(user_input):
    """Extract coordinates from user input using regex"""
    # Look for patterns like "1511300, 5266130" or "x: 1511300, y: 5266130"
    patterns = [
        r'(\d{6,7})\s*,\s*(\d{6,7})',  # 1511300, 5266130
        r'x:\s*(\d{6,7})\s*,\s*y:\s*(\d{6,7})',  # x: 1511300, y: 5266130
        r'coordinates?\s*[:\-]?\s*(\d{6,7})\s*,\s*(\d{6,7})',  # coordinates: 1511300, 5266130
    ]
    
    for pattern in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            return x, y
    
    return None, None

def agent(user_input):
    # Try regex first (fast and reliable)
    x, y = extract_coordinates(user_input)
    
    # If regex fails, try LLM as fallback
    if x is None or y is None:
        try:
            llm_response = pipe(
                f"Extract NZTM coordinates from this text. Return only the numbers separated by comma: {user_input}",
                max_new_tokens=20,
                do_sample=False,
                temperature=0.1
            )[0]["generated_text"]
            
            # Parse LLM response for coordinates
            coords_match = re.search(r'(\d{6,7})\s*,\s*(\d{6,7})', llm_response)
            if coords_match:
                x, y = int(coords_match.group(1)), int(coords_match.group(2))
            else:
                return "Could not extract coordinates. Please provide coordinates in format like '1511300, 5266130' or 'x: 1511300, y: 5266130'"
        except:
            return "Could not extract coordinates. Please provide coordinates in format like '1511300, 5266130' or 'x: 1511300, y: 5266130'"
    
    try:
        result = get_liquefaction_at_point(x, y)
        return f"Coordinates: ({x}, {y})\nLiquefaction Susceptibility: {result}"
    except Exception as e:
        return f"Error getting liquefaction data: {e}"

def predict(prompt):
    # Use a simpler approach - just pass the prompt directly without messages format
    completion = pipe(prompt, max_new_tokens=100, do_sample=True, temperature=0.7)[0]["generated_text"]
    
    # Remove the original prompt from the response
    if prompt in completion:
        response = completion[len(prompt):].strip()
    else:
        response = completion
    
    # Clean up any formatting issues
    response = response.replace("\\n", "\n").replace("\\'", "'")
    return response

# Create a tabbed interface
with gr.Blocks(title="Geo Agent Demo") as iface:
    gr.Markdown("# Geo Agent Demo")
    gr.Markdown("Enter NZTM coordinates to get liquefaction susceptibility data. The agent uses a Hugging Face model to extract coordinates and queries the Canterbury Liquefaction Susceptibility ArcGIS MapServer.")
    
    with gr.Tab("Coordinate Analysis"):
        coord_input = gr.Textbox(lines=2, label="Enter coordinates (e.g., '1511300, 5266130' or 'x: 1511300, y: 5266130')")
        coord_output = gr.Textbox(label="Liquefaction Susceptibility Result", lines=4)
        coord_button = gr.Button("Analyze Coordinates", variant="primary")
        coord_button.click(fn=agent, inputs=coord_input, outputs=coord_output)
        
        # Add example inputs
        gr.Examples(
            examples=[
                ["1511300, 5266130"],
                ["x: 1511300, y: 5266130"],
                ["What's the liquefaction at coordinates 1511300, 5266130?"],
                ["Can you check 1511300, 5266130 for me?"]
            ],
            inputs=coord_input
        )
    
    with gr.Tab("Chat Assistant"):
        chat_input = gr.Textbox(label="Type your message here:", placeholder="Hello, how can you help me?", lines=2)
        chat_output = gr.Textbox(label="AI Response", lines=6)
        chat_button = gr.Button("Send Message", variant="primary")
        chat_button.click(fn=predict, inputs=chat_input, outputs=chat_output)
        
        # Add example chat messages
        gr.Examples(
            examples=[
                ["Hello, what can you help me with?"],
                ["What is liquefaction susceptibility?"],
                ["How do I use this application?"],
                ["Tell me a joke"]
            ],
            inputs=chat_input
        )

if __name__ == "__main__":
    iface.launch(
        server_name="0.0.0.0",  # Allow external connections
        server_port=7860,       # Standard Gradio port
        share=False,            # Set to True if you want a public link
        show_error=True,        # Show detailed errors
        quiet=False             # Show startup messages
    ) 