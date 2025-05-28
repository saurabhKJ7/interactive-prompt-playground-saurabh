# Interactive Prompt Playground

A tool for experimenting with different LLM parameters and analyzing their effects on product descriptions.

## Features

- Test different parameter combinations:
  - Temperature (0.0, 0.7, 1.2)
  - Max tokens (50, 150, 300)
  - Presence penalty (0.0, 1.5)
  - Frequency penalty (0.0, 1.5)
- Support for multiple models (gpt-3.5-turbo)
- Customizable system and user prompts
- Automated experiment runner
- Detailed analysis of parameter effects
- Results saved to CSV files

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script:
```bash
python prompt_playground.py
```

The script will:
1. Run experiments with all parameter combinations
2. Save results to CSV files (one per model)
3. Provide analysis of parameter effects

## Parameter Effects Analysis

### Temperature
- 0.0: More deterministic, focused outputs
- 0.7: Balanced creativity and consistency
- 1.2: More creative and varied responses

### Token Length
- 50: Very concise, may be incomplete
- 150: Balanced length, captures key features
- 300: More detailed and comprehensive

### Penalties
- Presence Penalty: Discourages repetition
- Frequency Penalty: Discourages common phrases
- Higher values (1.5) prevent repetitive patterns

### Model Comparison
- GPT-4: More sophisticated and nuanced descriptions
- GPT-3.5-turbo: Faster but slightly less detailed

## Results Format

- model
- temperature
- max_tokens
- presence_penalty
- frequency_penalty
- response


## Parameter Effects Table

