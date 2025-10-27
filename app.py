import gradio as gr
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def chatbot_response(message, history, model, temp, max_tok):
    """Handle chatbot responses"""
    if model == "separator":
        return history, "Please select a valid model."
    
    # Add user message
    history.append({"role": "user", "content": message})
    
    # Simulate AI response (replace with actual model call)
    response = f"Model: {model}\nTemperature: {temp}\nMax Tokens: {max_tok}\n\n[This is a placeholder. Implement your model call here!]"
    history.append({"role": "assistant", "content": response})
    
    return history, ""

def process_document(file, model, temp, max_tok):
    """Handle document processing"""
    if file is None:
        return "No document uploaded."
    if model == "separator":
        return "Please select a valid model."
    
    # Simulate document processing
    return f"Model: {model}\nTemperature: {temp}\nMax Tokens: {max_tok}\n\n[Document processing placeholder - implement your logic here!]"

def create_interface():
    """Create and return the Gradio interface"""
    
    # Create a custom theme with standard fonts
    custom_theme = gr.themes.Default(
        font=("Arial", "sans-serif"),
        font_mono=("Courier", "monospace")
    )
    
    with gr.Blocks(title="LLM Playground", theme=custom_theme) as app:
        gr.Markdown(
            """
            # 🚀 LLM Models Playground
            
            Welcome to the LLM Playground! This is a fun experimental space to interact with various language models.
            Feel free to explore, experiment, and enjoy!
            """
        )
        
        # Model selection for both tabs
        model_dropdown = gr.Dropdown(
            choices=[
                ("🤖 OpenAI", "OpenAI"),
                ("🤖 Anthropic Claude", "Anthropic Claude"),
                ("🤖 Google Gemini", "Google Gemini"),
                ("--- Open Source Models ---", "separator"),
                ("🤖 Llama", "Llama"),
                ("🤖 Mistral", "Mistral"),
                ("🤖 Phi-3", "Phi-3"),
            ],
            value="OpenAI",
            label="Select Model"
        )
        
        with gr.Tabs():
            # Tab 0: Resources & Documentation
            with gr.Tab("📚 Resources & Documentation"):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### 📊 Model Analysis & Benchmarking")
                        
                        gr.Markdown("""
                        **Top Websites for Model Comparison:**
                        
                        • **Open LLM Leaderboard** 
                          https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
                        
                        • **LMSYS Chatbot Arena**
                          https://chat.lmsys.org
                        
                        • **Papers with Code**
                          https://paperswithcode.com/sota
                        
                        • **AI Models Arena**
                          https://arena.lmsys.org
                        
                        • **SEAL**
                          https://seal.mit.edu
                        
                        • **Velum**
                          https://velum.ai
                        
                        • **Artificial Analysis**
                          https://artificialanalysis.ai
                        """)
                        
                        gr.Markdown("### 🛠️ Essential Tools & Frameworks")
                        
                        gr.Markdown("""
                        **LLM Development:**
                        
                        • **LangChain** - Building LLM applications
                          https://python.langchain.com
                          - Chain different components
                          - Work with multiple LLM providers
                          - Document loaders and vector stores
                        
                        • **LlamaIndex** - LLM data frameworks
                          https://llamaindex.ai
                          - Querying and indexing data
                          - Semantic search capabilities
                          - Integrated with major LLM providers
                        
                        • **Hugging Face Transformers**
                          https://huggingface.co
                          - Largest model repository
                          - Easy model loading and deployment
                          - Pre-trained models for every task
                        
                        • **Ollama** - Run LLMs locally
                          https://ollama.ai
                          - Download and run models locally
                          - No API needed
                          - Privacy-focused
                        """)
                    
                    with gr.Column(scale=1):
                        gr.Markdown("### 💡 Quick Reference Guide")
                        
                        gr.Markdown("""
                        **Parameters Explained:**
                        
                        **Temperature** (0.1-2.0)
                        - 0.1-0.3: Very focused, deterministic
                        - 0.7-0.9: Balanced creativity
                        - 1.0-2.0: Highly creative/random
                        
                        **Max Tokens** (50-2000)
                        - Sets max response length
                        - Lower = shorter responses
                        - Higher = longer responses
                        
                        **Model Types:**
                        - Closed models: Usually best performance
                        - Open source: Customizable, local
                        """)
            
            # Tab 1: Chatbot
            with gr.Tab("💬 Chatbot"):
                with gr.Row():
                    with gr.Column(scale=3):
                        chatbot = gr.Chatbot(
                            label="Conversation",
                            height=450,
                            show_label=True,
                            type="messages"
                        )
                        prompt_textbox = gr.Textbox(
                            label="Enter your message",
                            placeholder="Type your message here...",
                            lines=2
                        )
                        with gr.Row():
                            submit_btn = gr.Button("Send", variant="primary", scale=2)
                            clear_btn = gr.Button("Clear", variant="secondary", scale=1)
                    
                    with gr.Column(scale=1):
                        gr.Markdown("### Settings")
                        temperature_slider = gr.Slider(
                            minimum=0.1,
                            maximum=2.0,
                            value=0.7,
                            step=0.1,
                            label="Temperature"
                        )
                        max_tokens_slider = gr.Slider(
                            minimum=50,
                            maximum=2000,
                            value=500,
                            step=50,
                            label="Max Tokens"
                        )
            
            # Tab 2: Multi-Model Chat
            with gr.Tab("🤝 Multi-Model Chat"):
                gr.Markdown("### Let models chat with each other!")
                gr.Markdown("Select two models and watch them have a conversation.")
                
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("### Model Selection")
                        
                        model1_dropdown = gr.Dropdown(
                            choices=[
                                ("🤖 OpenAI", "OpenAI"),
                                ("🤖 Anthropic Claude", "Anthropic Claude"),
                                ("🤖 Google Gemini", "Google Gemini"),
                                ("--- Open Source Models ---", "separator"),
                                ("🤖 Llama", "Llama"),
                                ("🤖 Mistral", "Mistral"),
                                ("🤖 Phi-3", "Phi-3"),
                            ],
                            value="OpenAI",
                            label="Model 1"
                        )
                        
                        model2_dropdown = gr.Dropdown(
                            choices=[
                                ("🤖 OpenAI", "OpenAI"),
                                ("🤖 Anthropic Claude", "Anthropic Claude"),
                                ("🤖 Google Gemini", "Google Gemini"),
                                ("--- Open Source Models ---", "separator"),
                                ("🤖 Llama", "Llama"),
                                ("🤖 Mistral", "Mistral"),
                                ("🤖 Phi-3", "Phi-3"),
                            ],
                            value="Anthropic Claude",
                            label="Model 2"
                        )
                        
                        conversation_topic = gr.Textbox(
                            label="Conversation Topic/Prompt",
                            placeholder="Enter the topic you want the models to discuss...",
                            lines=3,
                            value="Discuss the future of AI and its impact on society."
                        )
                        
                        with gr.Row():
                            start_chat_btn = gr.Button("Start Conversation", variant="primary", size="lg")
                            stop_chat_btn = gr.Button("Stop", variant="stop")
                        
                        gr.Markdown("### ⚙️ Settings")
                        
                        with gr.Row():
                            num_exchanges_slider = gr.Slider(
                                minimum=2,
                                maximum=20,
                                value=5,
                                step=1,
                                label="Number of Exchanges"
                            )
                        
                        with gr.Row():
                            multi_temperature_slider = gr.Slider(
                                minimum=0.1,
                                maximum=2.0,
                                value=0.7,
                                step=0.1,
                                label="Temperature"
                            )
                            
                            multi_max_tokens_slider = gr.Slider(
                                minimum=50,
                                maximum=2000,
                                value=500,
                                step=50,
                                label="Max Tokens"
                            )
                    
                    with gr.Column():
                        gr.Markdown("### 💬 Watch and Interject")
                        multi_chat_display = gr.Textbox(
                            label="Multi-Model Conversation",
                            lines=18,
                            interactive=False,
                            placeholder="Click 'Start Conversation' to begin the multi-model chat..."
                        )
                        
                        gr.Markdown("### Add Your Input")
                        
                        responder_model_dropdown = gr.Dropdown(
                            choices=[
                                ("Model 1 (Current)", "model1"),
                                ("Model 2 (Current)", "model2"),
                            ],
                            value="model1",
                            label="Select Which Model Responds"
                        )
                        
                        user_interjection = gr.Textbox(
                            label="Your Message (Interject in the conversation)",
                            placeholder="Type your message to add to the conversation...",
                            lines=2
                        )
                        
                        with gr.Row():
                            add_user_msg_btn = gr.Button("Send Your Message", variant="secondary")
                            clear_convo_btn = gr.Button("Clear Conversation", variant="secondary")
            
            # Tab 3: Document Analyzer
            with gr.Tab("📄 Document Analyzer"):
                gr.Markdown("### Upload documents and ask questions about them!")
                
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("### 📁 Upload and Process Documents")
                        
                        document_input = gr.File(
                            label="Upload Document",
                            type="filepath",
                            file_types=[".txt", ".pdf", ".md", ".docx"],
                            file_count="multiple"
                        )
                        
                        gr.Markdown("**OR paste text directly:**")
                        
                        document_text = gr.Textbox(
                            label="Enter Text Content",
                            lines=8,
                            placeholder="Paste your text here or upload a file above..."
                        )
                        
                        process_btn = gr.Button("Process Documents", variant="primary")
                        
                        gr.Markdown("### 📊 Document Status")
                        document_status = gr.Textbox(
                            label="Status",
                            value="No documents loaded yet.",
                            interactive=False,
                            lines=2
                        )
                        
                    with gr.Column():
                        gr.Markdown("### Model Response")
                        document_output = gr.Textbox(
                            label="Analysis Result",
                            lines=10,
                            interactive=False
                        )
                        
                        gr.Markdown("### 💬 Ask Questions About Your Document")
                        
                        rag_query = gr.Textbox(
                            label="Your Question",
                            placeholder="Ask a question about your uploaded document...",
                            lines=2
                        )
                        
                        with gr.Row():
                            ask_question_btn = gr.Button("Ask Question", variant="primary", scale=2)
                            clear_btn = gr.Button("Clear", variant="secondary", scale=1)
            
            # Tab 5: Email Q&A
            with gr.Tab("📧 Email Q&A"):
                gr.Markdown("### Connect to your email and ask questions about your emails!")
                
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### 🔌 Email Connection")
                        
                        email_provider_dropdown = gr.Dropdown(
                            choices=[
                                ("Gmail", "gmail"),
                                ("Outlook", "outlook"),
                                ("Yahoo", "yahoo"),
                                ("IMAP/SMTP", "imap"),
                            ],
                            value="gmail",
                            label="Email Provider"
                        )
                        
                        gr.Markdown("### 🔑 Authentication")
                        
                        email_address = gr.Textbox(
                            label="Email Address",
                            placeholder="your.email@example.com"
                        )
                        
                        email_password = gr.Textbox(
                            label="App Password / Access Token",
                            type="password",
                            placeholder="Enter your app password or access token"
                        )
                        
                        connect_email_btn = gr.Button("Connect to Email", variant="primary")
                        
                        disconnect_email_btn = gr.Button("Disconnect", variant="secondary")
                        
                        gr.Markdown("### 📊 Connection Status")
                        email_status = gr.Textbox(
                            label="Status",
                            value="Not connected. Please enter your credentials.",
                            interactive=False,
                            lines=2
                        )
                        
                        gr.Markdown("### ⚙️ Settings")
                        
                        email_query_type = gr.Radio(
                            choices=[
                                ("Recent emails (last 7 days)", "recent"),
                                ("Specific timeframe", "timeframe"),
                                ("All emails", "all"),
                            ],
                            value="recent",
                            label="Query Scope"
                        )
                        
                        num_emails_limit = gr.Slider(
                            minimum=10,
                            maximum=500,
                            value=100,
                            step=10,
                            label="Max Emails to Index"
                        )
                    
                    with gr.Column(scale=2):
                        gr.Markdown("### 💬 Ask Questions About Your Emails")
                        
                        email_chatbot = gr.Chatbot(
                            label="Email Q&A Conversation",
                            height=450,
                            show_label=True,
                            type="messages"
                        )
                        
                        email_query = gr.Textbox(
                            label="Your Question",
                            placeholder="Ask questions about your emails. Examples: 'What did I receive from Amazon?', 'Show me important emails from last week', etc.",
                            lines=3
                        )
                        
                        with gr.Row():
                            ask_email_btn = gr.Button("Ask About Emails", variant="primary", scale=2)
                            clear_email_chat_btn = gr.Button("Clear Chat", variant="secondary", scale=1)
        
        gr.Markdown(
            """
            ---
            ### 💡 Tips
            - **Resources & Documentation Tab**: Comprehensive guide to model analysis websites, tools, and learning resources
            - **Chatbot Tab**: Have interactive conversations with AI models
            - **Multi-Model Chat Tab**: Watch two AI models have a conversation with each other
            - **Document Analyzer Tab**: Upload documents and ask questions about them using RAG (Retrieval-Augmented Generation)
            - **Email Q&A Tab**: Connect to your email and ask questions about your emails using AI
            - Experiment with different temperature values to see how it affects creativity
            - Adjust max tokens to control response length
            - Use app passwords or access tokens for secure email connections
            """
        )
        
        # Chatbot functionality
        submit_btn.click(
            fn=chatbot_response,
            inputs=[prompt_textbox, chatbot, model_dropdown, temperature_slider, max_tokens_slider],
            outputs=[chatbot, prompt_textbox]
        )
        
        clear_btn.click(
            fn=lambda: [],
            outputs=[chatbot]
        )
        
        # Document functionality
        process_btn.click(
            fn=process_document,
            inputs=[document_input, model_dropdown, temperature_slider, max_tokens_slider],
            outputs=[document_output]
        )
    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch(server_name="0.0.0.0", server_port=7860, share=True, inbrowser=True)

