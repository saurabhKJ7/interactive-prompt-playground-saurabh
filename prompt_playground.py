from openai import OpenAI
import pandas as pd
from typing import Dict, List
import os
from dotenv import load_dotenv

# Load OpenAI API key from environment
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class PromptPlayground:
    def __init__(self):
        self.default_parameters = {
            'temperature': [0.0, 0.7, 1.2],
            'max_tokens': [50, 150, 300],
            'presence_penalty': [0.0, 1.5],
            'frequency_penalty': [0.0, 1.5],
            'models': ['gpt-3.5-turbo']
        }

    def run_experiment(self, system_prompt: str, user_prompt: str, model: str) -> pd.DataFrame:
        """Run experiments with different parameter combinations."""
        results = []
        for temp in self.default_parameters['temperature']:
            for max_tokens in self.default_parameters['max_tokens']:
                for presence in self.default_parameters['presence_penalty']:
                    for freq in self.default_parameters['frequency_penalty']:
                        try:
                            response = client.chat.completions.create(
                                model=model,
                                messages=[
                                    {"role": "system", "content": system_prompt},
                                    {"role": "user", "content": user_prompt}
                                ],
                                temperature=temp,
                                max_tokens=max_tokens,
                                presence_penalty=presence,
                                frequency_penalty=freq
                            )

                            result = {
                                'model': model,
                                'temperature': temp,
                                'max_tokens': max_tokens,
                                'presence_penalty': presence,
                                'frequency_penalty': freq,
                                'response': response.choices[0].message.content
                            }
                            results.append(result)
                        except Exception as e:
                            print(f"Error with params {temp}, {max_tokens}, {presence}, {freq}: {str(e)}")
                            continue

        return pd.DataFrame(results)

    def analyze_results(self, df: pd.DataFrame) -> str:
        # Basic placeholder analysis
        return f"Generated {len(df)} combinations. Here’s a sample response:\n\n{df.iloc[0]['response']}"


# Example usage
def main():
    # Get user input for product type
    product_type = input("Enter the product type (e.g., iPhone, Tesla, running shoes): ")
    
    # Create system and user prompts based on input
    system_prompt = "You are a product description expert. Write compelling product descriptions that highlight key features and benefits."
    user_prompt = f"Write a product description for {product_type}"

    playground = PromptPlayground()

    for model in ['gpt-3.5-turbo']:
        print(f"\nRunning experiments for model: {model}")
        print(f"Generating descriptions for: {product_type}")
        results_df = playground.run_experiment(system_prompt, user_prompt, model)

        print("\nExperiment Results:")
        print("-" * 80)
        print(results_df.to_string(index=False))
        print("\nAnalysis:")
        print("-" * 80)
        analysis = playground.analyze_results(results_df)
        print(analysis)


if __name__ == "__main__":
    main()
