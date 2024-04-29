from dotenv import load_dotenv
import os
import pandas as pd
# updated: (below, checkout llama_index discord)
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context


load_dotenv()

    
population_pth = os.path.join("data", "WorldPopulation2023.csv")
population_df = pd.read_csv(population_pth)

population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})
population_query_engine.query("What's the population of Taiwan?")
