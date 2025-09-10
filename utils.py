import pandas as pd

def save_results(results, filename="results/results.csv"):
    """Save results into a CSV file."""
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"✅ Results saved to {filename}")
