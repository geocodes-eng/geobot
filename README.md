# 🌍 Geo Agent Demo

A powerful Gradio application that combines intelligent coordinate analysis with AI chat capabilities for liquefaction susceptibility assessment.
[Link to the app.](https://huggingface.co/spaces/GeotechnicalCoder/geobot)

## 🚀 Features

### 🗺️ Smart Coordinate Analysis
- **Intelligent Extraction**: Uses regex patterns with LLM fallback for robust coordinate parsing
- **Multiple Formats**: Supports various input formats:
  - Standard: `1511300, 5266130`
  - Labeled: `x: 1511300, y: 5266130`
  - Natural Language: `"What's the liquefaction at coordinates 1511300, 5266130?"`
- **Real-time Data**: Queries Canterbury Liquefaction Susceptibility ArcGIS MapServer
- **Fast Processing**: Regex-first approach ensures quick responses

### 🤖 AI Chat Assistant
- **Powered by Qwen**: Uses Qwen/Qwen3-0.6B model for intelligent conversations
- **General Knowledge**: Also handles general questions and conversations


## 💻 Usage

### Coordinate Analysis
1. Navigate to the "Coordinate Analysis" tab
2. Enter coordinates in any supported format
3. Click "Analyze Coordinates" to get results
4. View liquefaction susceptibility data

### Chat Assistant
1. Switch to the "Chat Assistant" tab
2. Type your question or message
3. Click "Send Message" for AI response
4. Get helpful information and guidance

## 🔧 Technical Architecture

- **Frontend**: Gradio 4.0+ with modern UI components
- **AI Model**: Qwen/Qwen3-0.6B (Hugging Face Transformers)
- **Coordinate System**: NZTM (New Zealand Transverse Mercator)
- **Data Source**: Canterbury Liquefaction Susceptibility ArcGIS MapServer
- **Processing**: Hybrid regex + LLM approach for optimal performance

## 📊 Example Inputs

### Coordinate Analysis Examples:
```
1511300, 5266130
x: 1511300, y: 5266130
What's the liquefaction at coordinates 1511300, 5266130?
Can you check 1511300, 5266130 for me?
```

### Chat Assistant Examples:
```
Hello, what can you help me with?
What is liquefaction susceptibility?
How do I use this application?
```

## 🚀 Deployment

### Hugging Face Spaces
This application is optimized for Hugging Face Spaces deployment:

1. **Create Space**: New Gradio Space on huggingface.co/spaces
2. **Upload Files**: 
   - `app.py` (main application)
   - `requirements.txt` (dependencies)
   - `query.py` (coordinate query module)
3. **Configure**: 
   - Hardware: CPU (recommended)
   - Python: 3.9+
   - Visibility: Public/Private

### Local Development
```bash
pip install -r requirements.txt
python app.py
```

## 📋 Requirements

- Python 3.9+
- Gradio >= 4.0.0
- Transformers >= 4.30.0
- Torch >= 2.0.0
- Requests >= 2.28.0

## 🔍 How It Works

1. **Input Processing**: User provides coordinates or questions
2. **Smart Parsing**: Regex patterns extract coordinates, LLM handles complex queries
3. **Data Retrieval**: Queries ArcGIS MapServer for geological data
4. **Response Generation**: AI generates helpful responses and explanations
5. **Result Display**: Clean, formatted output for easy interpretation

## 🤝 Contributing

Feel free to contribute by:
- Reporting bugs
- Suggesting new features
- Improving documentation
- Adding new coordinate formats

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ for the geological and engineering community** 