| Temperature | Max Tokens | Presence Penalty | Frequency Penalty | Description Length | Creativity | Repetition | Example Response |
|-------------|------------|------------------|-------------------|--------------------|------------|------------|-----------------|
| 0.0 | 50 | 0.0 | 0.0 | Short | Low | High | "Introducing the iPhone 15 Pro, the pinnacle of innovation and technology in the palm of your hand. This cutting-edge device combines sleek design with powerful performance to elevate your mobile experience like never before." |
| 0.0 | 50 | 0.0 | 1.5 | Short | Low | Low | "Introducing the iPhone 15 Pro, where innovation meets sophistication. Elevate your mobile experience with this cutting-edge device that redefines what a smartphone can do." |
| 0.0 | 50 | 1.5 | 0.0 | Short | Low | Low | "Introducing the iPhone 15 Pro, where innovation meets sophistication. Elevate your mobile experience with this cutting-edge device that redefines what a smartphone can do." |
| 0.0 | 50 | 1.5 | 1.5 | Short | Low | Low | "Introducing the iPhone 15 Pro, a cutting-edge device that redefines innovation and sophistication. With its sleek design and advanced technology, this smartphone is sure to impress even the most discerning tech enthusiasts." |
| 0.0 | 150 | 0.0 | 0.0 | Medium | Low | High | "Introducing the iPhone 15 Pro, the pinnacle of innovation and technology in the palm of your hand... With the latest A16 Bionic chip, this smartphone offers lightning-fast speeds and seamless multitasking, ensuring smooth performance for all your apps and games." |
| 0.0 | 150 | 0.0 | 1.5 | Medium | Low | Low | "Introducing the iPhone 15 Pro, where innovation meets sophistication... The powerful A16 Bionic chip ensures seamless performance for all your multitasking needs, from gaming to productivity tasks." |
| 0.0 | 150 | 1.5 | 0.0 | Medium | Low | Low | "Introducing the iPhone 15 Pro, a cutting-edge marvel that redefines smartphone technology... With its sleek design and advanced technology, this device is sure to elevate your mobile experience to new heights." |
| 0.0 | 150 | 1.5 | 1.5 | Medium | Low | Low | "Introducing the iPhone 15 Pro, where innovation meets sophistication... The powerful A16 Bionic chip ensures seamless performance for all your multitasking needs, from gaming to productivity tasks." |
| 0.0 | 300 | 0.0 | 0.0 | Long | Low | High | "Introducing the iPhone 15 Pro, the pinnacle of innovation and technology in the palm of your hand... Experience the future of mobile technology with the iPhone 15 Pro. Elevate your everyday with a device that combines style, performance, and innovation in one sleek package." |
| 0.0 | 300 | 0.0 | 1.5 | Long | Low | Low | "Introducing the iPhone 15 Pro, a cutting-edge marvel that redefines smartphone technology... Experience true innovation with the iPhone 15 Pro – where style meets substance in one extraordinary device." |
| 0.0 | 300 | 1.5 | 0.0 | Long | Low | Low | "Introducing the iPhone 15 Pro, where innovation meets sophistication... Experience the future of smartphones with the iPhone 15 Pro – where style, functionality, and innovation converge to create a truly exceptional device." |
| 0.0 | 300 | 1.5 | 1.5 | Long | Low | Low | "Introducing the iPhone 15 Pro, a cutting-edge device that redefines innovation and sophistication... Experience security at its finest with Face ID recognition for effortless unlocking of your device while keeping your data safe from prying eyes." |
| 0.7 | 50 | 0.0 | 0.0 | Short | High | High | "Introducing the iPhone 15 Pro - the pinnacle of innovation and sophistication in the world of smartphones. With its sleek design and cutting-edge technology, this device is truly in a league of its own." |
| 0.7 | 50 | 0.0 | 1.5 | Short | High | Low | "Introducing the iPhone 15 Pro - the pinnacle of innovation and technology in the palm of your hand. This cutting-edge device boasts a stunning Super Retina XDR display that brings your content to life with vibrant colors and crisp details." |
| 0.7 | 50 | 1.5 | 0.0 | Short | High | Low | "Introducing the iPhone 15 Pro, where cutting-edge technology meets sleek design to redefine what a smartphone can do. Packed with innovative features and premium craftsmanship, this flagship device is a true game-changer." |
| 0.7 | 50 | 1.5 | 1.5 | Short | High | Low | "Introducing the iPhone 15 Pro, where cutting-edge technology and sleek design meet to elevate your mobile experience. This powerhouse of a device is packed with top-of-the-line features that will revolutionize how you connect, create, and communicate." |
| 0.7 | 150 | 0.0 | 0.0 | Medium | High | High | "Introducing the iPhone 15 Pro - the pinnacle of technological innovation and craftsmanship... Stay connected and productive with 5G capabilities, enabling seamless streaming, downloading, and communication." |
| 0.7 | 150 | 0.0 | 1.5 | Medium | High | Low | "Introducing the iPhone 15 Pro, the pinnacle of innovation and technology in your hands... With enhanced security features like Face ID, your personal information remains safe while unlocking your device." |
| 0.7 | 150 | 1.5 | 0.0 | Medium | High | Low | "Introducing the iPhone 15 Pro - a cutting-edge smartphone that redefines excellence in technology... The iPhone 15 Pro offers lightning-fast performance and seamless multitasking." |
| 0.7 | 150 | 1.5 | 1.5 | Medium | High | Low | "Introducing the iPhone 15 Pro, where cutting-edge technology meets sleek design... The iPhone 15 Pro offers immersive sound quality through spatial audio support for an unparalleled listening experience." |
| 0.7 | 300 | 0.0 | 0.0 | Long | High | High | "Introducing the iPhone 15 Pro - the pinnacle of innovation in the world of smartphones... Experience the future of mobile technology with the iPhone 15 Pro. With its sleek design, top-of-the-line features, and unparalleled performance, this device is truly in a league of its own." |
| 0.7 | 300 | 0.0 | 1.5 | Long | High | Low | "Experience the pinnacle of smartphone technology with the iPhone 15 Pro... Step into a new era of mobile innovation with the iPhone 15 Pro – where power meets elegance to create an unparalleled user experience." |
| 0.7 | 300 | 1.5 | 0.0 | Long | High | Low | "Introducing the iPhone 15 Pro – where innovation meets sophistication... Experience the future of mobile technology with the iPhone 15 Pro. Upgrade to the ultimate smartphone that combines cutting-edge features, unparalleled performance, and sleek design in one powerful package." |
| 0.7 | 300 | 1.5 | 1.5 | Long | High | Low | "Introducing the iPhone 15 Pro - where cutting-edge technology meets sleek design... Your data stays secure with Face ID facial recognition technology for effortless unlocking and Apple Pay transactions." |


## Reflection: Parameter Impact Analysis

Adjusting the parameters in the language model significantly influenced the output style and quality. Temperature settings, ranging from 0.0 to 0.7, demonstrated a clear shift from factual and repetitive responses to more creative and varied content. The presence and frequency penalties, when set to 1.5, effectively reduced repetition and encouraged more diverse word choices, while max tokens controlled the length and detail of the responses, with longer outputs (300 tokens) providing richer feature coverage.

These parameter variations highlight the importance of fine-tuning for specific use cases. For example, marketing content benefits from higher temperature and max tokens for engaging descriptions, while technical documentation requires lower temperature for factual consistency. Understanding these effects is crucial for effective prompt engineering and achieving desired outcomes in different contexts.


